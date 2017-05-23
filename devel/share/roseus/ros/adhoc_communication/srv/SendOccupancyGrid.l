;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::SendOccupancyGrid)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'SendOccupancyGrid (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::SENDOCCUPANCYGRID")
  (make-package "ADHOC_COMMUNICATION::SENDOCCUPANCYGRID"))
(unless (find-package "ADHOC_COMMUNICATION::SENDOCCUPANCYGRIDREQUEST")
  (make-package "ADHOC_COMMUNICATION::SENDOCCUPANCYGRIDREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::SENDOCCUPANCYGRIDRESPONSE")
  (make-package "ADHOC_COMMUNICATION::SENDOCCUPANCYGRIDRESPONSE"))

(in-package "ROS")

(if (not (find-package "NAV_MSGS"))
  (ros::roseus-add-msgs "nav_msgs"))




(defclass adhoc_communication::SendOccupancyGridRequest
  :super ros::object
  :slots (_dst_robot _topic _map ))

(defmethod adhoc_communication::SendOccupancyGridRequest
  (:init
   (&key
    ((:dst_robot __dst_robot) "")
    ((:topic __topic) "")
    ((:map __map) (instance nav_msgs::OccupancyGrid :init))
    )
   (send-super :init)
   (setq _dst_robot (string __dst_robot))
   (setq _topic (string __topic))
   (setq _map __map)
   self)
  (:dst_robot
   (&optional __dst_robot)
   (if __dst_robot (setq _dst_robot __dst_robot)) _dst_robot)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
  (:map
   (&rest __map)
   (if (keywordp (car __map))
       (send* _map __map)
     (progn
       (if __map (setq _map (car __map)))
       _map)))
  (:serialization-length
   ()
   (+
    ;; string _dst_robot
    4 (length _dst_robot)
    ;; string _topic
    4 (length _topic)
    ;; nav_msgs/OccupancyGrid _map
    (send _map :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _dst_robot
       (write-long (length _dst_robot) s) (princ _dst_robot s)
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; nav_msgs/OccupancyGrid _map
       (send _map :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _dst_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _dst_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; nav_msgs/OccupancyGrid _map
     (send _map :deserialize buf ptr-) (incf ptr- (send _map :serialization-length))
   ;;
   self)
  )

(defclass adhoc_communication::SendOccupancyGridResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::SendOccupancyGridResponse
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

(defclass adhoc_communication::SendOccupancyGrid
  :super ros::object
  :slots ())

(setf (get adhoc_communication::SendOccupancyGrid :md5sum-) "329d068b4117dbc7b058174b97e17df8")
(setf (get adhoc_communication::SendOccupancyGrid :datatype-) "adhoc_communication/SendOccupancyGrid")
(setf (get adhoc_communication::SendOccupancyGrid :request) adhoc_communication::SendOccupancyGridRequest)
(setf (get adhoc_communication::SendOccupancyGrid :response) adhoc_communication::SendOccupancyGridResponse)

(defmethod adhoc_communication::SendOccupancyGridRequest
  (:response () (instance adhoc_communication::SendOccupancyGridResponse :init)))

(setf (get adhoc_communication::SendOccupancyGridRequest :md5sum-) "329d068b4117dbc7b058174b97e17df8")
(setf (get adhoc_communication::SendOccupancyGridRequest :datatype-) "adhoc_communication/SendOccupancyGridRequest")
(setf (get adhoc_communication::SendOccupancyGridRequest :definition-)
      "string dst_robot
string topic
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

(setf (get adhoc_communication::SendOccupancyGridResponse :md5sum-) "329d068b4117dbc7b058174b97e17df8")
(setf (get adhoc_communication::SendOccupancyGridResponse :datatype-) "adhoc_communication/SendOccupancyGridResponse")
(setf (get adhoc_communication::SendOccupancyGridResponse :definition-)
      "string dst_robot
string topic
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



(provide :adhoc_communication/SendOccupancyGrid "329d068b4117dbc7b058174b97e17df8")


