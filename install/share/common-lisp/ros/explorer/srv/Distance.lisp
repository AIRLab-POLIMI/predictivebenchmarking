; Auto-generated. Do not edit!


(cl:in-package explorer-srv)


;//! \htmlinclude Distance-request.msg.html

(cl:defclass <Distance-request> (roslisp-msg-protocol:ros-message)
  ((x1
    :reader x1
    :initarg :x1
    :type cl:float
    :initform 0.0)
   (y1
    :reader y1
    :initarg :y1
    :type cl:float
    :initform 0.0)
   (x2
    :reader x2
    :initarg :x2
    :type cl:float
    :initform 0.0)
   (y2
    :reader y2
    :initarg :y2
    :type cl:float
    :initform 0.0))
)

(cl:defclass Distance-request (<Distance-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Distance-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Distance-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name explorer-srv:<Distance-request> is deprecated: use explorer-srv:Distance-request instead.")))

(cl:ensure-generic-function 'x1-val :lambda-list '(m))
(cl:defmethod x1-val ((m <Distance-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader explorer-srv:x1-val is deprecated.  Use explorer-srv:x1 instead.")
  (x1 m))

(cl:ensure-generic-function 'y1-val :lambda-list '(m))
(cl:defmethod y1-val ((m <Distance-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader explorer-srv:y1-val is deprecated.  Use explorer-srv:y1 instead.")
  (y1 m))

(cl:ensure-generic-function 'x2-val :lambda-list '(m))
(cl:defmethod x2-val ((m <Distance-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader explorer-srv:x2-val is deprecated.  Use explorer-srv:x2 instead.")
  (x2 m))

(cl:ensure-generic-function 'y2-val :lambda-list '(m))
(cl:defmethod y2-val ((m <Distance-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader explorer-srv:y2-val is deprecated.  Use explorer-srv:y2 instead.")
  (y2 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Distance-request>) ostream)
  "Serializes a message object of type '<Distance-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Distance-request>) istream)
  "Deserializes a message object of type '<Distance-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x1) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y1) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x2) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y2) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Distance-request>)))
  "Returns string type for a service object of type '<Distance-request>"
  "explorer/DistanceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Distance-request)))
  "Returns string type for a service object of type 'Distance-request"
  "explorer/DistanceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Distance-request>)))
  "Returns md5sum for a message object of type '<Distance-request>"
  "a709d085eafc08a7a947afad7963fe2c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Distance-request)))
  "Returns md5sum for a message object of type 'Distance-request"
  "a709d085eafc08a7a947afad7963fe2c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Distance-request>)))
  "Returns full string definition for message of type '<Distance-request>"
  (cl:format cl:nil "float32 x1~%float32 y1~%float32 x2~%float32 y2~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Distance-request)))
  "Returns full string definition for message of type 'Distance-request"
  (cl:format cl:nil "float32 x1~%float32 y1~%float32 x2~%float32 y2~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Distance-request>))
  (cl:+ 0
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Distance-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Distance-request
    (cl:cons ':x1 (x1 msg))
    (cl:cons ':y1 (y1 msg))
    (cl:cons ':x2 (x2 msg))
    (cl:cons ':y2 (y2 msg))
))
;//! \htmlinclude Distance-response.msg.html

(cl:defclass <Distance-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0)
   (distance
    :reader distance
    :initarg :distance
    :type cl:float
    :initform 0.0))
)

(cl:defclass Distance-response (<Distance-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Distance-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Distance-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name explorer-srv:<Distance-response> is deprecated: use explorer-srv:Distance-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <Distance-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader explorer-srv:status-val is deprecated.  Use explorer-srv:status instead.")
  (status m))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <Distance-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader explorer-srv:distance-val is deprecated.  Use explorer-srv:distance instead.")
  (distance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Distance-response>) ostream)
  "Serializes a message object of type '<Distance-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Distance-response>) istream)
  "Deserializes a message object of type '<Distance-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distance) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Distance-response>)))
  "Returns string type for a service object of type '<Distance-response>"
  "explorer/DistanceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Distance-response)))
  "Returns string type for a service object of type 'Distance-response"
  "explorer/DistanceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Distance-response>)))
  "Returns md5sum for a message object of type '<Distance-response>"
  "a709d085eafc08a7a947afad7963fe2c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Distance-response)))
  "Returns md5sum for a message object of type 'Distance-response"
  "a709d085eafc08a7a947afad7963fe2c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Distance-response>)))
  "Returns full string definition for message of type '<Distance-response>"
  (cl:format cl:nil "uint8 status~%float32 distance~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Distance-response)))
  "Returns full string definition for message of type 'Distance-response"
  (cl:format cl:nil "uint8 status~%float32 distance~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Distance-response>))
  (cl:+ 0
     1
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Distance-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Distance-response
    (cl:cons ':status (status msg))
    (cl:cons ':distance (distance msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Distance)))
  'Distance-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Distance)))
  'Distance-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Distance)))
  "Returns string type for a service object of type '<Distance>"
  "explorer/Distance")