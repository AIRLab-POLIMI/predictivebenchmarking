; Auto-generated. Do not edit!


(cl:in-package map_merger-srv)


;//! \htmlinclude TransformPoint-request.msg.html

(cl:defclass <TransformPoint-request> (roslisp-msg-protocol:ros-message)
  ((point
    :reader point
    :initarg :point
    :type adhoc_communication-msg:MmPoint
    :initform (cl:make-instance 'adhoc_communication-msg:MmPoint)))
)

(cl:defclass TransformPoint-request (<TransformPoint-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TransformPoint-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TransformPoint-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name map_merger-srv:<TransformPoint-request> is deprecated: use map_merger-srv:TransformPoint-request instead.")))

(cl:ensure-generic-function 'point-val :lambda-list '(m))
(cl:defmethod point-val ((m <TransformPoint-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader map_merger-srv:point-val is deprecated.  Use map_merger-srv:point instead.")
  (point m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TransformPoint-request>) ostream)
  "Serializes a message object of type '<TransformPoint-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'point) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TransformPoint-request>) istream)
  "Deserializes a message object of type '<TransformPoint-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'point) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TransformPoint-request>)))
  "Returns string type for a service object of type '<TransformPoint-request>"
  "map_merger/TransformPointRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TransformPoint-request)))
  "Returns string type for a service object of type 'TransformPoint-request"
  "map_merger/TransformPointRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TransformPoint-request>)))
  "Returns md5sum for a message object of type '<TransformPoint-request>"
  "118b08a194ba8d774bcc2a526a4b8444")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TransformPoint-request)))
  "Returns md5sum for a message object of type 'TransformPoint-request"
  "118b08a194ba8d774bcc2a526a4b8444")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TransformPoint-request>)))
  "Returns full string definition for message of type '<TransformPoint-request>"
  (cl:format cl:nil "adhoc_communication/MmPoint point~%~%================================================================================~%MSG: adhoc_communication/MmPoint~%string src_robot~%float64 x~%float64 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TransformPoint-request)))
  "Returns full string definition for message of type 'TransformPoint-request"
  (cl:format cl:nil "adhoc_communication/MmPoint point~%~%================================================================================~%MSG: adhoc_communication/MmPoint~%string src_robot~%float64 x~%float64 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TransformPoint-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'point))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TransformPoint-request>))
  "Converts a ROS message object to a list"
  (cl:list 'TransformPoint-request
    (cl:cons ':point (point msg))
))
;//! \htmlinclude TransformPoint-response.msg.html

(cl:defclass <TransformPoint-response> (roslisp-msg-protocol:ros-message)
  ((point
    :reader point
    :initarg :point
    :type adhoc_communication-msg:MmPoint
    :initform (cl:make-instance 'adhoc_communication-msg:MmPoint)))
)

(cl:defclass TransformPoint-response (<TransformPoint-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TransformPoint-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TransformPoint-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name map_merger-srv:<TransformPoint-response> is deprecated: use map_merger-srv:TransformPoint-response instead.")))

(cl:ensure-generic-function 'point-val :lambda-list '(m))
(cl:defmethod point-val ((m <TransformPoint-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader map_merger-srv:point-val is deprecated.  Use map_merger-srv:point instead.")
  (point m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TransformPoint-response>) ostream)
  "Serializes a message object of type '<TransformPoint-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'point) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TransformPoint-response>) istream)
  "Deserializes a message object of type '<TransformPoint-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'point) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TransformPoint-response>)))
  "Returns string type for a service object of type '<TransformPoint-response>"
  "map_merger/TransformPointResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TransformPoint-response)))
  "Returns string type for a service object of type 'TransformPoint-response"
  "map_merger/TransformPointResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TransformPoint-response>)))
  "Returns md5sum for a message object of type '<TransformPoint-response>"
  "118b08a194ba8d774bcc2a526a4b8444")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TransformPoint-response)))
  "Returns md5sum for a message object of type 'TransformPoint-response"
  "118b08a194ba8d774bcc2a526a4b8444")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TransformPoint-response>)))
  "Returns full string definition for message of type '<TransformPoint-response>"
  (cl:format cl:nil "adhoc_communication/MmPoint point~%~%~%================================================================================~%MSG: adhoc_communication/MmPoint~%string src_robot~%float64 x~%float64 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TransformPoint-response)))
  "Returns full string definition for message of type 'TransformPoint-response"
  (cl:format cl:nil "adhoc_communication/MmPoint point~%~%~%================================================================================~%MSG: adhoc_communication/MmPoint~%string src_robot~%float64 x~%float64 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TransformPoint-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'point))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TransformPoint-response>))
  "Converts a ROS message object to a list"
  (cl:list 'TransformPoint-response
    (cl:cons ':point (point msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'TransformPoint)))
  'TransformPoint-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'TransformPoint)))
  'TransformPoint-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TransformPoint)))
  "Returns string type for a service object of type '<TransformPoint>"
  "map_merger/TransformPoint")