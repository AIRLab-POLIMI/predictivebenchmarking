; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude SendMmControl-request.msg.html

(cl:defclass <SendMmControl-request> (roslisp-msg-protocol:ros-message)
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
   (msg
    :reader msg
    :initarg :msg
    :type adhoc_communication-msg:MmControl
    :initform (cl:make-instance 'adhoc_communication-msg:MmControl)))
)

(cl:defclass SendMmControl-request (<SendMmControl-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendMmControl-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendMmControl-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendMmControl-request> is deprecated: use adhoc_communication-srv:SendMmControl-request instead.")))

(cl:ensure-generic-function 'dst_robot-val :lambda-list '(m))
(cl:defmethod dst_robot-val ((m <SendMmControl-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:dst_robot-val is deprecated.  Use adhoc_communication-srv:dst_robot instead.")
  (dst_robot m))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <SendMmControl-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:topic-val is deprecated.  Use adhoc_communication-srv:topic instead.")
  (topic m))

(cl:ensure-generic-function 'msg-val :lambda-list '(m))
(cl:defmethod msg-val ((m <SendMmControl-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:msg-val is deprecated.  Use adhoc_communication-srv:msg instead.")
  (msg m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendMmControl-request>) ostream)
  "Serializes a message object of type '<SendMmControl-request>"
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
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'msg) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendMmControl-request>) istream)
  "Deserializes a message object of type '<SendMmControl-request>"
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
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'msg) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendMmControl-request>)))
  "Returns string type for a service object of type '<SendMmControl-request>"
  "adhoc_communication/SendMmControlRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendMmControl-request)))
  "Returns string type for a service object of type 'SendMmControl-request"
  "adhoc_communication/SendMmControlRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendMmControl-request>)))
  "Returns md5sum for a message object of type '<SendMmControl-request>"
  "c76c9edaa817ebcfb6a616740eff76e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendMmControl-request)))
  "Returns md5sum for a message object of type 'SendMmControl-request"
  "c76c9edaa817ebcfb6a616740eff76e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendMmControl-request>)))
  "Returns full string definition for message of type '<SendMmControl-request>"
  (cl:format cl:nil "string dst_robot~%string topic~%adhoc_communication/MmControl msg~%~%================================================================================~%MSG: adhoc_communication/MmControl~%string src_robot~%int32[] update_numbers~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendMmControl-request)))
  "Returns full string definition for message of type 'SendMmControl-request"
  (cl:format cl:nil "string dst_robot~%string topic~%adhoc_communication/MmControl msg~%~%================================================================================~%MSG: adhoc_communication/MmControl~%string src_robot~%int32[] update_numbers~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendMmControl-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'dst_robot))
     4 (cl:length (cl:slot-value msg 'topic))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'msg))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendMmControl-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SendMmControl-request
    (cl:cons ':dst_robot (dst_robot msg))
    (cl:cons ':topic (topic msg))
    (cl:cons ':msg (msg msg))
))
;//! \htmlinclude SendMmControl-response.msg.html

(cl:defclass <SendMmControl-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SendMmControl-response (<SendMmControl-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendMmControl-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendMmControl-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendMmControl-response> is deprecated: use adhoc_communication-srv:SendMmControl-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <SendMmControl-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:status-val is deprecated.  Use adhoc_communication-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendMmControl-response>) ostream)
  "Serializes a message object of type '<SendMmControl-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendMmControl-response>) istream)
  "Deserializes a message object of type '<SendMmControl-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendMmControl-response>)))
  "Returns string type for a service object of type '<SendMmControl-response>"
  "adhoc_communication/SendMmControlResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendMmControl-response)))
  "Returns string type for a service object of type 'SendMmControl-response"
  "adhoc_communication/SendMmControlResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendMmControl-response>)))
  "Returns md5sum for a message object of type '<SendMmControl-response>"
  "c76c9edaa817ebcfb6a616740eff76e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendMmControl-response)))
  "Returns md5sum for a message object of type 'SendMmControl-response"
  "c76c9edaa817ebcfb6a616740eff76e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendMmControl-response>)))
  "Returns full string definition for message of type '<SendMmControl-response>"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendMmControl-response)))
  "Returns full string definition for message of type 'SendMmControl-response"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendMmControl-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendMmControl-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SendMmControl-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SendMmControl)))
  'SendMmControl-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SendMmControl)))
  'SendMmControl-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendMmControl)))
  "Returns string type for a service object of type '<SendMmControl>"
  "adhoc_communication/SendMmControl")