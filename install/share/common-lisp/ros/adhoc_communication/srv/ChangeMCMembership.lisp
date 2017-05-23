; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude ChangeMCMembership-request.msg.html

(cl:defclass <ChangeMCMembership-request> (roslisp-msg-protocol:ros-message)
  ((group_name
    :reader group_name
    :initarg :group_name
    :type cl:string
    :initform "")
   (action
    :reader action
    :initarg :action
    :type cl:fixnum
    :initform 0))
)

(cl:defclass ChangeMCMembership-request (<ChangeMCMembership-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ChangeMCMembership-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ChangeMCMembership-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<ChangeMCMembership-request> is deprecated: use adhoc_communication-srv:ChangeMCMembership-request instead.")))

(cl:ensure-generic-function 'group_name-val :lambda-list '(m))
(cl:defmethod group_name-val ((m <ChangeMCMembership-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:group_name-val is deprecated.  Use adhoc_communication-srv:group_name instead.")
  (group_name m))

(cl:ensure-generic-function 'action-val :lambda-list '(m))
(cl:defmethod action-val ((m <ChangeMCMembership-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:action-val is deprecated.  Use adhoc_communication-srv:action instead.")
  (action m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ChangeMCMembership-request>) ostream)
  "Serializes a message object of type '<ChangeMCMembership-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'group_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'group_name))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'action)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ChangeMCMembership-request>) istream)
  "Deserializes a message object of type '<ChangeMCMembership-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'group_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'group_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'action)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ChangeMCMembership-request>)))
  "Returns string type for a service object of type '<ChangeMCMembership-request>"
  "adhoc_communication/ChangeMCMembershipRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ChangeMCMembership-request)))
  "Returns string type for a service object of type 'ChangeMCMembership-request"
  "adhoc_communication/ChangeMCMembershipRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ChangeMCMembership-request>)))
  "Returns md5sum for a message object of type '<ChangeMCMembership-request>"
  "49d7b72f6cfca8396fbad0de3d98f799")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ChangeMCMembership-request)))
  "Returns md5sum for a message object of type 'ChangeMCMembership-request"
  "49d7b72f6cfca8396fbad0de3d98f799")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ChangeMCMembership-request>)))
  "Returns full string definition for message of type '<ChangeMCMembership-request>"
  (cl:format cl:nil "string group_name~%uint8 action~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ChangeMCMembership-request)))
  "Returns full string definition for message of type 'ChangeMCMembership-request"
  (cl:format cl:nil "string group_name~%uint8 action~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ChangeMCMembership-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'group_name))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ChangeMCMembership-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ChangeMCMembership-request
    (cl:cons ':group_name (group_name msg))
    (cl:cons ':action (action msg))
))
;//! \htmlinclude ChangeMCMembership-response.msg.html

(cl:defclass <ChangeMCMembership-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass ChangeMCMembership-response (<ChangeMCMembership-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ChangeMCMembership-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ChangeMCMembership-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<ChangeMCMembership-response> is deprecated: use adhoc_communication-srv:ChangeMCMembership-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <ChangeMCMembership-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:status-val is deprecated.  Use adhoc_communication-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ChangeMCMembership-response>) ostream)
  "Serializes a message object of type '<ChangeMCMembership-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ChangeMCMembership-response>) istream)
  "Deserializes a message object of type '<ChangeMCMembership-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ChangeMCMembership-response>)))
  "Returns string type for a service object of type '<ChangeMCMembership-response>"
  "adhoc_communication/ChangeMCMembershipResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ChangeMCMembership-response)))
  "Returns string type for a service object of type 'ChangeMCMembership-response"
  "adhoc_communication/ChangeMCMembershipResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ChangeMCMembership-response>)))
  "Returns md5sum for a message object of type '<ChangeMCMembership-response>"
  "49d7b72f6cfca8396fbad0de3d98f799")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ChangeMCMembership-response)))
  "Returns md5sum for a message object of type 'ChangeMCMembership-response"
  "49d7b72f6cfca8396fbad0de3d98f799")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ChangeMCMembership-response>)))
  "Returns full string definition for message of type '<ChangeMCMembership-response>"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ChangeMCMembership-response)))
  "Returns full string definition for message of type 'ChangeMCMembership-response"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ChangeMCMembership-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ChangeMCMembership-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ChangeMCMembership-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ChangeMCMembership)))
  'ChangeMCMembership-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ChangeMCMembership)))
  'ChangeMCMembership-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ChangeMCMembership)))
  "Returns string type for a service object of type '<ChangeMCMembership>"
  "adhoc_communication/ChangeMCMembership")