;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::EmRobot)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'EmRobot (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::EMROBOT")
  (make-package "ADHOC_COMMUNICATION::EMROBOT"))

(in-package "ROS")
;;//! \htmlinclude EmRobot.msg.html


(defclass adhoc_communication::EmRobot
  :super ros::object
  :slots (_id _state _selected_ds _x _y ))

(defmethod adhoc_communication::EmRobot
  (:init
   (&key
    ((:id __id) 0)
    ((:state __state) 0)
    ((:selected_ds __selected_ds) 0)
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _state (round __state))
   (setq _selected_ds (round __selected_ds))
   (setq _x (float __x))
   (setq _y (float __y))
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:state
   (&optional __state)
   (if __state (setq _state __state)) _state)
  (:selected_ds
   (&optional __selected_ds)
   (if __selected_ds (setq _selected_ds __selected_ds)) _selected_ds)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:serialization-length
   ()
   (+
    ;; int32 _id
    4
    ;; int32 _state
    4
    ;; int32 _selected_ds
    4
    ;; float32 _x
    4
    ;; float32 _y
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _id
       (write-long _id s)
     ;; int32 _state
       (write-long _state s)
     ;; int32 _selected_ds
       (write-long _selected_ds s)
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _id
     (setq _id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _state
     (setq _state (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _selected_ds
     (setq _selected_ds (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get adhoc_communication::EmRobot :md5sum-) "c8b0953d68d06c5193efb226a802f624")
(setf (get adhoc_communication::EmRobot :datatype-) "adhoc_communication/EmRobot")
(setf (get adhoc_communication::EmRobot :definition-)
      "int32 id
int32 state # see energy_mgmt/docking.h
int32 selected_ds #the id of the docking stationc currelty selected by the robot to recharge
float32 x    #robot x-coordinate (in the reference system of the sending robot, not in the one of the receiver)
float32 y    #robot y-coordinate (in the reference system of the sending robot, not in the one of the receiver)

")



(provide :adhoc_communication/EmRobot "c8b0953d68d06c5193efb226a802f624")


