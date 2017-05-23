; Auto-generated. Do not edit!


(cl:in-package hector_elevation_msgs-msg)


;//! \htmlinclude ElevationMapMetaData.msg.html

(cl:defclass <ElevationMapMetaData> (roslisp-msg-protocol:ros-message)
  ((map_load_time
    :reader map_load_time
    :initarg :map_load_time
    :type cl:real
    :initform 0)
   (resolution_xy
    :reader resolution_xy
    :initarg :resolution_xy
    :type cl:float
    :initform 0.0)
   (resolution_z
    :reader resolution_z
    :initarg :resolution_z
    :type cl:float
    :initform 0.0)
   (min_elevation
    :reader min_elevation
    :initarg :min_elevation
    :type cl:float
    :initform 0.0)
   (max_elevation
    :reader max_elevation
    :initarg :max_elevation
    :type cl:float
    :initform 0.0)
   (zero_elevation
    :reader zero_elevation
    :initarg :zero_elevation
    :type cl:fixnum
    :initform 0)
   (width
    :reader width
    :initarg :width
    :type cl:integer
    :initform 0)
   (height
    :reader height
    :initarg :height
    :type cl:integer
    :initform 0)
   (origin
    :reader origin
    :initarg :origin
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose)))
)

(cl:defclass ElevationMapMetaData (<ElevationMapMetaData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ElevationMapMetaData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ElevationMapMetaData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name hector_elevation_msgs-msg:<ElevationMapMetaData> is deprecated: use hector_elevation_msgs-msg:ElevationMapMetaData instead.")))

(cl:ensure-generic-function 'map_load_time-val :lambda-list '(m))
(cl:defmethod map_load_time-val ((m <ElevationMapMetaData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hector_elevation_msgs-msg:map_load_time-val is deprecated.  Use hector_elevation_msgs-msg:map_load_time instead.")
  (map_load_time m))

(cl:ensure-generic-function 'resolution_xy-val :lambda-list '(m))
(cl:defmethod resolution_xy-val ((m <ElevationMapMetaData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hector_elevation_msgs-msg:resolution_xy-val is deprecated.  Use hector_elevation_msgs-msg:resolution_xy instead.")
  (resolution_xy m))

(cl:ensure-generic-function 'resolution_z-val :lambda-list '(m))
(cl:defmethod resolution_z-val ((m <ElevationMapMetaData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hector_elevation_msgs-msg:resolution_z-val is deprecated.  Use hector_elevation_msgs-msg:resolution_z instead.")
  (resolution_z m))

(cl:ensure-generic-function 'min_elevation-val :lambda-list '(m))
(cl:defmethod min_elevation-val ((m <ElevationMapMetaData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hector_elevation_msgs-msg:min_elevation-val is deprecated.  Use hector_elevation_msgs-msg:min_elevation instead.")
  (min_elevation m))

(cl:ensure-generic-function 'max_elevation-val :lambda-list '(m))
(cl:defmethod max_elevation-val ((m <ElevationMapMetaData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hector_elevation_msgs-msg:max_elevation-val is deprecated.  Use hector_elevation_msgs-msg:max_elevation instead.")
  (max_elevation m))

(cl:ensure-generic-function 'zero_elevation-val :lambda-list '(m))
(cl:defmethod zero_elevation-val ((m <ElevationMapMetaData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hector_elevation_msgs-msg:zero_elevation-val is deprecated.  Use hector_elevation_msgs-msg:zero_elevation instead.")
  (zero_elevation m))

(cl:ensure-generic-function 'width-val :lambda-list '(m))
(cl:defmethod width-val ((m <ElevationMapMetaData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hector_elevation_msgs-msg:width-val is deprecated.  Use hector_elevation_msgs-msg:width instead.")
  (width m))

(cl:ensure-generic-function 'height-val :lambda-list '(m))
(cl:defmethod height-val ((m <ElevationMapMetaData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hector_elevation_msgs-msg:height-val is deprecated.  Use hector_elevation_msgs-msg:height instead.")
  (height m))

(cl:ensure-generic-function 'origin-val :lambda-list '(m))
(cl:defmethod origin-val ((m <ElevationMapMetaData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hector_elevation_msgs-msg:origin-val is deprecated.  Use hector_elevation_msgs-msg:origin instead.")
  (origin m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ElevationMapMetaData>) ostream)
  "Serializes a message object of type '<ElevationMapMetaData>"
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'map_load_time)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'map_load_time) (cl:floor (cl:slot-value msg 'map_load_time)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'resolution_xy))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'resolution_z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'min_elevation))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'max_elevation))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'zero_elevation)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'width)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'width)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'width)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'width)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'height)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'height)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'height)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'height)) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'origin) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ElevationMapMetaData>) istream)
  "Deserializes a message object of type '<ElevationMapMetaData>"
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'map_load_time) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'resolution_xy) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'resolution_z) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'min_elevation) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'max_elevation) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'zero_elevation) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'width)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'width)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'width)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'width)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'height)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'height)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'height)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'height)) (cl:read-byte istream))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'origin) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ElevationMapMetaData>)))
  "Returns string type for a message object of type '<ElevationMapMetaData>"
  "hector_elevation_msgs/ElevationMapMetaData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ElevationMapMetaData)))
  "Returns string type for a message object of type 'ElevationMapMetaData"
  "hector_elevation_msgs/ElevationMapMetaData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ElevationMapMetaData>)))
  "Returns md5sum for a message object of type '<ElevationMapMetaData>"
  "6c887873faf3a1d55d884bdcc92b9241")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ElevationMapMetaData)))
  "Returns md5sum for a message object of type 'ElevationMapMetaData"
  "6c887873faf3a1d55d884bdcc92b9241")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ElevationMapMetaData>)))
  "Returns full string definition for message of type '<ElevationMapMetaData>"
  (cl:format cl:nil "# This hold basic information about the characterists of the EvaluationGrid~%~%# The time at which the map was loaded~%time map_load_time~%# Map resolution in xy plane [m/cell]~%float64 resolution_xy~%# Map resolution in height [m/cell]~%float64 resolution_z~%# min observed height [m]~%float64 min_elevation~%# max observed height [m]~%float64 max_elevation~%# Height zero value. For example 16384.~%int16 zero_elevation~%# Map width [cells]~%uint32 width~%# Map height [cells]~%uint32 height~%# The origin of the map [m, m, rad].  This is the real-world pose of the~%# cell (0,0) in the map.~%geometry_msgs/Pose origin~%~%~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ElevationMapMetaData)))
  "Returns full string definition for message of type 'ElevationMapMetaData"
  (cl:format cl:nil "# This hold basic information about the characterists of the EvaluationGrid~%~%# The time at which the map was loaded~%time map_load_time~%# Map resolution in xy plane [m/cell]~%float64 resolution_xy~%# Map resolution in height [m/cell]~%float64 resolution_z~%# min observed height [m]~%float64 min_elevation~%# max observed height [m]~%float64 max_elevation~%# Height zero value. For example 16384.~%int16 zero_elevation~%# Map width [cells]~%uint32 width~%# Map height [cells]~%uint32 height~%# The origin of the map [m, m, rad].  This is the real-world pose of the~%# cell (0,0) in the map.~%geometry_msgs/Pose origin~%~%~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ElevationMapMetaData>))
  (cl:+ 0
     8
     8
     8
     8
     8
     2
     4
     4
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'origin))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ElevationMapMetaData>))
  "Converts a ROS message object to a list"
  (cl:list 'ElevationMapMetaData
    (cl:cons ':map_load_time (map_load_time msg))
    (cl:cons ':resolution_xy (resolution_xy msg))
    (cl:cons ':resolution_z (resolution_z msg))
    (cl:cons ':min_elevation (min_elevation msg))
    (cl:cons ':max_elevation (max_elevation msg))
    (cl:cons ':zero_elevation (zero_elevation msg))
    (cl:cons ':width (width msg))
    (cl:cons ':height (height msg))
    (cl:cons ':origin (origin msg))
))
