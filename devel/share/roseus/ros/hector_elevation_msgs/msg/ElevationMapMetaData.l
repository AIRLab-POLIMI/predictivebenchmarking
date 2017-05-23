;; Auto-generated. Do not edit!


(when (boundp 'hector_elevation_msgs::ElevationMapMetaData)
  (if (not (find-package "HECTOR_ELEVATION_MSGS"))
    (make-package "HECTOR_ELEVATION_MSGS"))
  (shadow 'ElevationMapMetaData (find-package "HECTOR_ELEVATION_MSGS")))
(unless (find-package "HECTOR_ELEVATION_MSGS::ELEVATIONMAPMETADATA")
  (make-package "HECTOR_ELEVATION_MSGS::ELEVATIONMAPMETADATA"))

(in-package "ROS")
;;//! \htmlinclude ElevationMapMetaData.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass hector_elevation_msgs::ElevationMapMetaData
  :super ros::object
  :slots (_map_load_time _resolution_xy _resolution_z _min_elevation _max_elevation _zero_elevation _width _height _origin ))

(defmethod hector_elevation_msgs::ElevationMapMetaData
  (:init
   (&key
    ((:map_load_time __map_load_time) (instance ros::time :init))
    ((:resolution_xy __resolution_xy) 0.0)
    ((:resolution_z __resolution_z) 0.0)
    ((:min_elevation __min_elevation) 0.0)
    ((:max_elevation __max_elevation) 0.0)
    ((:zero_elevation __zero_elevation) 0)
    ((:width __width) 0)
    ((:height __height) 0)
    ((:origin __origin) (instance geometry_msgs::Pose :init))
    )
   (send-super :init)
   (setq _map_load_time __map_load_time)
   (setq _resolution_xy (float __resolution_xy))
   (setq _resolution_z (float __resolution_z))
   (setq _min_elevation (float __min_elevation))
   (setq _max_elevation (float __max_elevation))
   (setq _zero_elevation (round __zero_elevation))
   (setq _width (round __width))
   (setq _height (round __height))
   (setq _origin __origin)
   self)
  (:map_load_time
   (&optional __map_load_time)
   (if __map_load_time (setq _map_load_time __map_load_time)) _map_load_time)
  (:resolution_xy
   (&optional __resolution_xy)
   (if __resolution_xy (setq _resolution_xy __resolution_xy)) _resolution_xy)
  (:resolution_z
   (&optional __resolution_z)
   (if __resolution_z (setq _resolution_z __resolution_z)) _resolution_z)
  (:min_elevation
   (&optional __min_elevation)
   (if __min_elevation (setq _min_elevation __min_elevation)) _min_elevation)
  (:max_elevation
   (&optional __max_elevation)
   (if __max_elevation (setq _max_elevation __max_elevation)) _max_elevation)
  (:zero_elevation
   (&optional __zero_elevation)
   (if __zero_elevation (setq _zero_elevation __zero_elevation)) _zero_elevation)
  (:width
   (&optional __width)
   (if __width (setq _width __width)) _width)
  (:height
   (&optional __height)
   (if __height (setq _height __height)) _height)
  (:origin
   (&rest __origin)
   (if (keywordp (car __origin))
       (send* _origin __origin)
     (progn
       (if __origin (setq _origin (car __origin)))
       _origin)))
  (:serialization-length
   ()
   (+
    ;; time _map_load_time
    8
    ;; float64 _resolution_xy
    8
    ;; float64 _resolution_z
    8
    ;; float64 _min_elevation
    8
    ;; float64 _max_elevation
    8
    ;; int16 _zero_elevation
    2
    ;; uint32 _width
    4
    ;; uint32 _height
    4
    ;; geometry_msgs/Pose _origin
    (send _origin :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; time _map_load_time
       (write-long (send _map_load_time :sec) s) (write-long (send _map_load_time :nsec) s)
     ;; float64 _resolution_xy
       (sys::poke _resolution_xy (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _resolution_z
       (sys::poke _resolution_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _min_elevation
       (sys::poke _min_elevation (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _max_elevation
       (sys::poke _max_elevation (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int16 _zero_elevation
       (write-word _zero_elevation s)
     ;; uint32 _width
       (write-long _width s)
     ;; uint32 _height
       (write-long _height s)
     ;; geometry_msgs/Pose _origin
       (send _origin :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; time _map_load_time
     (send _map_load_time :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _map_load_time :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float64 _resolution_xy
     (setq _resolution_xy (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _resolution_z
     (setq _resolution_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _min_elevation
     (setq _min_elevation (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _max_elevation
     (setq _max_elevation (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int16 _zero_elevation
     (setq _zero_elevation (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint32 _width
     (setq _width (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint32 _height
     (setq _height (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; geometry_msgs/Pose _origin
     (send _origin :deserialize buf ptr-) (incf ptr- (send _origin :serialization-length))
   ;;
   self)
  )

(setf (get hector_elevation_msgs::ElevationMapMetaData :md5sum-) "6c887873faf3a1d55d884bdcc92b9241")
(setf (get hector_elevation_msgs::ElevationMapMetaData :datatype-) "hector_elevation_msgs/ElevationMapMetaData")
(setf (get hector_elevation_msgs::ElevationMapMetaData :definition-)
      "# This hold basic information about the characterists of the EvaluationGrid

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



(provide :hector_elevation_msgs/ElevationMapMetaData "6c887873faf3a1d55d884bdcc92b9241")


