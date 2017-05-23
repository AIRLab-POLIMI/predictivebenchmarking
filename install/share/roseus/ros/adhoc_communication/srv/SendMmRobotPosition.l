;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::SendMmRobotPosition)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'SendMmRobotPosition (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::SENDMMROBOTPOSITION")
  (make-package "ADHOC_COMMUNICATION::SENDMMROBOTPOSITION"))
(unless (find-package "ADHOC_COMMUNICATION::SENDMMROBOTPOSITIONREQUEST")
  (make-package "ADHOC_COMMUNICATION::SENDMMROBOTPOSITIONREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::SENDMMROBOTPOSITIONRESPONSE")
  (make-package "ADHOC_COMMUNICATION::SENDMMROBOTPOSITIONRESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::SendMmRobotPositionRequest
  :super ros::object
  :slots (_dst_robot _topic _position ))

(defmethod adhoc_communication::SendMmRobotPositionRequest
  (:init
   (&key
    ((:dst_robot __dst_robot) "")
    ((:topic __topic) "")
    ((:position __position) (instance adhoc_communication::MmRobotPosition :init))
    )
   (send-super :init)
   (setq _dst_robot (string __dst_robot))
   (setq _topic (string __topic))
   (setq _position __position)
   self)
  (:dst_robot
   (&optional __dst_robot)
   (if __dst_robot (setq _dst_robot __dst_robot)) _dst_robot)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
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
    ;; string _dst_robot
    4 (length _dst_robot)
    ;; string _topic
    4 (length _topic)
    ;; adhoc_communication/MmRobotPosition _position
    (send _position :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _dst_robot
       (write-long (length _dst_robot) s) (princ _dst_robot s)
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; adhoc_communication/MmRobotPosition _position
       (send _position :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _dst_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _dst_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; adhoc_communication/MmRobotPosition _position
     (send _position :deserialize buf ptr-) (incf ptr- (send _position :serialization-length))
   ;;
   self)
  )

(defclass adhoc_communication::SendMmRobotPositionResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::SendMmRobotPositionResponse
  (:init
   (&key
    ((:status __status) 0)
    )
   (send-super :init)
   (setq _status (round __status))
   self)
  (:status
   (&optional __status)
   (if __status (setq _status __status)) _status)
  (:serialization-length
   ()
   (+
    ;; uint8 _status
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _status
       (write-byte _status s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _status
     (setq _status (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(defclass adhoc_communication::SendMmRobotPosition
  :super ros::object
  :slots ())

(setf (get adhoc_communication::SendMmRobotPosition :md5sum-) "d6970ad1ec4273f24a69ae2e81f45361")
(setf (get adhoc_communication::SendMmRobotPosition :datatype-) "adhoc_communication/SendMmRobotPosition")
(setf (get adhoc_communication::SendMmRobotPosition :request) adhoc_communication::SendMmRobotPositionRequest)
(setf (get adhoc_communication::SendMmRobotPosition :response) adhoc_communication::SendMmRobotPositionResponse)

(defmethod adhoc_communication::SendMmRobotPositionRequest
  (:response () (instance adhoc_communication::SendMmRobotPositionResponse :init)))

(setf (get adhoc_communication::SendMmRobotPositionRequest :md5sum-) "d6970ad1ec4273f24a69ae2e81f45361")
(setf (get adhoc_communication::SendMmRobotPositionRequest :datatype-) "adhoc_communication/SendMmRobotPositionRequest")
(setf (get adhoc_communication::SendMmRobotPositionRequest :definition-)
      "string dst_robot
string topic
adhoc_communication/MmRobotPosition position

================================================================================
MSG: adhoc_communication/MmRobotPosition
string src_robot
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
---
uint8 status

")

(setf (get adhoc_communication::SendMmRobotPositionResponse :md5sum-) "d6970ad1ec4273f24a69ae2e81f45361")
(setf (get adhoc_communication::SendMmRobotPositionResponse :datatype-) "adhoc_communication/SendMmRobotPositionResponse")
(setf (get adhoc_communication::SendMmRobotPositionResponse :definition-)
      "string dst_robot
string topic
adhoc_communication/MmRobotPosition position

================================================================================
MSG: adhoc_communication/MmRobotPosition
string src_robot
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
---
uint8 status

")



(provide :adhoc_communication/SendMmRobotPosition "d6970ad1ec4273f24a69ae2e81f45361")


