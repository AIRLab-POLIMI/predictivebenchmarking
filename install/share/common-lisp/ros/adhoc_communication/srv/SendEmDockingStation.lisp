; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude SendEmDockingStation-request.msg.html

(cl:defclass <SendEmDockingStation-request> (roslisp-msg-protocol:ros-message)
  ((topic
    :reader topic
    :initarg :topic
    :type cl:string
    :initform "")
   (dst_robot
    :reader dst_robot
    :initarg :dst_robot
    :type cl:string
    :initform "")
   (docking_station
    :reader docking_station
    :initarg :docking_station
    :type adhoc_communication-msg:EmDockingStation
    :initform (cl:make-instance 'adhoc_communication-msg:EmDockingStation)))
)

(cl:defclass SendEmDockingStation-request (<SendEmDockingStation-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendEmDockingStation-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendEmDockingStation-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendEmDockingStation-request> is deprecated: use adhoc_communication-srv:SendEmDockingStation-request instead.")))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <SendEmDockingStation-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:topic-val is deprecated.  Use adhoc_communication-srv:topic instead.")
  (topic m))

(cl:ensure-generic-function 'dst_robot-val :lambda-list '(m))
(cl:defmethod dst_robot-val ((m <SendEmDockingStation-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:dst_robot-val is deprecated.  Use adhoc_communication-srv:dst_robot instead.")
  (dst_robot m))

(cl:ensure-generic-function 'docking_station-val :lambda-list '(m))
(cl:defmethod docking_station-val ((m <SendEmDockingStation-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:docking_station-val is deprecated.  Use adhoc_communication-srv:docking_station instead.")
  (docking_station m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendEmDockingStation-request>) ostream)
  "Serializes a message object of type '<SendEmDockingStation-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'topic))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'topic))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'dst_robot))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'dst_robot))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'docking_station) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendEmDockingStation-request>) istream)
  "Deserializes a message object of type '<SendEmDockingStation-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'topic) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'topic) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'dst_robot) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'dst_robot) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'docking_station) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendEmDockingStation-request>)))
  "Returns string type for a service object of type '<SendEmDockingStation-request>"
  "adhoc_communication/SendEmDockingStationRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendEmDockingStation-request)))
  "Returns string type for a service object of type 'SendEmDockingStation-request"
  "adhoc_communication/SendEmDockingStationRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendEmDockingStation-request>)))
  "Returns md5sum for a message object of type '<SendEmDockingStation-request>"
  "8f86c3f7e9c77062fc3c620d3c267397")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendEmDockingStation-request)))
  "Returns md5sum for a message object of type 'SendEmDockingStation-request"
  "8f86c3f7e9c77062fc3c620d3c267397")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendEmDockingStation-request>)))
  "Returns full string definition for message of type '<SendEmDockingStation-request>"
  (cl:format cl:nil "string topic~%string dst_robot~%adhoc_communication/EmDockingStation docking_station~%~%================================================================================~%MSG: adhoc_communication/EmDockingStation~%int32 id~%float64 x~%float64 y~%bool vacant~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendEmDockingStation-request)))
  "Returns full string definition for message of type 'SendEmDockingStation-request"
  (cl:format cl:nil "string topic~%string dst_robot~%adhoc_communication/EmDockingStation docking_station~%~%================================================================================~%MSG: adhoc_communication/EmDockingStation~%int32 id~%float64 x~%float64 y~%bool vacant~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendEmDockingStation-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'topic))
     4 (cl:length (cl:slot-value msg 'dst_robot))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'docking_station))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendEmDockingStation-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SendEmDockingStation-request
    (cl:cons ':topic (topic msg))
    (cl:cons ':dst_robot (dst_robot msg))
    (cl:cons ':docking_station (docking_station msg))
))
;//! \htmlinclude SendEmDockingStation-response.msg.html

(cl:defclass <SendEmDockingStation-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SendEmDockingStation-response (<SendEmDockingStation-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendEmDockingStation-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendEmDockingStation-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendEmDockingStation-response> is deprecated: use adhoc_communication-srv:SendEmDockingStation-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <SendEmDockingStation-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:status-val is deprecated.  Use adhoc_communication-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendEmDockingStation-response>) ostream)
  "Serializes a message object of type '<SendEmDockingStation-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendEmDockingStation-response>) istream)
  "Deserializes a message object of type '<SendEmDockingStation-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendEmDockingStation-response>)))
  "Returns string type for a service object of type '<SendEmDockingStation-response>"
  "adhoc_communication/SendEmDockingStationResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendEmDockingStation-response)))
  "Returns string type for a service object of type 'SendEmDockingStation-response"
  "adhoc_communication/SendEmDockingStationResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendEmDockingStation-response>)))
  "Returns md5sum for a message object of type '<SendEmDockingStation-response>"
  "8f86c3f7e9c77062fc3c620d3c267397")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendEmDockingStation-response)))
  "Returns md5sum for a message object of type 'SendEmDockingStation-response"
  "8f86c3f7e9c77062fc3c620d3c267397")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendEmDockingStation-response>)))
  "Returns full string definition for message of type '<SendEmDockingStation-response>"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendEmDockingStation-response)))
  "Returns full string definition for message of type 'SendEmDockingStation-response"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendEmDockingStation-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendEmDockingStation-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SendEmDockingStation-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SendEmDockingStation)))
  'SendEmDockingStation-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SendEmDockingStation)))
  'SendEmDockingStation-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendEmDockingStation)))
  "Returns string type for a service object of type '<SendEmDockingStation>"
  "adhoc_communication/SendEmDockingStation")