; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude SendMmMapUpdate-request.msg.html

(cl:defclass <SendMmMapUpdate-request> (roslisp-msg-protocol:ros-message)
  ((dst_robot
    :reader dst_robot
    :initarg :dst_robot
    :type cl:string
    :initform "")
   (topic
    :reader topic
    :initarg :topic
    :type cl:string
    :initform "")
   (map_update
    :reader map_update
    :initarg :map_update
    :type adhoc_communication-msg:MmMapUpdate
    :initform (cl:make-instance 'adhoc_communication-msg:MmMapUpdate)))
)

(cl:defclass SendMmMapUpdate-request (<SendMmMapUpdate-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendMmMapUpdate-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendMmMapUpdate-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendMmMapUpdate-request> is deprecated: use adhoc_communication-srv:SendMmMapUpdate-request instead.")))

(cl:ensure-generic-function 'dst_robot-val :lambda-list '(m))
(cl:defmethod dst_robot-val ((m <SendMmMapUpdate-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:dst_robot-val is deprecated.  Use adhoc_communication-srv:dst_robot instead.")
  (dst_robot m))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <SendMmMapUpdate-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:topic-val is deprecated.  Use adhoc_communication-srv:topic instead.")
  (topic m))

(cl:ensure-generic-function 'map_update-val :lambda-list '(m))
(cl:defmethod map_update-val ((m <SendMmMapUpdate-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:map_update-val is deprecated.  Use adhoc_communication-srv:map_update instead.")
  (map_update m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendMmMapUpdate-request>) ostream)
  "Serializes a message object of type '<SendMmMapUpdate-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'dst_robot))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'dst_robot))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'topic))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'topic))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'map_update) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendMmMapUpdate-request>) istream)
  "Deserializes a message object of type '<SendMmMapUpdate-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'dst_robot) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'dst_robot) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'topic) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'topic) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'map_update) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendMmMapUpdate-request>)))
  "Returns string type for a service object of type '<SendMmMapUpdate-request>"
  "adhoc_communication/SendMmMapUpdateRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendMmMapUpdate-request)))
  "Returns string type for a service object of type 'SendMmMapUpdate-request"
  "adhoc_communication/SendMmMapUpdateRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendMmMapUpdate-request>)))
  "Returns md5sum for a message object of type '<SendMmMapUpdate-request>"
  "6887084fcfdf3574f5698c6a4c7aeeb6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendMmMapUpdate-request)))
  "Returns md5sum for a message object of type 'SendMmMapUpdate-request"
  "6887084fcfdf3574f5698c6a4c7aeeb6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendMmMapUpdate-request>)))
  "Returns full string definition for message of type '<SendMmMapUpdate-request>"
  (cl:format cl:nil "string dst_robot~%string topic~%adhoc_communication/MmMapUpdate map_update~%~%================================================================================~%MSG: adhoc_communication/MmMapUpdate~%string src_robot~%int32[] update_numbers~%nav_msgs/OccupancyGrid map~%~%================================================================================~%MSG: nav_msgs/OccupancyGrid~%# This represents a 2-D grid map, in which each cell represents the probability of~%# occupancy.~%~%Header header ~%~%#MetaData for the map~%MapMetaData info~%~%# The map data, in row-major order, starting with (0,0).  Occupancy~%# probabilities are in the range [0,100].  Unknown is -1.~%int8[] data~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: nav_msgs/MapMetaData~%# This hold basic information about the characterists of the OccupancyGrid~%~%# The time at which the map was loaded~%time map_load_time~%# The map resolution [m/cell]~%float32 resolution~%# Map width [cells]~%uint32 width~%# Map height [cells]~%uint32 height~%# The origin of the map [m, m, rad].  This is the real-world pose of the~%# cell (0,0) in the map.~%geometry_msgs/Pose origin~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendMmMapUpdate-request)))
  "Returns full string definition for message of type 'SendMmMapUpdate-request"
  (cl:format cl:nil "string dst_robot~%string topic~%adhoc_communication/MmMapUpdate map_update~%~%================================================================================~%MSG: adhoc_communication/MmMapUpdate~%string src_robot~%int32[] update_numbers~%nav_msgs/OccupancyGrid map~%~%================================================================================~%MSG: nav_msgs/OccupancyGrid~%# This represents a 2-D grid map, in which each cell represents the probability of~%# occupancy.~%~%Header header ~%~%#MetaData for the map~%MapMetaData info~%~%# The map data, in row-major order, starting with (0,0).  Occupancy~%# probabilities are in the range [0,100].  Unknown is -1.~%int8[] data~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: nav_msgs/MapMetaData~%# This hold basic information about the characterists of the OccupancyGrid~%~%# The time at which the map was loaded~%time map_load_time~%# The map resolution [m/cell]~%float32 resolution~%# Map width [cells]~%uint32 width~%# Map height [cells]~%uint32 height~%# The origin of the map [m, m, rad].  This is the real-world pose of the~%# cell (0,0) in the map.~%geometry_msgs/Pose origin~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendMmMapUpdate-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'dst_robot))
     4 (cl:length (cl:slot-value msg 'topic))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'map_update))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendMmMapUpdate-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SendMmMapUpdate-request
    (cl:cons ':dst_robot (dst_robot msg))
    (cl:cons ':topic (topic msg))
    (cl:cons ':map_update (map_update msg))
))
;//! \htmlinclude SendMmMapUpdate-response.msg.html

(cl:defclass <SendMmMapUpdate-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SendMmMapUpdate-response (<SendMmMapUpdate-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendMmMapUpdate-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendMmMapUpdate-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendMmMapUpdate-response> is deprecated: use adhoc_communication-srv:SendMmMapUpdate-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <SendMmMapUpdate-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:status-val is deprecated.  Use adhoc_communication-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendMmMapUpdate-response>) ostream)
  "Serializes a message object of type '<SendMmMapUpdate-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendMmMapUpdate-response>) istream)
  "Deserializes a message object of type '<SendMmMapUpdate-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendMmMapUpdate-response>)))
  "Returns string type for a service object of type '<SendMmMapUpdate-response>"
  "adhoc_communication/SendMmMapUpdateResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendMmMapUpdate-response)))
  "Returns string type for a service object of type 'SendMmMapUpdate-response"
  "adhoc_communication/SendMmMapUpdateResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendMmMapUpdate-response>)))
  "Returns md5sum for a message object of type '<SendMmMapUpdate-response>"
  "6887084fcfdf3574f5698c6a4c7aeeb6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendMmMapUpdate-response)))
  "Returns md5sum for a message object of type 'SendMmMapUpdate-response"
  "6887084fcfdf3574f5698c6a4c7aeeb6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendMmMapUpdate-response>)))
  "Returns full string definition for message of type '<SendMmMapUpdate-response>"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendMmMapUpdate-response)))
  "Returns full string definition for message of type 'SendMmMapUpdate-response"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendMmMapUpdate-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendMmMapUpdate-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SendMmMapUpdate-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SendMmMapUpdate)))
  'SendMmMapUpdate-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SendMmMapUpdate)))
  'SendMmMapUpdate-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendMmMapUpdate)))
  "Returns string type for a service object of type '<SendMmMapUpdate>"
  "adhoc_communication/SendMmMapUpdate")