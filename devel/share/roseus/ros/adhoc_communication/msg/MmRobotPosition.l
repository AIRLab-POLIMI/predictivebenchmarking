;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::MmRobotPosition)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'MmRobotPosition (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::MMROBOTPOSITION")
  (make-package "ADHOC_COMMUNICATION::MMROBOTPOSITION"))

(in-package "ROS")
;;//! \htmlinclude MmRobotPosition.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass adhoc_communication::MmRobotPosition
  :super ros::object
  :slots (_src_robot _position ))

(defmethod adhoc_communication::MmRobotPosition
  (:init
   (&key
    ((:src_robot __src_robot) "")
    ((:position __position) (instance geometry_msgs::PoseStamped :init))
    )
   (send-super :init)
   (setq _src_robot (string __src_robot))
   (setq _position __position)
   self)
  (:src_robot
   (&optional __src_robot)
   (if __src_robot (setq _src_robot __src_robot)) _src_robot)
  (:position
   (&rest __position)
   (if (keywordp (car __position))
       (send* _position __position)
     (progn
       (if __position (setq _position (car __position)))
       _position)))
  (:serialization-length
   ()
   (+
    ;; string _src_robot
    4 (length _src_robot)
    ;; geometry_msgs/PoseStamped _position
    (send _position :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _src_robot
       (write-long (length _src_robot) s) (princ _src_robot s)
     ;; geometry_msgs/PoseStamped _position
       (send _position :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _src_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _src_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; geometry_msgs/PoseStamped _position
     (send _position :deserialize buf ptr-) (incf ptr- (send _position :serialization-length))
   ;;
   self)
  )

(setf (get adhoc_communication::MmRobotPosition :md5sum-) "b110eae90e8648401835f8c826926f86")
(setf (get adhoc_communication::MmRobotPosition :datatype-) "adhoc_communication/MmRobotPosition")
(setf (get adhoc_communication::MmRobotPosition :definition-)
      "string src_robot
geometry_msgs/PoseStamped position

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

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

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :adhoc_communication/MmRobotPosition "b110eae90e8648401835f8c826926f86")


