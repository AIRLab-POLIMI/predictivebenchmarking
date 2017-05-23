; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude BroadcastCMgrRobotUpdate-request.msg.html

(cl:defclass <BroadcastCMgrRobotUpdate-request> (roslisp-msg-protocol:ros-message)
  ((topic
    :reader topic
    :initarg :topic
    :type cl:string
    :initform "")
   (update
    :reader update
    :initarg :update
    :type adhoc_communication-msg:CMgrRobotUpdate
    :initform (cl:make-instance 'adhoc_communication-msg:CMgrRobotUpdate))
   (hop_limit
    :reader hop_limit
    :initarg :hop_limit
    :type cl:fixnum
    :initform 0))
)

(cl:defclass BroadcastCMgrRobotUpdate-request (<BroadcastCMgrRobotUpdate-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BroadcastCMgrRobotUpdate-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BroadcastCMgrRobotUpdate-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<BroadcastCMgrRobotUpdate-request> is deprecated: use adhoc_communication-srv:BroadcastCMgrRobotUpdate-request instead.")))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <BroadcastCMgrRobotUpdate-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:topic-val is deprecated.  Use adhoc_communication-srv:topic instead.")
  (topic m))

(cl:ensure-generic-function 'update-val :lambda-list '(m))
(cl:defmethod update-val ((m <BroadcastCMgrRobotUpdate-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:update-val is deprecated.  Use adhoc_communication-srv:update instead.")
  (update m))

(cl:ensure-generic-function 'hop_limit-val :lambda-list '(m))
(cl:defmethod hop_limit-val ((m <BroadcastCMgrRobotUpdate-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:hop_limit-val is deprecated.  Use adhoc_communication-srv:hop_limit instead.")
  (hop_limit m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BroadcastCMgrRobotUpdate-request>) ostream)
  "Serializes a message object of type '<BroadcastCMgrRobotUpdate-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'topic))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'topic))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'update) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'hop_limit)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BroadcastCMgrRobotUpdate-request>) istream)
  "Deserializes a message object of type '<BroadcastCMgrRobotUpdate-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'topic) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'topic) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'update) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'hop_limit)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BroadcastCMgrRobotUpdate-request>)))
  "Returns string type for a service object of type '<BroadcastCMgrRobotUpdate-request>"
  "adhoc_communication/BroadcastCMgrRobotUpdateRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BroadcastCMgrRobotUpdate-request)))
  "Returns string type for a service object of type 'BroadcastCMgrRobotUpdate-request"
  "adhoc_communication/BroadcastCMgrRobotUpdateRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BroadcastCMgrRobotUpdate-request>)))
  "Returns md5sum for a message object of type '<BroadcastCMgrRobotUpdate-request>"
  "4f803d834e6e3f0165ecc26babd1f3f1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BroadcastCMgrRobotUpdate-request)))
  "Returns md5sum for a message object of type 'BroadcastCMgrRobotUpdate-request"
  "4f803d834e6e3f0165ecc26babd1f3f1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BroadcastCMgrRobotUpdate-request>)))
  "Returns full string definition for message of type '<BroadcastCMgrRobotUpdate-request>"
  (cl:format cl:nil "string topic~%adhoc_communication/CMgrRobotUpdate update~%uint8 hop_limit~%~%================================================================================~%MSG: adhoc_communication/CMgrRobotUpdate~%string robot_name~%string capabilities~%float32 energy~%adhoc_communication/CMgrDimensions dimensions~%string status~%string[] neighbors~%~%================================================================================~%MSG: adhoc_communication/CMgrDimensions~%float32 x~%float32 y~%float32 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BroadcastCMgrRobotUpdate-request)))
  "Returns full string definition for message of type 'BroadcastCMgrRobotUpdate-request"
  (cl:format cl:nil "string topic~%adhoc_communication/CMgrRobotUpdate update~%uint8 hop_limit~%~%================================================================================~%MSG: adhoc_communication/CMgrRobotUpdate~%string robot_name~%string capabilities~%float32 energy~%adhoc_communication/CMgrDimensions dimensions~%string status~%string[] neighbors~%~%================================================================================~%MSG: adhoc_communication/CMgrDimensions~%float32 x~%float32 y~%float32 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BroadcastCMgrRobotUpdate-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'topic))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'update))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BroadcastCMgrRobotUpdate-request>))
  "Converts a ROS message object to a list"
  (cl:list 'BroadcastCMgrRobotUpdate-request
    (cl:cons ':topic (topic msg))
    (cl:cons ':update (update msg))
    (cl:cons ':hop_limit (hop_limit msg))
))
;//! \htmlinclude BroadcastCMgrRobotUpdate-response.msg.html

(cl:defclass <BroadcastCMgrRobotUpdate-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass BroadcastCMgrRobotUpdate-response (<BroadcastCMgrRobotUpdate-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BroadcastCMgrRobotUpdate-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BroadcastCMgrRobotUpdate-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<BroadcastCMgrRobotUpdate-response> is deprecated: use adhoc_communication-srv:BroadcastCMgrRobotUpdate-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <BroadcastCMgrRobotUpdate-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:status-val is deprecated.  Use adhoc_communication-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BroadcastCMgrRobotUpdate-response>) ostream)
  "Serializes a message object of type '<BroadcastCMgrRobotUpdate-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BroadcastCMgrRobotUpdate-response>) istream)
  "Deserializes a message object of type '<BroadcastCMgrRobotUpdate-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BroadcastCMgrRobotUpdate-response>)))
  "Returns string type for a service object of type '<BroadcastCMgrRobotUpdate-response>"
  "adhoc_communication/BroadcastCMgrRobotUpdateResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BroadcastCMgrRobotUpdate-response)))
  "Returns string type for a service object of type 'BroadcastCMgrRobotUpdate-response"
  "adhoc_communication/BroadcastCMgrRobotUpdateResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BroadcastCMgrRobotUpdate-response>)))
  "Returns md5sum for a message object of type '<BroadcastCMgrRobotUpdate-response>"
  "4f803d834e6e3f0165ecc26babd1f3f1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BroadcastCMgrRobotUpdate-response)))
  "Returns md5sum for a message object of type 'BroadcastCMgrRobotUpdate-response"
  "4f803d834e6e3f0165ecc26babd1f3f1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BroadcastCMgrRobotUpdate-response>)))
  "Returns full string definition for message of type '<BroadcastCMgrRobotUpdate-response>"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BroadcastCMgrRobotUpdate-response)))
  "Returns full string definition for message of type 'BroadcastCMgrRobotUpdate-response"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BroadcastCMgrRobotUpdate-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BroadcastCMgrRobotUpdate-response>))
  "Converts a ROS message object to a list"
  (cl:list 'BroadcastCMgrRobotUpdate-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'BroadcastCMgrRobotUpdate)))
  'BroadcastCMgrRobotUpdate-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'BroadcastCMgrRobotUpdate)))
  'BroadcastCMgrRobotUpdate-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BroadcastCMgrRobotUpdate)))
  "Returns string type for a service object of type '<BroadcastCMgrRobotUpdate>"
  "adhoc_communication/BroadcastCMgrRobotUpdate")