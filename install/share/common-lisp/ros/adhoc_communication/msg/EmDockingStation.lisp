; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-msg)


;//! \htmlinclude EmDockingStation.msg.html

(cl:defclass <EmDockingStation> (roslisp-msg-protocol:ros-message)
  ((id
    :reader id
    :initarg :id
    :type cl:integer
    :initform 0)
   (x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (vacant
    :reader vacant
    :initarg :vacant
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass EmDockingStation (<EmDockingStation>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <EmDockingStation>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'EmDockingStation)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-msg:<EmDockingStation> is deprecated: use adhoc_communication-msg:EmDockingStation instead.")))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <EmDockingStation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:id-val is deprecated.  Use adhoc_communication-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <EmDockingStation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:x-val is deprecated.  Use adhoc_communication-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <EmDockingStation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:y-val is deprecated.  Use adhoc_communication-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'vacant-val :lambda-list '(m))
(cl:defmethod vacant-val ((m <EmDockingStation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:vacant-val is deprecated.  Use adhoc_communication-msg:vacant instead.")
  (vacant m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <EmDockingStation>) ostream)
  "Serializes a message object of type '<EmDockingStation>"
  (cl:let* ((signed (cl:slot-value msg 'id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'vacant) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <EmDockingStation>) istream)
  "Deserializes a message object of type '<EmDockingStation>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'id) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:setf (cl:slot-value msg 'vacant) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<EmDockingStation>)))
  "Returns string type for a message object of type '<EmDockingStation>"
  "adhoc_communication/EmDockingStation")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EmDockingStation)))
  "Returns string type for a message object of type 'EmDockingStation"
  "adhoc_communication/EmDockingStation")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<EmDockingStation>)))
  "Returns md5sum for a message object of type '<EmDockingStation>"
  "02e4453bcd60ac3df68a333e1d9e1373")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'EmDockingStation)))
  "Returns md5sum for a message object of type 'EmDockingStation"
  "02e4453bcd60ac3df68a333e1d9e1373")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<EmDockingStation>)))
  "Returns full string definition for message of type '<EmDockingStation>"
  (cl:format cl:nil "int32 id~%float64 x~%float64 y~%bool vacant~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'EmDockingStation)))
  "Returns full string definition for message of type 'EmDockingStation"
  (cl:format cl:nil "int32 id~%float64 x~%float64 y~%bool vacant~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <EmDockingStation>))
  (cl:+ 0
     4
     8
     8
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <EmDockingStation>))
  "Converts a ROS message object to a list"
  (cl:list 'EmDockingStation
    (cl:cons ':id (id msg))
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':vacant (vacant msg))
))
