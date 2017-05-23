; Auto-generated. Do not edit!


(cl:in-package fake_network-srv)


;//! \htmlinclude RobotPosition-request.msg.html

(cl:defclass <RobotPosition-request> (roslisp-msg-protocol:ros-message)
  ((s
    :reader s
    :initarg :s
    :type cl:string
    :initform ""))
)

(cl:defclass RobotPosition-request (<RobotPosition-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RobotPosition-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RobotPosition-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name fake_network-srv:<RobotPosition-request> is deprecated: use fake_network-srv:RobotPosition-request instead.")))

(cl:ensure-generic-function 's-val :lambda-list '(m))
(cl:defmethod s-val ((m <RobotPosition-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fake_network-srv:s-val is deprecated.  Use fake_network-srv:s instead.")
  (s m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RobotPosition-request>) ostream)
  "Serializes a message object of type '<RobotPosition-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 's))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 's))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RobotPosition-request>) istream)
  "Deserializes a message object of type '<RobotPosition-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 's) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 's) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RobotPosition-request>)))
  "Returns string type for a service object of type '<RobotPosition-request>"
  "fake_network/RobotPositionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RobotPosition-request)))
  "Returns string type for a service object of type 'RobotPosition-request"
  "fake_network/RobotPositionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RobotPosition-request>)))
  "Returns md5sum for a message object of type '<RobotPosition-request>"
  "23c69c8103af21e37240b074f5348b77")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RobotPosition-request)))
  "Returns md5sum for a message object of type 'RobotPosition-request"
  "23c69c8103af21e37240b074f5348b77")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RobotPosition-request>)))
  "Returns full string definition for message of type '<RobotPosition-request>"
  (cl:format cl:nil "string s~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RobotPosition-request)))
  "Returns full string definition for message of type 'RobotPosition-request"
  (cl:format cl:nil "string s~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RobotPosition-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 's))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RobotPosition-request>))
  "Converts a ROS message object to a list"
  (cl:list 'RobotPosition-request
    (cl:cons ':s (s msg))
))
;//! \htmlinclude RobotPosition-response.msg.html

(cl:defclass <RobotPosition-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0)
   (x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0))
)

(cl:defclass RobotPosition-response (<RobotPosition-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RobotPosition-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RobotPosition-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name fake_network-srv:<RobotPosition-response> is deprecated: use fake_network-srv:RobotPosition-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <RobotPosition-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fake_network-srv:status-val is deprecated.  Use fake_network-srv:status instead.")
  (status m))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <RobotPosition-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fake_network-srv:x-val is deprecated.  Use fake_network-srv:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <RobotPosition-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fake_network-srv:y-val is deprecated.  Use fake_network-srv:y instead.")
  (y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RobotPosition-response>) ostream)
  "Serializes a message object of type '<RobotPosition-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RobotPosition-response>) istream)
  "Deserializes a message object of type '<RobotPosition-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RobotPosition-response>)))
  "Returns string type for a service object of type '<RobotPosition-response>"
  "fake_network/RobotPositionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RobotPosition-response)))
  "Returns string type for a service object of type 'RobotPosition-response"
  "fake_network/RobotPositionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RobotPosition-response>)))
  "Returns md5sum for a message object of type '<RobotPosition-response>"
  "23c69c8103af21e37240b074f5348b77")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RobotPosition-response)))
  "Returns md5sum for a message object of type 'RobotPosition-response"
  "23c69c8103af21e37240b074f5348b77")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RobotPosition-response>)))
  "Returns full string definition for message of type '<RobotPosition-response>"
  (cl:format cl:nil "uint8 status~%float32 x~%float32 y~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RobotPosition-response)))
  "Returns full string definition for message of type 'RobotPosition-response"
  (cl:format cl:nil "uint8 status~%float32 x~%float32 y~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RobotPosition-response>))
  (cl:+ 0
     1
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RobotPosition-response>))
  "Converts a ROS message object to a list"
  (cl:list 'RobotPosition-response
    (cl:cons ':status (status msg))
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'RobotPosition)))
  'RobotPosition-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'RobotPosition)))
  'RobotPosition-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RobotPosition)))
  "Returns string type for a service object of type '<RobotPosition>"
  "fake_network/RobotPosition")