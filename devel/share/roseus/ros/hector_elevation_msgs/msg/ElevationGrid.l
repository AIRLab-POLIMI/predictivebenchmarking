;; Auto-generated. Do not edit!


(when (boundp 'hector_elevation_msgs::ElevationGrid)
  (if (not (find-package "HECTOR_ELEVATION_MSGS"))
    (make-package "HECTOR_ELEVATION_MSGS"))
  (shadow 'ElevationGrid (find-package "HECTOR_ELEVATION_MSGS")))
(unless (find-package "HECTOR_ELEVATION_MSGS::ELEVATIONGRID")
  (make-package "HECTOR_ELEVATION_MSGS::ELEVATIONGRID"))

(in-package "ROS")
;;//! \htmlinclude ElevationGrid.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass hector_elevation_msgs::ElevationGrid
  :super ros::object
  :slots (_header _info _data ))

(defmethod hector_elevation_msgs::ElevationGrid
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:info __info) (instance hector_elevation_msgs::ElevationMapMetaData :init))
    ((:data __data) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _header __header)
   (setq _info __info)
   (setq _data __data)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:info
   (&rest __info)
   (if (keywordp (car __info))
       (send* _info __info)
     (progn
       (if __info (setq _info (car __info)))
       _info)))
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; hector_elevation_msgs/ElevationMapMetaData _info
    (send _info :serialization-length)
    ;; int16[] _data
    (* 2    (length _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; hector_elevation_msgs/ElevationMapMetaData _info
       (send _info :serialize s)
     ;; int16[] _data
     (write-long (length _data) s)
     (dotimes (i (length _data))
       (write-word (elt _data i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; hector_elevation_msgs/ElevationMapMetaData _info
     (send _info :deserialize buf ptr-) (incf ptr- (send _info :serialization-length))
   ;; int16[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _data i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     ))
   ;;
   self)
  )

(setf (get hector_elevation_msgs::ElevationGrid :md5sum-) "13f6dd2a4434f89ebecd8bfafa38cdf1")
(setf (get hector_elevation_msgs::ElevationGrid :datatype-) "hector_elevation_msgs/ElevationGrid")
(setf (get hector_elevation_msgs::ElevationGrid :definition-)
      "# This represents a 2-D grid map, in which each cell represents the elevation.

Header header 

#MetaData for the map
ElevationMapMetaData info

# The map data, in row-major order, starting with (0,0).  Elevation values 
# are in the range [0,32768].
# -> 0 belongs to max negative elevation, 32767 to max positive elevation, \"elevation_zero_level\" coresponds to zero, -elevation_zero_level to unknown elevation
int16[] data

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
MSG: hector_elevation_msgs/ElevationMapMetaData
# This hold basic information about the characterists of the EvaluationGrid

# The time at which the map was loaded
time map_load_time
# Map resolution in xy plane [m/cell]
float64 resolution_xy
# Map resolution in height [m/cell]
float64 resolution_z
# min observed height [m]
float64 min_elevation
# max observed height [m]
float64 max_elevation
# Height zero value. For example 16384.
int16 zero_elevation
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



(provide :hector_elevation_msgs/ElevationGrid "13f6dd2a4434f89ebecd8bfafa38cdf1")


