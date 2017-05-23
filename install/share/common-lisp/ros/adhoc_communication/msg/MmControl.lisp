; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-msg)


;//! \htmlinclude MmControl.msg.html

(cl:defclass <MmControl> (roslisp-msg-protocol:ros-message)
  ((src_robot
    :reader src_robot
    :initarg :src_robot
    :type cl:string
    :initform "")
   (update_numbers
    :reader update_numbers
    :initarg :update_numbers
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass MmControl (<MmControl>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MmControl>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MmControl)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-msg:<MmControl> is deprecated: use adhoc_communication-msg:MmControl instead.")))

(cl:ensure-generic-function 'src_robot-val :lambda-list '(m))
(cl:defmethod src_robot-val ((m <MmControl>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:src_robot-val is deprecated.  Use adhoc_communication-msg:src_robot instead.")
  (src_robot m))

(cl:ensure-generic-function 'update_numbers-val :lambda-list '(m))
(cl:defmethod update_numbers-val ((m <MmControl>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:update_numbers-val is deprecated.  Use adhoc_communication-msg:update_numbers instead.")
  (update_numbers m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MmControl>) ostream)
  "Serializes a message object of type '<MmControl>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'src_robot))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'src_robot))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'update_numbers))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'update_numbers))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MmControl>) istream)
  "Deserializes a message object of type '<MmControl>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'src_robot) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'src_robot) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'update_numbers) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'update_numbers)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MmControl>)))
  "Returns string type for a message object of type '<MmControl>"
  "adhoc_communication/MmControl")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MmControl)))
  "Returns string type for a message object of type 'MmControl"
  "adhoc_communication/MmControl")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MmControl>)))
  "Returns md5sum for a message object of type '<MmControl>"
  "3d223057e1839a50fdaaef262568a5a7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MmControl)))
  "Returns md5sum for a message object of type 'MmControl"
  "3d223057e1839a50fdaaef262568a5a7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MmControl>)))
  "Returns full string definition for message of type '<MmControl>"
  (cl:format cl:nil "string src_robot~%int32[] update_numbers~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MmControl)))
  "Returns full string definition for message of type 'MmControl"
  (cl:format cl:nil "string src_robot~%int32[] update_numbers~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MmControl>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'src_robot))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'update_numbers) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MmControl>))
  "Converts a ROS message object to a list"
  (cl:list 'MmControl
    (cl:cons ':src_robot (src_robot msg))
    (cl:cons ':update_numbers (update_numbers msg))
))
