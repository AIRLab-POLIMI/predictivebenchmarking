; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude ShutDown-request.msg.html

(cl:defclass <ShutDown-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass ShutDown-request (<ShutDown-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ShutDown-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ShutDown-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<ShutDown-request> is deprecated: use adhoc_communication-srv:ShutDown-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ShutDown-request>) ostream)
  "Serializes a message object of type '<ShutDown-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ShutDown-request>) istream)
  "Deserializes a message object of type '<ShutDown-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ShutDown-request>)))
  "Returns string type for a service object of type '<ShutDown-request>"
  "adhoc_communication/ShutDownRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ShutDown-request)))
  "Returns string type for a service object of type 'ShutDown-request"
  "adhoc_communication/ShutDownRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ShutDown-request>)))
  "Returns md5sum for a message object of type '<ShutDown-request>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ShutDown-request)))
  "Returns md5sum for a message object of type 'ShutDown-request"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ShutDown-request>)))
  "Returns full string definition for message of type '<ShutDown-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ShutDown-request)))
  "Returns full string definition for message of type 'ShutDown-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ShutDown-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ShutDown-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ShutDown-request
))
;//! \htmlinclude ShutDown-response.msg.html

(cl:defclass <ShutDown-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass ShutDown-response (<ShutDown-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ShutDown-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ShutDown-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<ShutDown-response> is deprecated: use adhoc_communication-srv:ShutDown-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ShutDown-response>) ostream)
  "Serializes a message object of type '<ShutDown-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ShutDown-response>) istream)
  "Deserializes a message object of type '<ShutDown-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ShutDown-response>)))
  "Returns string type for a service object of type '<ShutDown-response>"
  "adhoc_communication/ShutDownResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ShutDown-response)))
  "Returns string type for a service object of type 'ShutDown-response"
  "adhoc_communication/ShutDownResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ShutDown-response>)))
  "Returns md5sum for a message object of type '<ShutDown-response>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ShutDown-response)))
  "Returns md5sum for a message object of type 'ShutDown-response"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ShutDown-response>)))
  "Returns full string definition for message of type '<ShutDown-response>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ShutDown-response)))
  "Returns full string definition for message of type 'ShutDown-response"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ShutDown-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ShutDown-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ShutDown-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ShutDown)))
  'ShutDown-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ShutDown)))
  'ShutDown-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ShutDown)))
  "Returns string type for a service object of type '<ShutDown>"
  "adhoc_communication/ShutDown")