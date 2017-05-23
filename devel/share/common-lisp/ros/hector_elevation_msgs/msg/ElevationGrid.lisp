; Auto-generated. Do not edit!


(cl:in-package hector_elevation_msgs-msg)


;//! \htmlinclude ElevationGrid.msg.html

(cl:defclass <ElevationGrid> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (info
    :reader info
    :initarg :info
    :type hector_elevation_msgs-msg:ElevationMapMetaData
    :initform (cl:make-instance 'hector_elevation_msgs-msg:ElevationMapMetaData))
   (data
    :reader data
    :initarg :data
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass ElevationGrid (<ElevationGrid>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ElevationGrid>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ElevationGrid)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name hector_elevation_msgs-msg:<ElevationGrid> is deprecated: use hector_elevation_msgs-msg:ElevationGrid instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ElevationGrid>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hector_elevation_msgs-msg:header-val is deprecated.  Use hector_elevation_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'info-val :lambda-list '(m))
(cl:defmethod info-val ((m <ElevationGrid>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hector_elevation_msgs-msg:info-val is deprecated.  Use hector_elevation_msgs-msg:info instead.")
  (info m))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <ElevationGrid>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hector_elevation_msgs-msg:data-val is deprecated.  Use hector_elevation_msgs-msg:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ElevationGrid>) ostream)
  "Serializes a message object of type '<ElevationGrid>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'info) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ElevationGrid>) istream)
  "Deserializes a message object of type '<ElevationGrid>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'info) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ElevationGrid>)))
  "Returns string type for a message object of type '<ElevationGrid>"
  "hector_elevation_msgs/ElevationGrid")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ElevationGrid)))
  "Returns string type for a message object of type 'ElevationGrid"
  "hector_elevation_msgs/ElevationGrid")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ElevationGrid>)))
  "Returns md5sum for a message object of type '<ElevationGrid>"
  "13f6dd2a4434f89ebecd8bfafa38cdf1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ElevationGrid)))
  "Returns md5sum for a message object of type 'ElevationGrid"
  "13f6dd2a4434f89ebecd8bfafa38cdf1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ElevationGrid>)))
  "Returns full string definition for message of type '<ElevationGrid>"
  (cl:format cl:nil "# This represents a 2-D grid map, in which each cell represents the elevation.~%~%Header header ~%~%#MetaData for the map~%ElevationMapMetaData info~%~%# The map data, in row-major order, starting with (0,0).  Elevation values ~%# are in the range [0,32768].~%# -> 0 belongs to max negative elevation, 32767 to max positive elevation, \"elevation_zero_level\" coresponds to zero, -elevation_zero_level to unknown elevation~%int16[] data~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: hector_elevation_msgs/ElevationMapMetaData~%# This hold basic information about the characterists of the EvaluationGrid~%~%# The time at which the map was loaded~%time map_load_time~%# Map resolution in xy plane [m/cell]~%float64 resolution_xy~%# Map resolution in height [m/cell]~%float64 resolution_z~%# min observed height [m]~%float64 min_elevation~%# max observed height [m]~%float64 max_elevation~%# Height zero value. For example 16384.~%int16 zero_elevation~%# Map width [cells]~%uint32 width~%# Map height [cells]~%uint32 height~%# The origin of the map [m, m, rad].  This is the real-world pose of the~%# cell (0,0) in the map.~%geometry_msgs/Pose origin~%~%~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ElevationGrid)))
  "Returns full string definition for message of type 'ElevationGrid"
  (cl:format cl:nil "# This represents a 2-D grid map, in which each cell represents the elevation.~%~%Header header ~%~%#MetaData for the map~%ElevationMapMetaData info~%~%# The map data, in row-major order, starting with (0,0).  Elevation values ~%# are in the range [0,32768].~%# -> 0 belongs to max negative elevation, 32767 to max positive elevation, \"elevation_zero_level\" coresponds to zero, -elevation_zero_level to unknown elevation~%int16[] data~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: hector_elevation_msgs/ElevationMapMetaData~%# This hold basic information about the characterists of the EvaluationGrid~%~%# The time at which the map was loaded~%time map_load_time~%# Map resolution in xy plane [m/cell]~%float64 resolution_xy~%# Map resolution in height [m/cell]~%float64 resolution_z~%# min observed height [m]~%float64 min_elevation~%# max observed height [m]~%float64 max_elevation~%# Height zero value. For example 16384.~%int16 zero_elevation~%# Map width [cells]~%uint32 width~%# Map height [cells]~%uint32 height~%# The origin of the map [m, m, rad].  This is the real-world pose of the~%# cell (0,0) in the map.~%geometry_msgs/Pose origin~%~%~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ElevationGrid>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'info))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ElevationGrid>))
  "Converts a ROS message object to a list"
  (cl:list 'ElevationGrid
    (cl:cons ':header (header msg))
    (cl:cons ':info (info msg))
    (cl:cons ':data (data msg))
))
