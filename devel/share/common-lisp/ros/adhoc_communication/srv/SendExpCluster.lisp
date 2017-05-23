; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude SendExpCluster-request.msg.html

(cl:defclass <SendExpCluster-request> (roslisp-msg-protocol:ros-message)
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
   (cluster
    :reader cluster
    :initarg :cluster
    :type adhoc_communication-msg:ExpCluster
    :initform (cl:make-instance 'adhoc_communication-msg:ExpCluster)))
)

(cl:defclass SendExpCluster-request (<SendExpCluster-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendExpCluster-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendExpCluster-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendExpCluster-request> is deprecated: use adhoc_communication-srv:SendExpCluster-request instead.")))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <SendExpCluster-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:topic-val is deprecated.  Use adhoc_communication-srv:topic instead.")
  (topic m))

(cl:ensure-generic-function 'dst_robot-val :lambda-list '(m))
(cl:defmethod dst_robot-val ((m <SendExpCluster-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:dst_robot-val is deprecated.  Use adhoc_communication-srv:dst_robot instead.")
  (dst_robot m))

(cl:ensure-generic-function 'cluster-val :lambda-list '(m))
(cl:defmethod cluster-val ((m <SendExpCluster-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:cluster-val is deprecated.  Use adhoc_communication-srv:cluster instead.")
  (cluster m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendExpCluster-request>) ostream)
  "Serializes a message object of type '<SendExpCluster-request>"
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
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'cluster) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendExpCluster-request>) istream)
  "Deserializes a message object of type '<SendExpCluster-request>"
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
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'cluster) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendExpCluster-request>)))
  "Returns string type for a service object of type '<SendExpCluster-request>"
  "adhoc_communication/SendExpClusterRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendExpCluster-request)))
  "Returns string type for a service object of type 'SendExpCluster-request"
  "adhoc_communication/SendExpClusterRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendExpCluster-request>)))
  "Returns md5sum for a message object of type '<SendExpCluster-request>"
  "356dd4b5adb461bab3c183a7d7c21532")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendExpCluster-request)))
  "Returns md5sum for a message object of type 'SendExpCluster-request"
  "356dd4b5adb461bab3c183a7d7c21532")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendExpCluster-request>)))
  "Returns full string definition for message of type '<SendExpCluster-request>"
  (cl:format cl:nil "string topic~%string dst_robot~%adhoc_communication/ExpCluster cluster~%~%================================================================================~%MSG: adhoc_communication/ExpCluster~%ExpClusterElement[] ids_contained~%float64 bid ~%~%================================================================================~%MSG: adhoc_communication/ExpClusterElement~%int64 id~%string detected_by_robot_str~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendExpCluster-request)))
  "Returns full string definition for message of type 'SendExpCluster-request"
  (cl:format cl:nil "string topic~%string dst_robot~%adhoc_communication/ExpCluster cluster~%~%================================================================================~%MSG: adhoc_communication/ExpCluster~%ExpClusterElement[] ids_contained~%float64 bid ~%~%================================================================================~%MSG: adhoc_communication/ExpClusterElement~%int64 id~%string detected_by_robot_str~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendExpCluster-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'topic))
     4 (cl:length (cl:slot-value msg 'dst_robot))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'cluster))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendExpCluster-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SendExpCluster-request
    (cl:cons ':topic (topic msg))
    (cl:cons ':dst_robot (dst_robot msg))
    (cl:cons ':cluster (cluster msg))
))
;//! \htmlinclude SendExpCluster-response.msg.html

(cl:defclass <SendExpCluster-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SendExpCluster-response (<SendExpCluster-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendExpCluster-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendExpCluster-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendExpCluster-response> is deprecated: use adhoc_communication-srv:SendExpCluster-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <SendExpCluster-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:status-val is deprecated.  Use adhoc_communication-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendExpCluster-response>) ostream)
  "Serializes a message object of type '<SendExpCluster-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendExpCluster-response>) istream)
  "Deserializes a message object of type '<SendExpCluster-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendExpCluster-response>)))
  "Returns string type for a service object of type '<SendExpCluster-response>"
  "adhoc_communication/SendExpClusterResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendExpCluster-response)))
  "Returns string type for a service object of type 'SendExpCluster-response"
  "adhoc_communication/SendExpClusterResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendExpCluster-response>)))
  "Returns md5sum for a message object of type '<SendExpCluster-response>"
  "356dd4b5adb461bab3c183a7d7c21532")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendExpCluster-response)))
  "Returns md5sum for a message object of type 'SendExpCluster-response"
  "356dd4b5adb461bab3c183a7d7c21532")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendExpCluster-response>)))
  "Returns full string definition for message of type '<SendExpCluster-response>"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendExpCluster-response)))
  "Returns full string definition for message of type 'SendExpCluster-response"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendExpCluster-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendExpCluster-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SendExpCluster-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SendExpCluster)))
  'SendExpCluster-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SendExpCluster)))
  'SendExpCluster-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendExpCluster)))
  "Returns string type for a service object of type '<SendExpCluster>"
  "adhoc_communication/SendExpCluster")