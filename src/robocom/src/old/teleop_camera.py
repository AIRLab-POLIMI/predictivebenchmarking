#!/usr/bin/env python
"""
Robocom teleoperator node
"""

import math, sys, os, time

import pygame
from pygame.locals import *

import roslib; roslib.load_manifest("triskar")
import rospy
from sensor_msgs.msg import Image
from robocom.msg import Velocity, Proximity

from filters import ExpFilter, SmoothedVec3


# Global constants
SCREEN_SIZE         = ( 640, 480 )
MOUSE_SENS          = ( 0.02, 0.02 )
SP_IMPULSE_SPEED    = ( ( 0.25, 0.25, 0.5 ), ( 1.0, 1.0, 1.0 ) )    # Normal, fast
ROS_TO_SURF_ENC     = { "mono8":"P", "rgb8":"RGB", "bgr8":"BGR", "rgba8":"RGBA" }
EAST = 0; NORTH = 1; WEST = 2; SOUTH = 3
PROXIMITY_THRESHOLD = ( 0.1, 0.1, 0.1, 0.1 )    # Don't move where lower

# Global variables
screen              = None
camera_frame        = None
mouse_grabbed       = False
proximities         = [ 1.0, 1.0, 1.0, 1.0 ]


def camera_frame_cb(msg):
    """ Camera frame callback """
    global camera_frame
    size = (msg.width, msg.height)
    encoding = ROS_TO_SURF_ENC[msg.encoding]
    frame = pygame.image.frombuffer(msg.data, size, encoding)
    frame = pygame.transform.smoothscale(frame, screen.get_size())
    camera_frame = frame.convert()


def proximity_cb(msg):
    """ Proximity sensors callback """
    proximities = msg.proximities[:]


def center_mouse(screenSize):
    """ Centers the mouse """
    pygame.event.set_blocked(MOUSEMOTION)
    pygame.mouse.set_pos((screenSize[0] / 2, screenSize[1] / 2))
    pygame.event.set_allowed(MOUSEMOTION)
    

def grab_mouse(grabbed):
    """ Grabs/ungrabs the mouse """
    global mouse_grabbed
    if grabbed and not mouse_grabbed:
        mouse_grabbed = True
        pygame.mouse.set_visible(False)
    elif not grabbed and mouse_grabbed:
        mouse_grabbed = False
        pygame.mouse.set_visible(True)


def handle_inputs(sp_accum, sp_impulse):
    """ Processes mouse inputs """
    
    # Configure mouse movements (accumulated if left button held)
    for i in range(3): sp_impulse[i] = 0.0
    sp_temp = [ 0.0, 0.0, 0.0 ]
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:
        mouse_scale = ( 0.1 * MOUSE_SENS[0], 0.1 * MOUSE_SENS[1] )
    else:
        mouse_scale = MOUSE_SENS
        for i in range(3): sp_accum[i] = 0.0
    
    # Process events since the last call
    for e in pygame.event.get():
        if e.type is QUIT:
            rospy.signal_shutdown("User closed the teleoperator window")
        elif e.type is KEYDOWN:
            grab_mouse(not e.key is K_ESCAPE)
        elif e.type is KEYUP:
            if not e.key is K_ESCAPE: grab_mouse(True)
        elif e.type is MOUSEBUTTONDOWN:
            grab_mouse(True)
        elif e.type is MOUSEBUTTONUP:
            grab_mouse(True)
        elif e.type is MOUSEMOTION and mouse_grabbed:
            screenSize = screen.get_size()
            center_mouse(screenSize)
            sp_temp[1] -= float(e.rel[1]) * mouse_scale[1]      # Fwd / Bwd
            if mouse_buttons[2]: sp_temp[0] += float(e.rel[0]) * mouse_scale[0]  # Strafe
            else:                sp_temp[2] -= float(e.rel[0]) * mouse_scale[0]  # Turn
    
    # Process keyboard impulses
    keys = pygame.key.get_pressed()
    mods = pygame.key.get_mods()
    gear = int(bool(mods & KMOD_SHIFT))
    if keys[K_d]: sp_impulse[0] += SP_IMPULSE_SPEED[gear][0]
    if keys[K_a]: sp_impulse[0] -= SP_IMPULSE_SPEED[gear][0]
    if keys[K_w]: sp_impulse[1] += SP_IMPULSE_SPEED[gear][1]
    if keys[K_s]: sp_impulse[1] -= SP_IMPULSE_SPEED[gear][1]
    if keys[K_q]: sp_impulse[2] += SP_IMPULSE_SPEED[gear][2]
    if keys[K_e]: sp_impulse[2] -= SP_IMPULSE_SPEED[gear][2]
    
    # Apply mouse movements (either accumulated motion or impulses)
    if mouse_buttons[0]:
        for i in range(3): sp_accum[i] += sp_temp[i]
    else:
        for i in range(3): sp_impulse[i] += sp_temp[i]

    # Block movements towards constrained directions
    if proximities[EAST] < PROXIMITY_THRESHOLD[EAST]:
        sp_accum[0]   = min(0.0, sp_accum[0])
        sp_impulse[0] = min(0.0, sp_impulse[0])
    if proximities[WEST] < PROXIMITY_THRESHOLD[WEST]:
        sp_accum[0]   = max(0.0, sp_accum[0])
        sp_impulse[0] = max(0.0, sp_impulse[0])
    if proximities[NORTH] < PROXIMITY_THRESHOLD[NORTH]:
        sp_accum[1]   = min(0.0, sp_accum[1])
        sp_impulse[1] = min(0.0, sp_impulse[1])
    if proximities[SOUTH] < PROXIMITY_THRESHOLD[SOUTH]:
        sp_accum[1]   = max(0.0, sp_accum[1])
        sp_impulse[1] = max(0.0, sp_impulse[1])


