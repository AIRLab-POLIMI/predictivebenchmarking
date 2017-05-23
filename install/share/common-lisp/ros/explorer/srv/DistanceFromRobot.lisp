; Auto-generated. Do not edit!


(cl:in-package explorer-srv)


;//! \htmlinclude DistanceFromRobot-request.msg.html

(cl:defclass <DistanceFromRobot-request> (roslisp-msg-protocol:ros-message)
  ((x
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

(cl:defclass DistanceFromRobot-request (<DistanceFromRobot-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DistanceFromRobot-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DistanceFromRobot-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name explorer-srv:<DistanceFromRobot-request> is deprecated: use explorer-srv:DistanceFromRobot-request instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <DistanceFromRobot-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader explorer-srv:x-val is deprecated.  Use explorer-srv:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <DistanceFromRobot-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader explorer-srv:y-val is deprecated.  Use explorer-srv:y instead.")
  (y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DistanceFromRobot-request>) ostream)
  "Serializes a message object of type '<DistanceFromRobot-request>"
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DistanceFromRobot-request>) istream)
  "Deserializes a message object of type '<DistanceFromRobot-request>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DistanceFromRobot-request>)))
  "Returns string type for a service object of type '<DistanceFromRobot-request>"
  "explorer/DistanceFromRobotRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DistanceFromRobot-request)))
  "Returns string type for a service object of type 'DistanceFromRobot-request"
  "explorer/DistanceFromRobotRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DistanceFromRobot-request>)))
  "Returns md5sum for a message object of type '<DistanceFromRobot-request>"
  "fcc6a54f128d10ae4d19b273bb4c2682")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DistanceFromRobot-request)))
  "Returns md5sum for a message object of type 'DistanceFromRobot-request"
  "fcc6a54f128d10ae4d19b273bb4c2682")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DistanceFromRobot-request>)))
  "Returns full string definition for message of type '<DistanceFromRobot-request>"
  (cl:format cl:nil "float32 x~%float32 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DistanceFromRobot-request)))
  "Returns full string definition for message of type 'DistanceFromRobot-request"
  (cl:format cl:nil "float32 x~%float32 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DistanceFromRobot-request>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DistanceFromRobot-request>))
  "Converts a ROS message object to a list"
  (cl:list 'DistanceFromRobot-request
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
))
;//! \htmlinclude DistanceFromRobot-response.msg.html

(cl:defclass <DistanceFromRobot-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0)
   (reachable
    :reader reachable
    :initarg :reachable
    :type cl:fixnum
    :initform 0)
   (distance
    :reader distance
    :initarg :distance
    :type cl:float
    :initform 0.0))
)

(cl:defclass DistanceFromRobot-response (<DistanceFromRobot-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DistanceFromRobot-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DistanceFromRobot-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name explorer-srv:<DistanceFromRobot-response> is deprecated: use explorer-srv:DistanceFromRobot-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <DistanceFromRobot-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader explorer-srv:status-val is deprecated.  Use explorer-srv:status instead.")
  (status m))

(cl:ensure-generic-function 'reachable-val :lambda-list '(m))
(cl:defmethod reachable-val ((m <DistanceFromRobot-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader explorer-srv:reachable-val is deprecated.  Use explorer-srv:reachable instead.")
  (reachable m))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <DistanceFromRobot-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader explorer-srv:distance-val is deprecated.  Use explorer-srv:distance instead.")
  (distance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DistanceFromRobot-response>) ostream)
  "Serializes a message object of type '<DistanceFromRobot-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'reachable)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DistanceFromRobot-response>) istream)
  "Deserializes a message object of type '<DistanceFromRobot-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'reachable)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distance) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DistanceFromRobot-response>)))
  "Returns string type for a service object of type '<DistanceFromRobot-response>"
  "explorer/DistanceFromRobotResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DistanceFromRobot-response)))
  "Returns string type for a service object of type 'DistanceFromRobot-response"
  "explorer/DistanceFromRobotResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DistanceFromRobot-response>)))
  "Returns md5sum for a message object of type '<DistanceFromRobot-response>"
  "fcc6a54f128d10ae4d19b273bb4c2682")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DistanceFromRobot-response)))
  "Returns md5sum for a message object of type 'DistanceFromRobot-response"
  "fcc6a54f128d10ae4d19b273bb4c2682")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DistanceFromRobot-response>)))
  "Returns full string definition for message of type '<DistanceFromRobot-response>"
  (cl:format cl:nil "uint8 status~%uint8 reachable~%float32 distance~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DistanceFromRobot-response)))
  "Returns full string definition for message of type 'DistanceFromRobot-response"
  (cl:format cl:nil "uint8 status~%uint8 reachable~%float32 distance~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DistanceFromRobot-response>))
  (cl:+ 0
     1
     1
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DistanceFromRobot-response>))
  "Converts a ROS message object to a list"
  (cl:list 'DistanceFromRobot-response
    (cl:cons ':status (status msg))
    (cl:cons ':reachable (reachable msg))
    (cl:cons ':distance (distance msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'DistanceFromRobot)))
  'DistanceFromRobot-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'DistanceFromRobot)))
  'DistanceFromRobot-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DistanceFromRobot)))
  "Returns string type for a service object of type '<DistanceFromRobot>"
  "explorer/DistanceFromRobot")