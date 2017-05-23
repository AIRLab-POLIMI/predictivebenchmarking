; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-msg)


;//! \htmlinclude ExpClusterElement.msg.html

(cl:defclass <ExpClusterElement> (roslisp-msg-protocol:ros-message)
  ((id
    :reader id
    :initarg :id
    :type cl:integer
    :initform 0)
   (detected_by_robot_str
    :reader detected_by_robot_str
    :initarg :detected_by_robot_str
    :type cl:string
    :initform ""))
)

(cl:defclass ExpClusterElement (<ExpClusterElement>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ExpClusterElement>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ExpClusterElement)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-msg:<ExpClusterElement> is deprecated: use adhoc_communication-msg:ExpClusterElement instead.")))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <ExpClusterElement>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:id-val is deprecated.  Use adhoc_communication-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'detected_by_robot_str-val :lambda-list '(m))
(cl:defmethod detected_by_robot_str-val ((m <ExpClusterElement>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:detected_by_robot_str-val is deprecated.  Use adhoc_communication-msg:detected_by_robot_str instead.")
  (detected_by_robot_str m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ExpClusterElement>) ostream)
  "Serializes a message object of type '<ExpClusterElement>"
  (cl:let* ((signed (cl:slot-value msg 'id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'detected_by_robot_str))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'detected_by_robot_str))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ExpClusterElement>) istream)
  "Deserializes a message object of type '<ExpClusterElement>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'id) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'detected_by_robot_str) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'detected_by_robot_str) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ExpClusterElement>)))
  "Returns string type for a message object of type '<ExpClusterElement>"
  "adhoc_communication/ExpClusterElement")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExpClusterElement)))
  "Returns string type for a message object of type 'ExpClusterElement"
  "adhoc_communication/ExpClusterElement")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ExpClusterElement>)))
  "Returns md5sum for a message object of type '<ExpClusterElement>"
  "4c7924311e9f149f7f5025e4bf173fd7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ExpClusterElement)))
  "Returns md5sum for a message object of type 'ExpClusterElement"
  "4c7924311e9f149f7f5025e4bf173fd7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ExpClusterElement>)))
  "Returns full string definition for message of type '<ExpClusterElement>"
  (cl:format cl:nil "int64 id~%string detected_by_robot_str~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ExpClusterElement)))
  "Returns full string definition for message of type 'ExpClusterElement"
  (cl:format cl:nil "int64 id~%string detected_by_robot_str~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ExpClusterElement>))
  (cl:+ 0
     8
     4 (cl:length (cl:slot-value msg 'detected_by_robot_str))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ExpClusterElement>))
  "Converts a ROS message object to a list"
  (cl:list 'ExpClusterElement
    (cl:cons ':id (id msg))
    (cl:cons ':detected_by_robot_str (detected_by_robot_str msg))
))
