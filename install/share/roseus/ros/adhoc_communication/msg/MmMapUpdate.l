;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::MmMapUpdate)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'MmMapUpdate (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::MMMAPUPDATE")
  (make-package "ADHOC_COMMUNICATION::MMMAPUPDATE"))

(in-package "ROS")
;;//! \htmlinclude MmMapUpdate.msg.html
(if (not (find-package "NAV_MSGS"))
  (ros::roseus-add-msgs "nav_msgs"))


(defclass adhoc_communication::MmMapUpdate
  :super ros::object
  :slots (_src_robot _update_numbers _map ))

(defmethod adhoc_communication::MmMapUpdate
  (:init
   (&key
    ((:src_robot __src_robot) "")
    ((:update_numbers __update_numbers) (make-array 0 :initial-element 0 :element-type :integer))
    ((:map __map) (instance nav_msgs::OccupancyGrid :init))
    )
   (send-super :init)
   (setq _src_robot (string __src_robot))
   (setq _update_numbers __update_numbers)
   (setq _map __map)
   self)
  (:src_robot
   (&optional __src_robot)
   (if __src_robot (setq _src_robot __src_robot)) _src_robot)
  (:update_numbers
   (&optional __update_numbers)
   (if __update_numbers (setq _update_numbers __update_numbers)) _update_numbers)
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
    ;; string _src_robot
    4 (length _src_robot)
    ;; int32[] _update_numbers
    (* 4    (length _update_numbers)) 4
    ;; nav_msgs/OccupancyGrid _map
    (send _map :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _src_robot
       (write-long (length _src_robot) s) (princ _src_robot s)
     ;; int32[] _update_numbers
     (write-long (length _update_numbers) s)
     (dotimes (i (length _update_numbers))
       (write-long (elt _update_numbers i) s)
       )
     ;; nav_msgs/OccupancyGrid _map
       (send _map :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _src_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _src_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int32[] _update_numbers
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _update_numbers (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _update_numbers i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; nav_msgs/OccupancyGrid _map
     (send _map :deserialize buf ptr-) (incf ptr- (send _map :serialization-length))
   ;;
   self)
  )

(setf (get adhoc_communication::MmMapUpdate :md5sum-) "cf3b81cd59c0d2ac72a16d2e10428027")
(setf (get adhoc_communication::MmMapUpdate :datatype-) "adhoc_communication/MmMapUpdate")
(setf (get adhoc_communication::MmMapUpdate :definition-)
      "string src_robot
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

")



(provide :adhoc_communication/MmMapUpdate "cf3b81cd59c0d2ac72a16d2e10428027")


