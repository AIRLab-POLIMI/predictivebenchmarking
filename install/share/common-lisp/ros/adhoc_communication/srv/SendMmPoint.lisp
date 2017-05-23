; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude SendMmPoint-request.msg.html

(cl:defclass <SendMmPoint-request> (roslisp-msg-protocol:ros-message)
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
   (point
    :reader point
    :initarg :point
    :type adhoc_communication-msg:MmPoint
    :initform (cl:make-instance 'adhoc_communication-msg:MmPoint)))
)

(cl:defclass SendMmPoint-request (<SendMmPoint-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendMmPoint-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendMmPoint-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendMmPoint-request> is deprecated: use adhoc_communication-srv:SendMmPoint-request instead.")))

(cl:ensure-generic-function 'dst_robot-val :lambda-list '(m))
(cl:defmethod dst_robot-val ((m <SendMmPoint-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:dst_robot-val is deprecated.  Use adhoc_communication-srv:dst_robot instead.")
  (dst_robot m))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <SendMmPoint-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:topic-val is deprecated.  Use adhoc_communication-srv:topic instead.")
  (topic m))

(cl:ensure-generic-function 'point-val :lambda-list '(m))
(cl:defmethod point-val ((m <SendMmPoint-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:point-val is deprecated.  Use adhoc_communication-srv:point instead.")
  (point m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendMmPoint-request>) ostream)
  "Serializes a message object of type '<SendMmPoint-request>"
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
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'point) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendMmPoint-request>) istream)
  "Deserializes a message object of type '<SendMmPoint-request>"
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
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'point) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendMmPoint-request>)))
  "Returns string type for a service object of type '<SendMmPoint-request>"
  "adhoc_communication/SendMmPointRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendMmPoint-request)))
  "Returns string type for a service object of type 'SendMmPoint-request"
  "adhoc_communication/SendMmPointRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendMmPoint-request>)))
  "Returns md5sum for a message object of type '<SendMmPoint-request>"
  "caf6ffd259d365577a9cd46d32b9cb17")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendMmPoint-request)))
  "Returns md5sum for a message object of type 'SendMmPoint-request"
  "caf6ffd259d365577a9cd46d32b9cb17")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendMmPoint-request>)))
  "Returns full string definition for message of type '<SendMmPoint-request>"
  (cl:format cl:nil "string dst_robot~%string topic~%adhoc_communication/MmPoint point~%~%================================================================================~%MSG: adhoc_communication/MmPoint~%string src_robot~%float64 x~%float64 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendMmPoint-request)))
  "Returns full string definition for message of type 'SendMmPoint-request"
  (cl:format cl:nil "string dst_robot~%string topic~%adhoc_communication/MmPoint point~%~%================================================================================~%MSG: adhoc_communication/MmPoint~%string src_robot~%float64 x~%float64 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendMmPoint-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'dst_robot))
     4 (cl:length (cl:slot-value msg 'topic))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'point))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendMmPoint-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SendMmPoint-request
    (cl:cons ':dst_robot (dst_robot msg))
    (cl:cons ':topic (topic msg))
    (cl:cons ':point (point msg))
))
;//! \htmlinclude SendMmPoint-response.msg.html

(cl:defclass <SendMmPoint-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SendMmPoint-response (<SendMmPoint-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendMmPoint-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendMmPoint-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendMmPoint-response> is deprecated: use adhoc_communication-srv:SendMmPoint-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <SendMmPoint-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:status-val is deprecated.  Use adhoc_communication-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendMmPoint-response>) ostream)
  "Serializes a message object of type '<SendMmPoint-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendMmPoint-response>) istream)
  "Deserializes a message object of type '<SendMmPoint-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendMmPoint-response>)))
  "Returns string type for a service object of type '<SendMmPoint-response>"
  "adhoc_communication/SendMmPointResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendMmPoint-response)))
  "Returns string type for a service object of type 'SendMmPoint-response"
  "adhoc_communication/SendMmPointResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendMmPoint-response>)))
  "Returns md5sum for a message object of type '<SendMmPoint-response>"
  "caf6ffd259d365577a9cd46d32b9cb17")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendMmPoint-response)))
  "Returns md5sum for a message object of type 'SendMmPoint-response"
  "caf6ffd259d365577a9cd46d32b9cb17")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendMmPoint-response>)))
  "Returns full string definition for message of type '<SendMmPoint-response>"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendMmPoint-response)))
  "Returns full string definition for message of type 'SendMmPoint-response"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendMmPoint-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendMmPoint-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SendMmPoint-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SendMmPoint)))
  'SendMmPoint-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SendMmPoint)))
  'SendMmPoint-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendMmPoint)))
  "Returns string type for a service object of type '<SendMmPoint>"
  "adhoc_communication/SendMmPoint")