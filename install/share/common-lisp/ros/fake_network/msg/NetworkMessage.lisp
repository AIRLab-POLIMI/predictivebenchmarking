; Auto-generated. Do not edit!


(cl:in-package fake_network-msg)


;//! \htmlinclude NetworkMessage.msg.html

(cl:defclass <NetworkMessage> (roslisp-msg-protocol:ros-message)
  ((source_robot
    :reader source_robot
    :initarg :source_robot
    :type cl:string
    :initform "")
   (payload
    :reader payload
    :initarg :payload
    :type cl:string
    :initform "")
   (data_type
    :reader data_type
    :initarg :data_type
    :type cl:fixnum
    :initform 0)
   (topic
    :reader topic
    :initarg :topic
    :type cl:string
    :initform ""))
)

(cl:defclass NetworkMessage (<NetworkMessage>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <NetworkMessage>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'NetworkMessage)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name fake_network-msg:<NetworkMessage> is deprecated: use fake_network-msg:NetworkMessage instead.")))

(cl:ensure-generic-function 'source_robot-val :lambda-list '(m))
(cl:defmethod source_robot-val ((m <NetworkMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fake_network-msg:source_robot-val is deprecated.  Use fake_network-msg:source_robot instead.")
  (source_robot m))

(cl:ensure-generic-function 'payload-val :lambda-list '(m))
(cl:defmethod payload-val ((m <NetworkMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fake_network-msg:payload-val is deprecated.  Use fake_network-msg:payload instead.")
  (payload m))

(cl:ensure-generic-function 'data_type-val :lambda-list '(m))
(cl:defmethod data_type-val ((m <NetworkMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fake_network-msg:data_type-val is deprecated.  Use fake_network-msg:data_type instead.")
  (data_type m))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <NetworkMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fake_network-msg:topic-val is deprecated.  Use fake_network-msg:topic instead.")
  (topic m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <NetworkMessage>) ostream)
  "Serializes a message object of type '<NetworkMessage>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'source_robot))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'source_robot))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'payload))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'payload))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'data_type)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'topic))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'topic))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <NetworkMessage>) istream)
  "Deserializes a message object of type '<NetworkMessage>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'source_robot) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'source_robot) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'payload) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'payload) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'data_type)) (cl:read-byte istream))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'topic) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'topic) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<NetworkMessage>)))
  "Returns string type for a message object of type '<NetworkMessage>"
  "fake_network/NetworkMessage")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'NetworkMessage)))
  "Returns string type for a message object of type 'NetworkMessage"
  "fake_network/NetworkMessage")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<NetworkMessage>)))
  "Returns md5sum for a message object of type '<NetworkMessage>"
  "67d28fd41fb2346145ecac16f2c7c957")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'NetworkMessage)))
  "Returns md5sum for a message object of type 'NetworkMessage"
  "67d28fd41fb2346145ecac16f2c7c957")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<NetworkMessage>)))
  "Returns full string definition for message of type '<NetworkMessage>"
  (cl:format cl:nil "string source_robot~%string payload~%uint8 data_type~%string topic~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'NetworkMessage)))
  "Returns full string definition for message of type 'NetworkMessage"
  (cl:format cl:nil "string source_robot~%string payload~%uint8 data_type~%string topic~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <NetworkMessage>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'source_robot))
     4 (cl:length (cl:slot-value msg 'payload))
     1
     4 (cl:length (cl:slot-value msg 'topic))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <NetworkMessage>))
  "Converts a ROS message object to a list"
  (cl:list 'NetworkMessage
    (cl:cons ':source_robot (source_robot msg))
    (cl:cons ':payload (payload msg))
    (cl:cons ':data_type (data_type msg))
    (cl:cons ':topic (topic msg))
))
