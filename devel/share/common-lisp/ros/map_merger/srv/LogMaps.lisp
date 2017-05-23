; Auto-generated. Do not edit!


(cl:in-package map_merger-srv)


;//! \htmlinclude LogMaps-request.msg.html

(cl:defclass <LogMaps-request> (roslisp-msg-protocol:ros-message)
  ((log
    :reader log
    :initarg :log
    :type cl:fixnum
    :initform 0))
)

(cl:defclass LogMaps-request (<LogMaps-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LogMaps-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LogMaps-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name map_merger-srv:<LogMaps-request> is deprecated: use map_merger-srv:LogMaps-request instead.")))

(cl:ensure-generic-function 'log-val :lambda-list '(m))
(cl:defmethod log-val ((m <LogMaps-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader map_merger-srv:log-val is deprecated.  Use map_merger-srv:log instead.")
  (log m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LogMaps-request>) ostream)
  "Serializes a message object of type '<LogMaps-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'log)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'log)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LogMaps-request>) istream)
  "Deserializes a message object of type '<LogMaps-request>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'log)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'log)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LogMaps-request>)))
  "Returns string type for a service object of type '<LogMaps-request>"
  "map_merger/LogMapsRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LogMaps-request)))
  "Returns string type for a service object of type 'LogMaps-request"
  "map_merger/LogMapsRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LogMaps-request>)))
  "Returns md5sum for a message object of type '<LogMaps-request>"
  "bb54d185c1070cbf70d4cfb2996c18fd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LogMaps-request)))
  "Returns md5sum for a message object of type 'LogMaps-request"
  "bb54d185c1070cbf70d4cfb2996c18fd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LogMaps-request>)))
  "Returns full string definition for message of type '<LogMaps-request>"
  (cl:format cl:nil "uint16 log~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LogMaps-request)))
  "Returns full string definition for message of type 'LogMaps-request"
  (cl:format cl:nil "uint16 log~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LogMaps-request>))
  (cl:+ 0
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LogMaps-request>))
  "Converts a ROS message object to a list"
  (cl:list 'LogMaps-request
    (cl:cons ':log (log msg))
))
;//! \htmlinclude LogMaps-response.msg.html

(cl:defclass <LogMaps-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass LogMaps-response (<LogMaps-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LogMaps-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LogMaps-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name map_merger-srv:<LogMaps-response> is deprecated: use map_merger-srv:LogMaps-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LogMaps-response>) ostream)
  "Serializes a message object of type '<LogMaps-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LogMaps-response>) istream)
  "Deserializes a message object of type '<LogMaps-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LogMaps-response>)))
  "Returns string type for a service object of type '<LogMaps-response>"
  "map_merger/LogMapsResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LogMaps-response)))
  "Returns string type for a service object of type 'LogMaps-response"
  "map_merger/LogMapsResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LogMaps-response>)))
  "Returns md5sum for a message object of type '<LogMaps-response>"
  "bb54d185c1070cbf70d4cfb2996c18fd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LogMaps-response)))
  "Returns md5sum for a message object of type 'LogMaps-response"
  "bb54d185c1070cbf70d4cfb2996c18fd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LogMaps-response>)))
  "Returns full string definition for message of type '<LogMaps-response>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LogMaps-response)))
  "Returns full string definition for message of type 'LogMaps-response"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LogMaps-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LogMaps-response>))
  "Converts a ROS message object to a list"
  (cl:list 'LogMaps-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'LogMaps)))
  'LogMaps-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'LogMaps)))
  'LogMaps-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LogMaps)))
  "Returns string type for a service object of type '<LogMaps>"
  "map_merger/LogMaps")