; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude SendMmRobotPosition-request.msg.html

(cl:defclass <SendMmRobotPosition-request> (roslisp-msg-protocol:ros-message)
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
   (position
    :reader position
    :initarg :position
    :type adhoc_communication-msg:MmRobotPosition
    :initform (cl:make-instance 'adhoc_communication-msg:MmRobotPosition)))
)

(cl:defclass SendMmRobotPosition-request (<SendMmRobotPosition-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendMmRobotPosition-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendMmRobotPosition-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendMmRobotPosition-request> is deprecated: use adhoc_communication-srv:SendMmRobotPosition-request instead.")))

(cl:ensure-generic-function 'dst_robot-val :lambda-list '(m))
(cl:defmethod dst_robot-val ((m <SendMmRobotPosition-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:dst_robot-val is deprecated.  Use adhoc_communication-srv:dst_robot instead.")
  (dst_robot m))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <SendMmRobotPosition-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:topic-val is deprecated.  Use adhoc_communication-srv:topic instead.")
  (topic m))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <SendMmRobotPosition-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:position-val is deprecated.  Use adhoc_communication-srv:position instead.")
  (position m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendMmRobotPosition-request>) ostream)
  "Serializes a message object of type '<SendMmRobotPosition-request>"
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
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'position) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendMmRobotPosition-request>) istream)
  "Deserializes a message object of type '<SendMmRobotPosition-request>"
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
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'position) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendMmRobotPosition-request>)))
  "Returns string type for a service object of type '<SendMmRobotPosition-request>"
  "adhoc_communication/SendMmRobotPositionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendMmRobotPosition-request)))
  "Returns string type for a service object of type 'SendMmRobotPosition-request"
  "adhoc_communication/SendMmRobotPositionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendMmRobotPosition-request>)))
  "Returns md5sum for a message object of type '<SendMmRobotPosition-request>"
  "d6970ad1ec4273f24a69ae2e81f45361")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendMmRobotPosition-request)))
  "Returns md5sum for a message object of type 'SendMmRobotPosition-request"
  "d6970ad1ec4273f24a69ae2e81f45361")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendMmRobotPosition-request>)))
  "Returns full string definition for message of type '<SendMmRobotPosition-request>"
  (cl:format cl:nil "string dst_robot~%string topic~%adhoc_communication/MmRobotPosition position~%~%================================================================================~%MSG: adhoc_communication/MmRobotPosition~%string src_robot~%geometry_msgs/PoseStamped position~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendMmRobotPosition-request)))
  "Returns full string definition for message of type 'SendMmRobotPosition-request"
  (cl:format cl:nil "string dst_robot~%string topic~%adhoc_communication/MmRobotPosition position~%~%================================================================================~%MSG: adhoc_communication/MmRobotPosition~%string src_robot~%geometry_msgs/PoseStamped position~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendMmRobotPosition-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'dst_robot))
     4 (cl:length (cl:slot-value msg 'topic))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'position))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendMmRobotPosition-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SendMmRobotPosition-request
    (cl:cons ':dst_robot (dst_robot msg))
    (cl:cons ':topic (topic msg))
    (cl:cons ':position (position msg))
))
;//! \htmlinclude SendMmRobotPosition-response.msg.html

(cl:defclass <SendMmRobotPosition-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SendMmRobotPosition-response (<SendMmRobotPosition-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendMmRobotPosition-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendMmRobotPosition-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendMmRobotPosition-response> is deprecated: use adhoc_communication-srv:SendMmRobotPosition-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <SendMmRobotPosition-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:status-val is deprecated.  Use adhoc_communication-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendMmRobotPosition-response>) ostream)
  "Serializes a message object of type '<SendMmRobotPosition-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendMmRobotPosition-response>) istream)
  "Deserializes a message object of type '<SendMmRobotPosition-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendMmRobotPosition-response>)))
  "Returns string type for a service object of type '<SendMmRobotPosition-response>"
  "adhoc_communication/SendMmRobotPositionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendMmRobotPosition-response)))
  "Returns string type for a service object of type 'SendMmRobotPosition-response"
  "adhoc_communication/SendMmRobotPositionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendMmRobotPosition-response>)))
  "Returns md5sum for a message object of type '<SendMmRobotPosition-response>"
  "d6970ad1ec4273f24a69ae2e81f45361")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendMmRobotPosition-response)))
  "Returns md5sum for a message object of type 'SendMmRobotPosition-response"
  "d6970ad1ec4273f24a69ae2e81f45361")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendMmRobotPosition-response>)))
  "Returns full string definition for message of type '<SendMmRobotPosition-response>"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendMmRobotPosition-response)))
  "Returns full string definition for message of type 'SendMmRobotPosition-response"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendMmRobotPosition-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendMmRobotPosition-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SendMmRobotPosition-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SendMmRobotPosition)))
  'SendMmRobotPosition-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SendMmRobotPosition)))
  'SendMmRobotPosition-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendMmRobotPosition)))
  "Returns string type for a service object of type '<SendMmRobotPosition>"
  "adhoc_communication/SendMmRobotPosition")