def draw_circle_arc(surface, color, pos, radius, start, stop, width=0):
    """ Draws a centered arc """
    rect = ((pos[0] - radius, pos[1] - radius), (2 * radius, 2 * radius))
    if start > stop: (start, stop) = (stop, start)
    pygame.draw.arc(screen, 0x0000FF, rect, start, stop, width)


def render_scene(screen, setpoint):
    """ Renders the current screen frame """
    screen.fill(0x808080)
    screen.blit(camera_frame, ( 0, 0 ))

    c = screen.get_size()
    c = ( c[0] / 2, c[1] / 2 )
    r = min([ 64, c[0], c[1] ])
    pygame.draw.line(screen, 0xFF0000, c, (int(c[0] + r * setpoint[0]), c[1]), 2)
    pygame.draw.line(screen, 0x00FF00, c, (c[0], int(c[1] - r * setpoint[1])), 2)
    draw_circle_arc(screen, 0x0000FF, c, r, math.pi/2, math.pi/2 + setpoint[2], 2)
    pygame.draw.circle(screen, 0xFFFFFF, c, 2)


def main():
    # Initialize pygame stuff
    global screen, camera_frame
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    screen.fill(0x808080)
    pygame.display.flip()
    pygame.display.set_caption("Triskar2 teleoperator")
    pygame.mouse.set_visible(True)
    camera_frame = pygame.Surface(( 1, 1 )).convert()   # Fake camera frame placeholder

    # Initialize ROS stuff
    rospy.init_node("teleop_node")
    pubVelocity = rospy.Publisher("robocom/velocity", Velocity)
    pubVelocity.publish(Velocity(0.0, 0.0, 0.0))
    rospy.Subscriber("robocom/front_camera", Image, camera_frame_cb)
    rospy.Subscriber("robocom/proximity", Proximity, proximity_cb)
    
    # Initialize setpoints
    sp_impulse = [ 0.0, 0.0, 0.0 ]
    sp_accum = [ 0.0, 0.0, 0.0 ]
    sp_smooth = SmoothedVec3(ExpFilter(1.0 / 60, 1.0, 0.000001), sp_accum)
    
    while not rospy.is_shutdown():
        # Process inputs
        handle_inputs(sp_accum, sp_impulse)
        if rospy.is_shutdown(): break
        sp = sp_smooth.process([ sp_impulse[i] + sp_accum[i] for i in range(3) ])
        pubVelocity.publish(Velocity(sp[0], sp[1]))
        
        # Render the scene
        render_scene(screen, sp)
        pygame.display.flip()
        clock.tick(60)

    # Stop the robot
    pubVelocity.publish(Velocity(0.0, 0.0))


# Call the 'main' function when this script is executed
if __name__ == "__main__":
    try: main()
    except rospy.ROSInterruptException: pass

