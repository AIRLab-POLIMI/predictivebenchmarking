; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude SendExpAuction-request.msg.html

(cl:defclass <SendExpAuction-request> (roslisp-msg-protocol:ros-message)
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
    :type adhoc_communication-msg:ExpAuction
    :initform (cl:make-instance 'adhoc_communication-msg:ExpAuction)))
)

(cl:defclass SendExpAuction-request (<SendExpAuction-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendExpAuction-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendExpAuction-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendExpAuction-request> is deprecated: use adhoc_communication-srv:SendExpAuction-request instead.")))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <SendExpAuction-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:topic-val is deprecated.  Use adhoc_communication-srv:topic instead.")
  (topic m))

(cl:ensure-generic-function 'dst_robot-val :lambda-list '(m))
(cl:defmethod dst_robot-val ((m <SendExpAuction-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:dst_robot-val is deprecated.  Use adhoc_communication-srv:dst_robot instead.")
  (dst_robot m))

(cl:ensure-generic-function 'auction-val :lambda-list '(m))
(cl:defmethod auction-val ((m <SendExpAuction-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:auction-val is deprecated.  Use adhoc_communication-srv:auction instead.")
  (auction m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendExpAuction-request>) ostream)
  "Serializes a message object of type '<SendExpAuction-request>"
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendExpAuction-request>) istream)
  "Deserializes a message object of type '<SendExpAuction-request>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendExpAuction-request>)))
  "Returns string type for a service object of type '<SendExpAuction-request>"
  "adhoc_communication/SendExpAuctionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendExpAuction-request)))
  "Returns string type for a service object of type 'SendExpAuction-request"
  "adhoc_communication/SendExpAuctionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendExpAuction-request>)))
  "Returns md5sum for a message object of type '<SendExpAuction-request>"
  "ff9ea50dac4ae5fb2075cab78b2fc2b9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendExpAuction-request)))
  "Returns md5sum for a message object of type 'SendExpAuction-request"
  "ff9ea50dac4ae5fb2075cab78b2fc2b9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendExpAuction-request>)))
  "Returns full string definition for message of type '<SendExpAuction-request>"
  (cl:format cl:nil "string topic~%string dst_robot~%adhoc_communication/ExpAuction auction~%~%================================================================================~%MSG: adhoc_communication/ExpAuction~%bool auction_status_message~%bool start_auction~%bool auction_finished~%ExpAuctionElement[] occupied_ids~%ExpCluster[] requested_clusters~%uint32 auction_id~%string robot_name~%ExpCluster[] available_clusters~%~%================================================================================~%MSG: adhoc_communication/ExpAuctionElement~%int64 id~%string detected_by_robot_str~%~%================================================================================~%MSG: adhoc_communication/ExpCluster~%ExpClusterElement[] ids_contained~%float64 bid ~%~%================================================================================~%MSG: adhoc_communication/ExpClusterElement~%int64 id~%string detected_by_robot_str~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendExpAuction-request)))
  "Returns full string definition for message of type 'SendExpAuction-request"
  (cl:format cl:nil "string topic~%string dst_robot~%adhoc_communication/ExpAuction auction~%~%================================================================================~%MSG: adhoc_communication/ExpAuction~%bool auction_status_message~%bool start_auction~%bool auction_finished~%ExpAuctionElement[] occupied_ids~%ExpCluster[] requested_clusters~%uint32 auction_id~%string robot_name~%ExpCluster[] available_clusters~%~%================================================================================~%MSG: adhoc_communication/ExpAuctionElement~%int64 id~%string detected_by_robot_str~%~%================================================================================~%MSG: adhoc_communication/ExpCluster~%ExpClusterElement[] ids_contained~%float64 bid ~%~%================================================================================~%MSG: adhoc_communication/ExpClusterElement~%int64 id~%string detected_by_robot_str~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendExpAuction-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'topic))
     4 (cl:length (cl:slot-value msg 'dst_robot))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'auction))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendExpAuction-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SendExpAuction-request
    (cl:cons ':topic (topic msg))
    (cl:cons ':dst_robot (dst_robot msg))
    (cl:cons ':auction (auction msg))
))
;//! \htmlinclude SendExpAuction-response.msg.html

(cl:defclass <SendExpAuction-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SendExpAuction-response (<SendExpAuction-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendExpAuction-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendExpAuction-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendExpAuction-response> is deprecated: use adhoc_communication-srv:SendExpAuction-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <SendExpAuction-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:status-val is deprecated.  Use adhoc_communication-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendExpAuction-response>) ostream)
  "Serializes a message object of type '<SendExpAuction-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendExpAuction-response>) istream)
  "Deserializes a message object of type '<SendExpAuction-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendExpAuction-response>)))
  "Returns string type for a service object of type '<SendExpAuction-response>"
  "adhoc_communication/SendExpAuctionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendExpAuction-response)))
  "Returns string type for a service object of type 'SendExpAuction-response"
  "adhoc_communication/SendExpAuctionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendExpAuction-response>)))
  "Returns md5sum for a message object of type '<SendExpAuction-response>"
  "ff9ea50dac4ae5fb2075cab78b2fc2b9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendExpAuction-response)))
  "Returns md5sum for a message object of type 'SendExpAuction-response"
  "ff9ea50dac4ae5fb2075cab78b2fc2b9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendExpAuction-response>)))
  "Returns full string definition for message of type '<SendExpAuction-response>"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendExpAuction-response)))
  "Returns full string definition for message of type 'SendExpAuction-response"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendExpAuction-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendExpAuction-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SendExpAuction-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SendExpAuction)))
  'SendExpAuction-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SendExpAuction)))
  'SendExpAuction-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendExpAuction)))
  "Returns string type for a service object of type '<SendExpAuction>"
  "adhoc_communication/SendExpAuction")