;; Auto-generated. Do not edit!


(when (boundp 'nav2d_msgs::LocalizedScan)
  (if (not (find-package "NAV2D_MSGS"))
    (make-package "NAV2D_MSGS"))
  (shadow 'LocalizedScan (find-package "NAV2D_MSGS")))
(unless (find-package "NAV2D_MSGS::LOCALIZEDSCAN")
  (make-package "NAV2D_MSGS::LOCALIZEDSCAN"))

(in-package "ROS")
;;//! \htmlinclude LocalizedScan.msg.html
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(defclass nav2d_msgs::LocalizedScan
  :super ros::object
  :slots (_robot_id _laser_type _x _y _yaw _scan ))

(defmethod nav2d_msgs::LocalizedScan
  (:init
   (&key
    ((:robot_id __robot_id) 0)
    ((:laser_type __laser_type) 0)
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:yaw __yaw) 0.0)
    ((:scan __scan) (instance sensor_msgs::LaserScan :init))
    )
   (send-super :init)
   (setq _robot_id (round __robot_id))
   (setq _laser_type (round __laser_type))
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _yaw (float __yaw))
   (setq _scan __scan)
   self)
  (:robot_id
   (&optional __robot_id)
   (if __robot_id (setq _robot_id __robot_id)) _robot_id)
  (:laser_type
   (&optional __laser_type)
   (if __laser_type (setq _laser_type __laser_type)) _laser_type)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:yaw
   (&optional __yaw)
   (if __yaw (setq _yaw __yaw)) _yaw)
  (:scan
   (&rest __scan)
   (if (keywordp (car __scan))
       (send* _scan __scan)
     (progn
       (if __scan (setq _scan (car __scan)))
       _scan)))
  (:serialization-length
   ()
   (+
    ;; int8 _robot_id
    1
    ;; int8 _laser_type
    1
    ;; float32 _x
    4
    ;; float32 _y
    4
    ;; float32 _yaw
    4
    ;; sensor_msgs/LaserScan _scan
    (send _scan :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _robot_id
       (write-byte _robot_id s)
     ;; int8 _laser_type
       (write-byte _laser_type s)
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _yaw
       (sys::poke _yaw (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; sensor_msgs/LaserScan _scan
       (send _scan :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _robot_id
     (setq _robot_id (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _robot_id 127) (setq _robot_id (- _robot_id 256)))
   ;; int8 _laser_type
     (setq _laser_type (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _laser_type 127) (setq _laser_type (- _laser_type 256)))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _yaw
     (setq _yaw (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; sensor_msgs/LaserScan _scan
     (send _scan :deserialize buf ptr-) (incf ptr- (send _scan :serialization-length))
   ;;
   self)
  )

(setf (get nav2d_msgs::LocalizedScan :md5sum-) "bab53504723a56692b3864ccf3dfe635")
(setf (get nav2d_msgs::LocalizedScan :datatype-) "nav2d_msgs/LocalizedScan")
(setf (get nav2d_msgs::LocalizedScan :definition-)
      "int8      robot_id
int8      laser_type
float32   x
float32   y
float32   yaw
sensor_msgs/LaserScan scan
================================================================================
MSG: sensor_msgs/LaserScan
# Single scan from a planar laser range-finder
#
# If you have another ranging device with different behavior (e.g. a sonar
# array), please find or create a different message, since applications
# will make fairly laser-specific assumptions about this data

Header header            # timestamp in the header is the acquisition time of 
                         # the first ray in the scan.
                         #
                         # in frame frame_id, angles are measured around 
                         # the positive Z axis (counterclockwise, if Z is up)
                         # with zero angle being forward along the x axis
                         
float32 angle_min        # start angle of the scan [rad]
float32 angle_max        # end angle of the scan [rad]
float32 angle_increment  # angular distance between measurements [rad]

float32 time_increment   # time between measurements [seconds] - if your scanner
                         # is moving, this will be used in interpolating position
                         # of 3d points
float32 scan_time        # time between scans [seconds]

float32 range_min        # minimum range value [m]
float32 range_max        # maximum range value [m]

float32[] ranges         # range data [m] (Note: values < range_min or > range_max should be discarded)
float32[] intensities    # intensity data [device-specific units].  If your
                         # device does not provide intensities, please leave
                         # the array empty.

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

")



(provide :nav2d_msgs/LocalizedScan "bab53504723a56692b3864ccf3dfe635")


