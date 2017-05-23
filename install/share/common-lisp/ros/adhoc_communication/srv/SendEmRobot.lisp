; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude SendEmRobot-request.msg.html

(cl:defclass <SendEmRobot-request> (roslisp-msg-protocol:ros-message)
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
   (robot
    :reader robot
    :initarg :robot
    :type adhoc_communication-msg:EmRobot
    :initform (cl:make-instance 'adhoc_communication-msg:EmRobot)))
)

(cl:defclass SendEmRobot-request (<SendEmRobot-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendEmRobot-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendEmRobot-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendEmRobot-request> is deprecated: use adhoc_communication-srv:SendEmRobot-request instead.")))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <SendEmRobot-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:topic-val is deprecated.  Use adhoc_communication-srv:topic instead.")
  (topic m))

(cl:ensure-generic-function 'dst_robot-val :lambda-list '(m))
(cl:defmethod dst_robot-val ((m <SendEmRobot-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:dst_robot-val is deprecated.  Use adhoc_communication-srv:dst_robot instead.")
  (dst_robot m))

(cl:ensure-generic-function 'robot-val :lambda-list '(m))
(cl:defmethod robot-val ((m <SendEmRobot-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:robot-val is deprecated.  Use adhoc_communication-srv:robot instead.")
  (robot m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendEmRobot-request>) ostream)
  "Serializes a message object of type '<SendEmRobot-request>"
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
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'robot) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendEmRobot-request>) istream)
  "Deserializes a message object of type '<SendEmRobot-request>"
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
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'robot) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendEmRobot-request>)))
  "Returns string type for a service object of type '<SendEmRobot-request>"
  "adhoc_communication/SendEmRobotRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendEmRobot-request)))
  "Returns string type for a service object of type 'SendEmRobot-request"
  "adhoc_communication/SendEmRobotRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendEmRobot-request>)))
  "Returns md5sum for a message object of type '<SendEmRobot-request>"
  "3d9be68bdd2f929d348378e69f0dc7c2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendEmRobot-request)))
  "Returns md5sum for a message object of type 'SendEmRobot-request"
  "3d9be68bdd2f929d348378e69f0dc7c2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendEmRobot-request>)))
  "Returns full string definition for message of type '<SendEmRobot-request>"
  (cl:format cl:nil "string topic~%string dst_robot~%adhoc_communication/EmRobot robot~%~%================================================================================~%MSG: adhoc_communication/EmRobot~%int32 id~%int32 state # see energy_mgmt/docking.h~%int32 selected_ds #the id of the docking stationc currelty selected by the robot to recharge~%float32 x    #robot x-coordinate (in the reference system of the sending robot, not in the one of the receiver)~%float32 y    #robot y-coordinate (in the reference system of the sending robot, not in the one of the receiver)~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendEmRobot-request)))
  "Returns full string definition for message of type 'SendEmRobot-request"
  (cl:format cl:nil "string topic~%string dst_robot~%adhoc_communication/EmRobot robot~%~%================================================================================~%MSG: adhoc_communication/EmRobot~%int32 id~%int32 state # see energy_mgmt/docking.h~%int32 selected_ds #the id of the docking stationc currelty selected by the robot to recharge~%float32 x    #robot x-coordinate (in the reference system of the sending robot, not in the one of the receiver)~%float32 y    #robot y-coordinate (in the reference system of the sending robot, not in the one of the receiver)~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendEmRobot-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'topic))
     4 (cl:length (cl:slot-value msg 'dst_robot))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'robot))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendEmRobot-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SendEmRobot-request
    (cl:cons ':topic (topic msg))
    (cl:cons ':dst_robot (dst_robot msg))
    (cl:cons ':robot (robot msg))
))
;//! \htmlinclude SendEmRobot-response.msg.html

(cl:defclass <SendEmRobot-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SendEmRobot-response (<SendEmRobot-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendEmRobot-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendEmRobot-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendEmRobot-response> is deprecated: use adhoc_communication-srv:SendEmRobot-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <SendEmRobot-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:status-val is deprecated.  Use adhoc_communication-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendEmRobot-response>) ostream)
  "Serializes a message object of type '<SendEmRobot-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendEmRobot-response>) istream)
  "Deserializes a message object of type '<SendEmRobot-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendEmRobot-response>)))
  "Returns string type for a service object of type '<SendEmRobot-response>"
  "adhoc_communication/SendEmRobotResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendEmRobot-response)))
  "Returns string type for a service object of type 'SendEmRobot-response"
  "adhoc_communication/SendEmRobotResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendEmRobot-response>)))
  "Returns md5sum for a message object of type '<SendEmRobot-response>"
  "3d9be68bdd2f929d348378e69f0dc7c2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendEmRobot-response)))
  "Returns md5sum for a message object of type 'SendEmRobot-response"
  "3d9be68bdd2f929d348378e69f0dc7c2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendEmRobot-response>)))
  "Returns full string definition for message of type '<SendEmRobot-response>"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendEmRobot-response)))
  "Returns full string definition for message of type 'SendEmRobot-response"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendEmRobot-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendEmRobot-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SendEmRobot-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SendEmRobot)))
  'SendEmRobot-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SendEmRobot)))
  'SendEmRobot-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendEmRobot)))
  "Returns string type for a service object of type '<SendEmRobot>"
  "adhoc_communication/SendEmRobot")