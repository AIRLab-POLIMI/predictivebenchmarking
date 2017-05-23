; Auto-generated. Do not edit!


(cl:in-package energy_mgmt-msg)


;//! \htmlinclude battery_state.msg.html

(cl:defclass <battery_state> (roslisp-msg-protocol:ros-message)
  ((charging
    :reader charging
    :initarg :charging
    :type cl:boolean
    :initform cl:nil)
   (soc
    :reader soc
    :initarg :soc
    :type cl:float
    :initform 0.0)
   (remaining_time_charge
    :reader remaining_time_charge
    :initarg :remaining_time_charge
    :type cl:float
    :initform 0.0)
   (remaining_time_run
    :reader remaining_time_run
    :initarg :remaining_time_run
    :type cl:float
    :initform 0.0)
   (remaining_distance
    :reader remaining_distance
    :initarg :remaining_distance
    :type cl:float
    :initform 0.0))
)

(cl:defclass battery_state (<battery_state>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <battery_state>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'battery_state)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name energy_mgmt-msg:<battery_state> is deprecated: use energy_mgmt-msg:battery_state instead.")))

(cl:ensure-generic-function 'charging-val :lambda-list '(m))
(cl:defmethod charging-val ((m <battery_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader energy_mgmt-msg:charging-val is deprecated.  Use energy_mgmt-msg:charging instead.")
  (charging m))

(cl:ensure-generic-function 'soc-val :lambda-list '(m))
(cl:defmethod soc-val ((m <battery_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader energy_mgmt-msg:soc-val is deprecated.  Use energy_mgmt-msg:soc instead.")
  (soc m))

(cl:ensure-generic-function 'remaining_time_charge-val :lambda-list '(m))
(cl:defmethod remaining_time_charge-val ((m <battery_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader energy_mgmt-msg:remaining_time_charge-val is deprecated.  Use energy_mgmt-msg:remaining_time_charge instead.")
  (remaining_time_charge m))

(cl:ensure-generic-function 'remaining_time_run-val :lambda-list '(m))
(cl:defmethod remaining_time_run-val ((m <battery_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader energy_mgmt-msg:remaining_time_run-val is deprecated.  Use energy_mgmt-msg:remaining_time_run instead.")
  (remaining_time_run m))

(cl:ensure-generic-function 'remaining_distance-val :lambda-list '(m))
(cl:defmethod remaining_distance-val ((m <battery_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader energy_mgmt-msg:remaining_distance-val is deprecated.  Use energy_mgmt-msg:remaining_distance instead.")
  (remaining_distance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <battery_state>) ostream)
  "Serializes a message object of type '<battery_state>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'charging) 1 0)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'soc))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'remaining_time_charge))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'remaining_time_run))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'remaining_distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <battery_state>) istream)
  "Deserializes a message object of type '<battery_state>"
    (cl:setf (cl:slot-value msg 'charging) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'soc) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'remaining_time_charge) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'remaining_time_run) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'remaining_distance) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<battery_state>)))
  "Returns string type for a message object of type '<battery_state>"
  "energy_mgmt/battery_state")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'battery_state)))
  "Returns string type for a message object of type 'battery_state"
  "energy_mgmt/battery_state")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<battery_state>)))
  "Returns md5sum for a message object of type '<battery_state>"
  "ae34ca1536c302c535b231631ea2d4bc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'battery_state)))
  "Returns md5sum for a message object of type 'battery_state"
  "ae34ca1536c302c535b231631ea2d4bc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<battery_state>)))
  "Returns full string definition for message of type '<battery_state>"
  (cl:format cl:nil "bool charging~%float32 soc~%float32 remaining_time_charge~%float32 remaining_time_run~%float32 remaining_distance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'battery_state)))
  "Returns full string definition for message of type 'battery_state"
  (cl:format cl:nil "bool charging~%float32 soc~%float32 remaining_time_charge~%float32 remaining_time_run~%float32 remaining_distance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <battery_state>))
  (cl:+ 0
     1
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <battery_state>))
  "Converts a ROS message object to a list"
  (cl:list 'battery_state
    (cl:cons ':charging (charging msg))
    (cl:cons ':soc (soc msg))
    (cl:cons ':remaining_time_charge (remaining_time_charge msg))
    (cl:cons ':remaining_time_run (remaining_time_run msg))
    (cl:cons ':remaining_distance (remaining_distance msg))
))
