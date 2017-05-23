; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude BroadcastString-request.msg.html

(cl:defclass <BroadcastString-request> (roslisp-msg-protocol:ros-message)
  ((topic
    :reader topic
    :initarg :topic
    :type cl:string
    :initform "")
   (data
    :reader data
    :initarg :data
    :type cl:string
    :initform "")
   (hop_limit
    :reader hop_limit
    :initarg :hop_limit
    :type cl:fixnum
    :initform 0))
)

(cl:defclass BroadcastString-request (<BroadcastString-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BroadcastString-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BroadcastString-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<BroadcastString-request> is deprecated: use adhoc_communication-srv:BroadcastString-request instead.")))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <BroadcastString-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:topic-val is deprecated.  Use adhoc_communication-srv:topic instead.")
  (topic m))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <BroadcastString-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:data-val is deprecated.  Use adhoc_communication-srv:data instead.")
  (data m))

(cl:ensure-generic-function 'hop_limit-val :lambda-list '(m))
(cl:defmethod hop_limit-val ((m <BroadcastString-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:hop_limit-val is deprecated.  Use adhoc_communication-srv:hop_limit instead.")
  (hop_limit m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BroadcastString-request>) ostream)
  "Serializes a message object of type '<BroadcastString-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'topic))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'topic))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'data))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'hop_limit)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BroadcastString-request>) istream)
  "Deserializes a message object of type '<BroadcastString-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'topic) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'topic) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'data) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'data) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'hop_limit)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BroadcastString-request>)))
  "Returns string type for a service object of type '<BroadcastString-request>"
  "adhoc_communication/BroadcastStringRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BroadcastString-request)))
  "Returns string type for a service object of type 'BroadcastString-request"
  "adhoc_communication/BroadcastStringRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BroadcastString-request>)))
  "Returns md5sum for a message object of type '<BroadcastString-request>"
  "79e1c1b930819d5a990dea57200bd10a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BroadcastString-request)))
  "Returns md5sum for a message object of type 'BroadcastString-request"
  "79e1c1b930819d5a990dea57200bd10a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BroadcastString-request>)))
  "Returns full string definition for message of type '<BroadcastString-request>"
  (cl:format cl:nil "string topic~%string data~%uint8 hop_limit~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BroadcastString-request)))
  "Returns full string definition for message of type 'BroadcastString-request"
  (cl:format cl:nil "string topic~%string data~%uint8 hop_limit~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BroadcastString-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'topic))
     4 (cl:length (cl:slot-value msg 'data))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BroadcastString-request>))
  "Converts a ROS message object to a list"
  (cl:list 'BroadcastString-request
    (cl:cons ':topic (topic msg))
    (cl:cons ':data (data msg))
    (cl:cons ':hop_limit (hop_limit msg))
))
;//! \htmlinclude BroadcastString-response.msg.html

(cl:defclass <BroadcastString-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass BroadcastString-response (<BroadcastString-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BroadcastString-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BroadcastString-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<BroadcastString-response> is deprecated: use adhoc_communication-srv:BroadcastString-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <BroadcastString-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:status-val is deprecated.  Use adhoc_communication-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BroadcastString-response>) ostream)
  "Serializes a message object of type '<BroadcastString-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BroadcastString-response>) istream)
  "Deserializes a message object of type '<BroadcastString-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BroadcastString-response>)))
  "Returns string type for a service object of type '<BroadcastString-response>"
  "adhoc_communication/BroadcastStringResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BroadcastString-response)))
  "Returns string type for a service object of type 'BroadcastString-response"
  "adhoc_communication/BroadcastStringResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BroadcastString-response>)))
  "Returns md5sum for a message object of type '<BroadcastString-response>"
  "79e1c1b930819d5a990dea57200bd10a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BroadcastString-response)))
  "Returns md5sum for a message object of type 'BroadcastString-response"
  "79e1c1b930819d5a990dea57200bd10a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BroadcastString-response>)))
  "Returns full string definition for message of type '<BroadcastString-response>"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BroadcastString-response)))
  "Returns full string definition for message of type 'BroadcastString-response"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BroadcastString-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BroadcastString-response>))
  "Converts a ROS message object to a list"
  (cl:list 'BroadcastString-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'BroadcastString)))
  'BroadcastString-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'BroadcastString)))
  'BroadcastString-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BroadcastString)))
  "Returns string type for a service object of type '<BroadcastString>"
  "adhoc_communication/BroadcastString")