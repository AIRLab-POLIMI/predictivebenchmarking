; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-msg)


;//! \htmlinclude EmAuction.msg.html

(cl:defclass <EmAuction> (roslisp-msg-protocol:ros-message)
  ((auction
    :reader auction
    :initarg :auction
    :type cl:integer
    :initform 0)
   (robot
    :reader robot
    :initarg :robot
    :type cl:integer
    :initform 0)
   (docking_station
    :reader docking_station
    :initarg :docking_station
    :type cl:integer
    :initform 0)
   (bid
    :reader bid
    :initarg :bid
    :type cl:float
    :initform 0.0))
)

(cl:defclass EmAuction (<EmAuction>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <EmAuction>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'EmAuction)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-msg:<EmAuction> is deprecated: use adhoc_communication-msg:EmAuction instead.")))

(cl:ensure-generic-function 'auction-val :lambda-list '(m))
(cl:defmethod auction-val ((m <EmAuction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:auction-val is deprecated.  Use adhoc_communication-msg:auction instead.")
  (auction m))

(cl:ensure-generic-function 'robot-val :lambda-list '(m))
(cl:defmethod robot-val ((m <EmAuction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:robot-val is deprecated.  Use adhoc_communication-msg:robot instead.")
  (robot m))

(cl:ensure-generic-function 'docking_station-val :lambda-list '(m))
(cl:defmethod docking_station-val ((m <EmAuction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:docking_station-val is deprecated.  Use adhoc_communication-msg:docking_station instead.")
  (docking_station m))

(cl:ensure-generic-function 'bid-val :lambda-list '(m))
(cl:defmethod bid-val ((m <EmAuction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:bid-val is deprecated.  Use adhoc_communication-msg:bid instead.")
  (bid m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <EmAuction>) ostream)
  "Serializes a message object of type '<EmAuction>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'auction)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'auction)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'auction)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'auction)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'robot)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'robot)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'robot)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'robot)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'docking_station)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'docking_station)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'docking_station)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'docking_station)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'bid))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <EmAuction>) istream)
  "Deserializes a message object of type '<EmAuction>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'auction)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'auction)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'auction)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'auction)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'robot)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'robot)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'robot)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'robot)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'docking_station)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'docking_station)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'docking_station)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'docking_station)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'bid) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<EmAuction>)))
  "Returns string type for a message object of type '<EmAuction>"
  "adhoc_communication/EmAuction")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EmAuction)))
  "Returns string type for a message object of type 'EmAuction"
  "adhoc_communication/EmAuction")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<EmAuction>)))
  "Returns md5sum for a message object of type '<EmAuction>"
  "942c2474214e04f260e8c0832e6a1dad")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'EmAuction)))
  "Returns md5sum for a message object of type 'EmAuction"
  "942c2474214e04f260e8c0832e6a1dad")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<EmAuction>)))
  "Returns full string definition for message of type '<EmAuction>"
  (cl:format cl:nil "uint32 auction~%uint32 robot~%uint32 docking_station~%float32 bid~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'EmAuction)))
  "Returns full string definition for message of type 'EmAuction"
  (cl:format cl:nil "uint32 auction~%uint32 robot~%uint32 docking_station~%float32 bid~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <EmAuction>))
  (cl:+ 0
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <EmAuction>))
  "Converts a ROS message object to a list"
  (cl:list 'EmAuction
    (cl:cons ':auction (auction msg))
    (cl:cons ':robot (robot msg))
    (cl:cons ':docking_station (docking_station msg))
    (cl:cons ':bid (bid msg))
))
