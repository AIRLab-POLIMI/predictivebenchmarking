; Auto-generated. Do not edit!


(cl:in-package nav2d_operator-msg)


;//! \htmlinclude cmd.msg.html

(cl:defclass <cmd> (roslisp-msg-protocol:ros-message)
  ((Velocity
    :reader Velocity
    :initarg :Velocity
    :type cl:float
    :initform 0.0)
   (Turn
    :reader Turn
    :initarg :Turn
    :type cl:float
    :initform 0.0)
   (Mode
    :reader Mode
    :initarg :Mode
    :type cl:fixnum
    :initform 0))
)

(cl:defclass cmd (<cmd>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <cmd>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'cmd)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nav2d_operator-msg:<cmd> is deprecated: use nav2d_operator-msg:cmd instead.")))

(cl:ensure-generic-function 'Velocity-val :lambda-list '(m))
(cl:defmethod Velocity-val ((m <cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nav2d_operator-msg:Velocity-val is deprecated.  Use nav2d_operator-msg:Velocity instead.")
  (Velocity m))

(cl:ensure-generic-function 'Turn-val :lambda-list '(m))
(cl:defmethod Turn-val ((m <cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nav2d_operator-msg:Turn-val is deprecated.  Use nav2d_operator-msg:Turn instead.")
  (Turn m))

(cl:ensure-generic-function 'Mode-val :lambda-list '(m))
(cl:defmethod Mode-val ((m <cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nav2d_operator-msg:Mode-val is deprecated.  Use nav2d_operator-msg:Mode instead.")
  (Mode m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <cmd>) ostream)
  "Serializes a message object of type '<cmd>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'Velocity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'Turn))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'Mode)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <cmd>) istream)
  "Deserializes a message object of type '<cmd>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'Velocity) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'Turn) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'Mode) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<cmd>)))
  "Returns string type for a message object of type '<cmd>"
  "nav2d_operator/cmd")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'cmd)))
  "Returns string type for a message object of type 'cmd"
  "nav2d_operator/cmd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<cmd>)))
  "Returns md5sum for a message object of type '<cmd>"
  "90c9a043660646e2102f124332ecb8b7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'cmd)))
  "Returns md5sum for a message object of type 'cmd"
  "90c9a043660646e2102f124332ecb8b7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<cmd>)))
  "Returns full string definition for message of type '<cmd>"
  (cl:format cl:nil "float64 Velocity~%float64 Turn~%int8    Mode~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'cmd)))
  "Returns full string definition for message of type 'cmd"
  (cl:format cl:nil "float64 Velocity~%float64 Turn~%int8    Mode~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <cmd>))
  (cl:+ 0
     8
     8
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <cmd>))
  "Converts a ROS message object to a list"
  (cl:list 'cmd
    (cl:cons ':Velocity (Velocity msg))
    (cl:cons ':Turn (Turn msg))
    (cl:cons ':Mode (Mode msg))
))
