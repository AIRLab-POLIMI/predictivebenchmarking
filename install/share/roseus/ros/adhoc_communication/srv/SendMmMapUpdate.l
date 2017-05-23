;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::SendMmMapUpdate)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'SendMmMapUpdate (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::SENDMMMAPUPDATE")
  (make-package "ADHOC_COMMUNICATION::SENDMMMAPUPDATE"))
(unless (find-package "ADHOC_COMMUNICATION::SENDMMMAPUPDATEREQUEST")
  (make-package "ADHOC_COMMUNICATION::SENDMMMAPUPDATEREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::SENDMMMAPUPDATERESPONSE")
  (make-package "ADHOC_COMMUNICATION::SENDMMMAPUPDATERESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::SendMmMapUpdateRequest
  :super ros::object
  :slots (_dst_robot _topic _map_update ))

(defmethod adhoc_communication::SendMmMapUpdateRequest
  (:init
   (&key
    ((:dst_robot __dst_robot) "")
    ((:topic __topic) "")
    ((:map_update __map_update) (instance adhoc_communication::MmMapUpdate :init))
    )
   (send-super :init)
   (setq _dst_robot (string __dst_robot))
   (setq _topic (string __topic))
   (setq _map_update __map_update)
   self)
  (:dst_robot
   (&optional __dst_robot)
   (if __dst_robot (setq _dst_robot __dst_robot)) _dst_robot)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
  (:map_update
   (&rest __map_update)
   (if (keywordp (car __map_update))
       (send* _map_update __map_update)
     (progn
       (if __map_update (setq _map_update (car __map_update)))
       _map_update)))
  (:serialization-length
   ()
   (+
    ;; string _dst_robot
    4 (length _dst_robot)
    ;; string _topic
    4 (length _topic)
    ;; adhoc_communication/MmMapUpdate _map_update
    (send _map_update :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _dst_robot
       (write-long (length _dst_robot) s) (princ _dst_robot s)
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; adhoc_communication/MmMapUpdate _map_update
       (send _map_update :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _dst_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _dst_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; adhoc_communication/MmMapUpdate _map_update
     (send _map_update :deserialize buf ptr-) (incf ptr- (send _map_update :serialization-length))
   ;;
   self)
  )

(defclass adhoc_communication::SendMmMapUpdateResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::SendMmMapUpdateResponse
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

(defclass adhoc_communication::SendMmMapUpdate
  :super ros::object
  :slots ())

(setf (get adhoc_communication::SendMmMapUpdate :md5sum-) "6887084fcfdf3574f5698c6a4c7aeeb6")
(setf (get adhoc_communication::SendMmMapUpdate :datatype-) "adhoc_communication/SendMmMapUpdate")
(setf (get adhoc_communication::SendMmMapUpdate :request) adhoc_communication::SendMmMapUpdateRequest)
(setf (get adhoc_communication::SendMmMapUpdate :response) adhoc_communication::SendMmMapUpdateResponse)

(defmethod adhoc_communication::SendMmMapUpdateRequest
  (:response () (instance adhoc_communication::SendMmMapUpdateResponse :init)))

(setf (get adhoc_communication::SendMmMapUpdateRequest :md5sum-) "6887084fcfdf3574f5698c6a4c7aeeb6")
(setf (get adhoc_communication::SendMmMapUpdateRequest :datatype-) "adhoc_communication/SendMmMapUpdateRequest")
(setf (get adhoc_communication::SendMmMapUpdateRequest :definition-)
      "string dst_robot
string topic
adhoc_communication/MmMapUpdate map_update

================================================================================
MSG: adhoc_communication/MmMapUpdate
string src_robot
int32[] update_numbers
nav_msgs/OccupancyGrid map

================================================================================
MSG: nav_msgs/OccupancyGrid
# This represents a 2-D grid map, in which each cell represents the probability of
# occupancy.

Header header 

#MetaData for the map
MapMetaData info

# The map data, in row-major order, starting with (0,0).  Occupancy
# probabilities are in the range [0,100].  Unknown is -1.
int8[] data

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
MSG: nav_msgs/MapMetaData
# This hold basic information about the characterists of the OccupancyGrid

# The time at which the map was loaded
time map_load_time
# The map resolution [m/cell]
float32 resolution
# Map width [cells]
uint32 width
# Map height [cells]
uint32 height
# The origin of the map [m, m, rad].  This is the real-world pose of the
# cell (0,0) in the map.
geometry_msgs/Pose origin
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

(setf (get adhoc_communication::SendMmMapUpdateResponse :md5sum-) "6887084fcfdf3574f5698c6a4c7aeeb6")
(setf (get adhoc_communication::SendMmMapUpdateResponse :datatype-) "adhoc_communication/SendMmMapUpdateResponse")
(setf (get adhoc_communication::SendMmMapUpdateResponse :definition-)
      "string dst_robot
string topic
adhoc_communication/MmMapUpdate map_update

================================================================================
MSG: adhoc_communication/MmMapUpdate
string src_robot
int32[] update_numbers
nav_msgs/OccupancyGrid map

================================================================================
MSG: nav_msgs/OccupancyGrid
# This represents a 2-D grid map, in which each cell represents the probability of
# occupancy.

Header header 

#MetaData for the map
MapMetaData info

# The map data, in row-major order, starting with (0,0).  Occupancy
# probabilities are in the range [0,100].  Unknown is -1.
int8[] data

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
MSG: nav_msgs/MapMetaData
# This hold basic information about the characterists of the OccupancyGrid

# The time at which the map was loaded
time map_load_time
# The map resolution [m/cell]
float32 resolution
# Map width [cells]
uint32 width
# Map height [cells]
uint32 height
# The origin of the map [m, m, rad].  This is the real-world pose of the
# cell (0,0) in the map.
geometry_msgs/Pose origin
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



(provide :adhoc_communication/SendMmMapUpdate "6887084fcfdf3574f5698c6a4c7aeeb6")


