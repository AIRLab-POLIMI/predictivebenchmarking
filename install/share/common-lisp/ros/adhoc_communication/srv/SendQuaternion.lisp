; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude SendQuaternion-request.msg.html

(cl:defclass <SendQuaternion-request> (roslisp-msg-protocol:ros-message)
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
   (quaternion
    :reader quaternion
    :initarg :quaternion
    :type geometry_msgs-msg:Quaternion
    :initform (cl:make-instance 'geometry_msgs-msg:Quaternion)))
)

(cl:defclass SendQuaternion-request (<SendQuaternion-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendQuaternion-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendQuaternion-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendQuaternion-request> is deprecated: use adhoc_communication-srv:SendQuaternion-request instead.")))

(cl:ensure-generic-function 'dst_robot-val :lambda-list '(m))
(cl:defmethod dst_robot-val ((m <SendQuaternion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:dst_robot-val is deprecated.  Use adhoc_communication-srv:dst_robot instead.")
  (dst_robot m))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <SendQuaternion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:topic-val is deprecated.  Use adhoc_communication-srv:topic instead.")
  (topic m))

(cl:ensure-generic-function 'quaternion-val :lambda-list '(m))
(cl:defmethod quaternion-val ((m <SendQuaternion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:quaternion-val is deprecated.  Use adhoc_communication-srv:quaternion instead.")
  (quaternion m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendQuaternion-request>) ostream)
  "Serializes a message object of type '<SendQuaternion-request>"
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
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'quaternion) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendQuaternion-request>) istream)
  "Deserializes a message object of type '<SendQuaternion-request>"
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
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'quaternion) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendQuaternion-request>)))
  "Returns string type for a service object of type '<SendQuaternion-request>"
  "adhoc_communication/SendQuaternionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendQuaternion-request)))
  "Returns string type for a service object of type 'SendQuaternion-request"
  "adhoc_communication/SendQuaternionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendQuaternion-request>)))
  "Returns md5sum for a message object of type '<SendQuaternion-request>"
  "6d4c9ce8c8598fcc5972b254856eb7e3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendQuaternion-request)))
  "Returns md5sum for a message object of type 'SendQuaternion-request"
  "6d4c9ce8c8598fcc5972b254856eb7e3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendQuaternion-request>)))
  "Returns full string definition for message of type '<SendQuaternion-request>"
  (cl:format cl:nil "string dst_robot~%string topic~%geometry_msgs/Quaternion quaternion~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendQuaternion-request)))
  "Returns full string definition for message of type 'SendQuaternion-request"
  (cl:format cl:nil "string dst_robot~%string topic~%geometry_msgs/Quaternion quaternion~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendQuaternion-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'dst_robot))
     4 (cl:length (cl:slot-value msg 'topic))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'quaternion))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendQuaternion-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SendQuaternion-request
    (cl:cons ':dst_robot (dst_robot msg))
    (cl:cons ':topic (topic msg))
    (cl:cons ':quaternion (quaternion msg))
))
;//! \htmlinclude SendQuaternion-response.msg.html

(cl:defclass <SendQuaternion-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SendQuaternion-response (<SendQuaternion-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendQuaternion-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendQuaternion-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendQuaternion-response> is deprecated: use adhoc_communication-srv:SendQuaternion-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <SendQuaternion-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:status-val is deprecated.  Use adhoc_communication-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendQuaternion-response>) ostream)
  "Serializes a message object of type '<SendQuaternion-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendQuaternion-response>) istream)
  "Deserializes a message object of type '<SendQuaternion-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendQuaternion-response>)))
  "Returns string type for a service object of type '<SendQuaternion-response>"
  "adhoc_communication/SendQuaternionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendQuaternion-response)))
  "Returns string type for a service object of type 'SendQuaternion-response"
  "adhoc_communication/SendQuaternionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendQuaternion-response>)))
  "Returns md5sum for a message object of type '<SendQuaternion-response>"
  "6d4c9ce8c8598fcc5972b254856eb7e3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendQuaternion-response)))
  "Returns md5sum for a message object of type 'SendQuaternion-response"
  "6d4c9ce8c8598fcc5972b254856eb7e3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendQuaternion-response>)))
  "Returns full string definition for message of type '<SendQuaternion-response>"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendQuaternion-response)))
  "Returns full string definition for message of type 'SendQuaternion-response"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendQuaternion-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendQuaternion-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SendQuaternion-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SendQuaternion)))
  'SendQuaternion-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SendQuaternion)))
  'SendQuaternion-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendQuaternion)))
  "Returns string type for a service object of type '<SendQuaternion>"
  "adhoc_communication/SendQuaternion")