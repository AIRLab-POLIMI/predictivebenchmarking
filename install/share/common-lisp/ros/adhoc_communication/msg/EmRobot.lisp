; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-msg)


;//! \htmlinclude EmRobot.msg.html

(cl:defclass <EmRobot> (roslisp-msg-protocol:ros-message)
  ((id
    :reader id
    :initarg :id
    :type cl:integer
    :initform 0)
   (state
    :reader state
    :initarg :state
    :type cl:integer
    :initform 0)
   (selected_ds
    :reader selected_ds
    :initarg :selected_ds
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
    :initform 0.0))
)

(cl:defclass EmRobot (<EmRobot>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <EmRobot>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'EmRobot)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-msg:<EmRobot> is deprecated: use adhoc_communication-msg:EmRobot instead.")))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <EmRobot>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:id-val is deprecated.  Use adhoc_communication-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <EmRobot>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:state-val is deprecated.  Use adhoc_communication-msg:state instead.")
  (state m))

(cl:ensure-generic-function 'selected_ds-val :lambda-list '(m))
(cl:defmethod selected_ds-val ((m <EmRobot>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:selected_ds-val is deprecated.  Use adhoc_communication-msg:selected_ds instead.")
  (selected_ds m))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <EmRobot>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:x-val is deprecated.  Use adhoc_communication-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <EmRobot>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:y-val is deprecated.  Use adhoc_communication-msg:y instead.")
  (y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <EmRobot>) ostream)
  "Serializes a message object of type '<EmRobot>"
  (cl:let* ((signed (cl:slot-value msg 'id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'state)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'selected_ds)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <EmRobot>) istream)
  "Deserializes a message object of type '<EmRobot>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'id) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'selected_ds) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<EmRobot>)))
  "Returns string type for a message object of type '<EmRobot>"
  "adhoc_communication/EmRobot")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EmRobot)))
  "Returns string type for a message object of type 'EmRobot"
  "adhoc_communication/EmRobot")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<EmRobot>)))
  "Returns md5sum for a message object of type '<EmRobot>"
  "c8b0953d68d06c5193efb226a802f624")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'EmRobot)))
  "Returns md5sum for a message object of type 'EmRobot"
  "c8b0953d68d06c5193efb226a802f624")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<EmRobot>)))
  "Returns full string definition for message of type '<EmRobot>"
  (cl:format cl:nil "int32 id~%int32 state # see energy_mgmt/docking.h~%int32 selected_ds #the id of the docking stationc currelty selected by the robot to recharge~%float32 x    #robot x-coordinate (in the reference system of the sending robot, not in the one of the receiver)~%float32 y    #robot y-coordinate (in the reference system of the sending robot, not in the one of the receiver)~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'EmRobot)))
  "Returns full string definition for message of type 'EmRobot"
  (cl:format cl:nil "int32 id~%int32 state # see energy_mgmt/docking.h~%int32 selected_ds #the id of the docking stationc currelty selected by the robot to recharge~%float32 x    #robot x-coordinate (in the reference system of the sending robot, not in the one of the receiver)~%float32 y    #robot y-coordinate (in the reference system of the sending robot, not in the one of the receiver)~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <EmRobot>))
  (cl:+ 0
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <EmRobot>))
  "Converts a ROS message object to a list"
  (cl:list 'EmRobot
    (cl:cons ':id (id msg))
    (cl:cons ':state (state msg))
    (cl:cons ':selected_ds (selected_ds msg))
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
))
