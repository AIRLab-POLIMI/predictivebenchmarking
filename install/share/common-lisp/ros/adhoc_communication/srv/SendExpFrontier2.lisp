; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude SendExpFrontier2-request.msg.html

(cl:defclass <SendExpFrontier2-request> (roslisp-msg-protocol:ros-message)
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
   (frontier
    :reader frontier
    :initarg :frontier
    :type adhoc_communication-msg:ExpFrontierElement
    :initform (cl:make-instance 'adhoc_communication-msg:ExpFrontierElement)))
)

(cl:defclass SendExpFrontier2-request (<SendExpFrontier2-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendExpFrontier2-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendExpFrontier2-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendExpFrontier2-request> is deprecated: use adhoc_communication-srv:SendExpFrontier2-request instead.")))

(cl:ensure-generic-function 'dst_robot-val :lambda-list '(m))
(cl:defmethod dst_robot-val ((m <SendExpFrontier2-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:dst_robot-val is deprecated.  Use adhoc_communication-srv:dst_robot instead.")
  (dst_robot m))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <SendExpFrontier2-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:topic-val is deprecated.  Use adhoc_communication-srv:topic instead.")
  (topic m))

(cl:ensure-generic-function 'frontier-val :lambda-list '(m))
(cl:defmethod frontier-val ((m <SendExpFrontier2-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:frontier-val is deprecated.  Use adhoc_communication-srv:frontier instead.")
  (frontier m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendExpFrontier2-request>) ostream)
  "Serializes a message object of type '<SendExpFrontier2-request>"
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
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'frontier) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendExpFrontier2-request>) istream)
  "Deserializes a message object of type '<SendExpFrontier2-request>"
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
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'frontier) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendExpFrontier2-request>)))
  "Returns string type for a service object of type '<SendExpFrontier2-request>"
  "adhoc_communication/SendExpFrontier2Request")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendExpFrontier2-request)))
  "Returns string type for a service object of type 'SendExpFrontier2-request"
  "adhoc_communication/SendExpFrontier2Request")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendExpFrontier2-request>)))
  "Returns md5sum for a message object of type '<SendExpFrontier2-request>"
  "c95ef85b5ba5b536a769a25a3d571277")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendExpFrontier2-request)))
  "Returns md5sum for a message object of type 'SendExpFrontier2-request"
  "c95ef85b5ba5b536a769a25a3d571277")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendExpFrontier2-request>)))
  "Returns full string definition for message of type '<SendExpFrontier2-request>"
  (cl:format cl:nil "string dst_robot~%string topic~%adhoc_communication/ExpFrontierElement frontier~%~%================================================================================~%MSG: adhoc_communication/ExpFrontierElement~%int64 id~%string detected_by_robot_str~%int64 detected_by_robot~%float64 robot_home_position_x~%float64 robot_home_position_y~%float64 x_coordinate~%float64 y_coordinate~%float64 bid~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendExpFrontier2-request)))
  "Returns full string definition for message of type 'SendExpFrontier2-request"
  (cl:format cl:nil "string dst_robot~%string topic~%adhoc_communication/ExpFrontierElement frontier~%~%================================================================================~%MSG: adhoc_communication/ExpFrontierElement~%int64 id~%string detected_by_robot_str~%int64 detected_by_robot~%float64 robot_home_position_x~%float64 robot_home_position_y~%float64 x_coordinate~%float64 y_coordinate~%float64 bid~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendExpFrontier2-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'dst_robot))
     4 (cl:length (cl:slot-value msg 'topic))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'frontier))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendExpFrontier2-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SendExpFrontier2-request
    (cl:cons ':dst_robot (dst_robot msg))
    (cl:cons ':topic (topic msg))
    (cl:cons ':frontier (frontier msg))
))
;//! \htmlinclude SendExpFrontier2-response.msg.html

(cl:defclass <SendExpFrontier2-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SendExpFrontier2-response (<SendExpFrontier2-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendExpFrontier2-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendExpFrontier2-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendExpFrontier2-response> is deprecated: use adhoc_communication-srv:SendExpFrontier2-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <SendExpFrontier2-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:status-val is deprecated.  Use adhoc_communication-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendExpFrontier2-response>) ostream)
  "Serializes a message object of type '<SendExpFrontier2-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendExpFrontier2-response>) istream)
  "Deserializes a message object of type '<SendExpFrontier2-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendExpFrontier2-response>)))
  "Returns string type for a service object of type '<SendExpFrontier2-response>"
  "adhoc_communication/SendExpFrontier2Response")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendExpFrontier2-response)))
  "Returns string type for a service object of type 'SendExpFrontier2-response"
  "adhoc_communication/SendExpFrontier2Response")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendExpFrontier2-response>)))
  "Returns md5sum for a message object of type '<SendExpFrontier2-response>"
  "c95ef85b5ba5b536a769a25a3d571277")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendExpFrontier2-response)))
  "Returns md5sum for a message object of type 'SendExpFrontier2-response"
  "c95ef85b5ba5b536a769a25a3d571277")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendExpFrontier2-response>)))
  "Returns full string definition for message of type '<SendExpFrontier2-response>"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendExpFrontier2-response)))
  "Returns full string definition for message of type 'SendExpFrontier2-response"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendExpFrontier2-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendExpFrontier2-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SendExpFrontier2-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SendExpFrontier2)))
  'SendExpFrontier2-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SendExpFrontier2)))
  'SendExpFrontier2-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendExpFrontier2)))
  "Returns string type for a service object of type '<SendExpFrontier2>"
  "adhoc_communication/SendExpFrontier2")