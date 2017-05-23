; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-msg)


;//! \htmlinclude ExpAuctionElement.msg.html

(cl:defclass <ExpAuctionElement> (roslisp-msg-protocol:ros-message)
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

(cl:defclass ExpAuctionElement (<ExpAuctionElement>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ExpAuctionElement>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ExpAuctionElement)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-msg:<ExpAuctionElement> is deprecated: use adhoc_communication-msg:ExpAuctionElement instead.")))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <ExpAuctionElement>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:id-val is deprecated.  Use adhoc_communication-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'detected_by_robot_str-val :lambda-list '(m))
(cl:defmethod detected_by_robot_str-val ((m <ExpAuctionElement>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:detected_by_robot_str-val is deprecated.  Use adhoc_communication-msg:detected_by_robot_str instead.")
  (detected_by_robot_str m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ExpAuctionElement>) ostream)
  "Serializes a message object of type '<ExpAuctionElement>"
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ExpAuctionElement>) istream)
  "Deserializes a message object of type '<ExpAuctionElement>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ExpAuctionElement>)))
  "Returns string type for a message object of type '<ExpAuctionElement>"
  "adhoc_communication/ExpAuctionElement")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExpAuctionElement)))
  "Returns string type for a message object of type 'ExpAuctionElement"
  "adhoc_communication/ExpAuctionElement")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ExpAuctionElement>)))
  "Returns md5sum for a message object of type '<ExpAuctionElement>"
  "4c7924311e9f149f7f5025e4bf173fd7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ExpAuctionElement)))
  "Returns md5sum for a message object of type 'ExpAuctionElement"
  "4c7924311e9f149f7f5025e4bf173fd7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ExpAuctionElement>)))
  "Returns full string definition for message of type '<ExpAuctionElement>"
  (cl:format cl:nil "int64 id~%string detected_by_robot_str~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ExpAuctionElement)))
  "Returns full string definition for message of type 'ExpAuctionElement"
  (cl:format cl:nil "int64 id~%string detected_by_robot_str~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ExpAuctionElement>))
  (cl:+ 0
     8
     4 (cl:length (cl:slot-value msg 'detected_by_robot_str))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ExpAuctionElement>))
  "Converts a ROS message object to a list"
  (cl:list 'ExpAuctionElement
    (cl:cons ':id (id msg))
    (cl:cons ':detected_by_robot_str (detected_by_robot_str msg))
))
