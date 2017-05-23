; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude SendEmAuction-request.msg.html

(cl:defclass <SendEmAuction-request> (roslisp-msg-protocol:ros-message)
  ((topic
    :reader topic
    :initarg :topic
    :type cl:string
    :initform "")
   (dst_robot
    :reader dst_robot
    :initarg :dst_robot
    :type cl:string
    :initform "")
   (auction
    :reader auction
    :initarg :auction
    :type adhoc_communication-msg:EmAuction
    :initform (cl:make-instance 'adhoc_communication-msg:EmAuction)))
)

(cl:defclass SendEmAuction-request (<SendEmAuction-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendEmAuction-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendEmAuction-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendEmAuction-request> is deprecated: use adhoc_communication-srv:SendEmAuction-request instead.")))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <SendEmAuction-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:topic-val is deprecated.  Use adhoc_communication-srv:topic instead.")
  (topic m))

(cl:ensure-generic-function 'dst_robot-val :lambda-list '(m))
(cl:defmethod dst_robot-val ((m <SendEmAuction-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:dst_robot-val is deprecated.  Use adhoc_communication-srv:dst_robot instead.")
  (dst_robot m))

(cl:ensure-generic-function 'auction-val :lambda-list '(m))
(cl:defmethod auction-val ((m <SendEmAuction-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:auction-val is deprecated.  Use adhoc_communication-srv:auction instead.")
  (auction m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendEmAuction-request>) ostream)
  "Serializes a message object of type '<SendEmAuction-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'topic))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'topic))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'dst_robot))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'dst_robot))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'auction) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendEmAuction-request>) istream)
  "Deserializes a message object of type '<SendEmAuction-request>"
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
      (cl:setf (cl:slot-value msg 'dst_robot) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'dst_robot) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'auction) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendEmAuction-request>)))
  "Returns string type for a service object of type '<SendEmAuction-request>"
  "adhoc_communication/SendEmAuctionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendEmAuction-request)))
  "Returns string type for a service object of type 'SendEmAuction-request"
  "adhoc_communication/SendEmAuctionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendEmAuction-request>)))
  "Returns md5sum for a message object of type '<SendEmAuction-request>"
  "c8c30dfd876c5f060f1c0f80b80a6768")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendEmAuction-request)))
  "Returns md5sum for a message object of type 'SendEmAuction-request"
  "c8c30dfd876c5f060f1c0f80b80a6768")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendEmAuction-request>)))
  "Returns full string definition for message of type '<SendEmAuction-request>"
  (cl:format cl:nil "string topic~%string dst_robot~%adhoc_communication/EmAuction auction~%~%================================================================================~%MSG: adhoc_communication/EmAuction~%uint32 auction~%uint32 robot~%uint32 docking_station~%float32 bid~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendEmAuction-request)))
  "Returns full string definition for message of type 'SendEmAuction-request"
  (cl:format cl:nil "string topic~%string dst_robot~%adhoc_communication/EmAuction auction~%~%================================================================================~%MSG: adhoc_communication/EmAuction~%uint32 auction~%uint32 robot~%uint32 docking_station~%float32 bid~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendEmAuction-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'topic))
     4 (cl:length (cl:slot-value msg 'dst_robot))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'auction))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendEmAuction-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SendEmAuction-request
    (cl:cons ':topic (topic msg))
    (cl:cons ':dst_robot (dst_robot msg))
    (cl:cons ':auction (auction msg))
))
;//! \htmlinclude SendEmAuction-response.msg.html

(cl:defclass <SendEmAuction-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SendEmAuction-response (<SendEmAuction-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendEmAuction-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendEmAuction-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendEmAuction-response> is deprecated: use adhoc_communication-srv:SendEmAuction-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <SendEmAuction-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:status-val is deprecated.  Use adhoc_communication-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendEmAuction-response>) ostream)
  "Serializes a message object of type '<SendEmAuction-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendEmAuction-response>) istream)
  "Deserializes a message object of type '<SendEmAuction-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendEmAuction-response>)))
  "Returns string type for a service object of type '<SendEmAuction-response>"
  "adhoc_communication/SendEmAuctionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendEmAuction-response)))
  "Returns string type for a service object of type 'SendEmAuction-response"
  "adhoc_communication/SendEmAuctionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendEmAuction-response>)))
  "Returns md5sum for a message object of type '<SendEmAuction-response>"
  "c8c30dfd876c5f060f1c0f80b80a6768")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendEmAuction-response)))
  "Returns md5sum for a message object of type 'SendEmAuction-response"
  "c8c30dfd876c5f060f1c0f80b80a6768")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendEmAuction-response>)))
  "Returns full string definition for message of type '<SendEmAuction-response>"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendEmAuction-response)))
  "Returns full string definition for message of type 'SendEmAuction-response"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendEmAuction-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendEmAuction-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SendEmAuction-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SendEmAuction)))
  'SendEmAuction-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SendEmAuction)))
  'SendEmAuction-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendEmAuction)))
  "Returns string type for a service object of type '<SendEmAuction>"
  "adhoc_communication/SendEmAuction")