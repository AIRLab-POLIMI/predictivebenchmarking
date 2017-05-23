; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-msg)


;//! \htmlinclude RecvString.msg.html

(cl:defclass <RecvString> (roslisp-msg-protocol:ros-message)
  ((src_robot
    :reader src_robot
    :initarg :src_robot
    :type cl:string
    :initform "")
   (data
    :reader data
    :initarg :data
    :type cl:string
    :initform ""))
)

(cl:defclass RecvString (<RecvString>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RecvString>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RecvString)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-msg:<RecvString> is deprecated: use adhoc_communication-msg:RecvString instead.")))

(cl:ensure-generic-function 'src_robot-val :lambda-list '(m))
(cl:defmethod src_robot-val ((m <RecvString>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:src_robot-val is deprecated.  Use adhoc_communication-msg:src_robot instead.")
  (src_robot m))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <RecvString>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:data-val is deprecated.  Use adhoc_communication-msg:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RecvString>) ostream)
  "Serializes a message object of type '<RecvString>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'src_robot))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'src_robot))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RecvString>) istream)
  "Deserializes a message object of type '<RecvString>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'src_robot) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'src_robot) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'data) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'data) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RecvString>)))
  "Returns string type for a message object of type '<RecvString>"
  "adhoc_communication/RecvString")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RecvString)))
  "Returns string type for a message object of type 'RecvString"
  "adhoc_communication/RecvString")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RecvString>)))
  "Returns md5sum for a message object of type '<RecvString>"
  "357efa7118aea6ce32be041203afb4ca")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RecvString)))
  "Returns md5sum for a message object of type 'RecvString"
  "357efa7118aea6ce32be041203afb4ca")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RecvString>)))
  "Returns full string definition for message of type '<RecvString>"
  (cl:format cl:nil "string src_robot~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RecvString)))
  "Returns full string definition for message of type 'RecvString"
  (cl:format cl:nil "string src_robot~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RecvString>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'src_robot))
     4 (cl:length (cl:slot-value msg 'data))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RecvString>))
  "Converts a ROS message object to a list"
  (cl:list 'RecvString
    (cl:cons ':src_robot (src_robot msg))
    (cl:cons ':data (data msg))
))
