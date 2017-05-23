; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude SendCMgrRobotUpdate-request.msg.html

(cl:defclass <SendCMgrRobotUpdate-request> (roslisp-msg-protocol:ros-message)
  ((dst_robot
    :reader dst_robot
    :initarg :dst_robot
    :type cl:string
    :initform "")
   (topic
    :reader topic
    :initarg :topic
    :type cl:string
    :initform "")
   (update
    :reader update
    :initarg :update
    :type adhoc_communication-msg:CMgrRobotUpdate
    :initform (cl:make-instance 'adhoc_communication-msg:CMgrRobotUpdate)))
)

(cl:defclass SendCMgrRobotUpdate-request (<SendCMgrRobotUpdate-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendCMgrRobotUpdate-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendCMgrRobotUpdate-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendCMgrRobotUpdate-request> is deprecated: use adhoc_communication-srv:SendCMgrRobotUpdate-request instead.")))

(cl:ensure-generic-function 'dst_robot-val :lambda-list '(m))
(cl:defmethod dst_robot-val ((m <SendCMgrRobotUpdate-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:dst_robot-val is deprecated.  Use adhoc_communication-srv:dst_robot instead.")
  (dst_robot m))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <SendCMgrRobotUpdate-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:topic-val is deprecated.  Use adhoc_communication-srv:topic instead.")
  (topic m))

(cl:ensure-generic-function 'update-val :lambda-list '(m))
(cl:defmethod update-val ((m <SendCMgrRobotUpdate-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:update-val is deprecated.  Use adhoc_communication-srv:update instead.")
  (update m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendCMgrRobotUpdate-request>) ostream)
  "Serializes a message object of type '<SendCMgrRobotUpdate-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'dst_robot))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'dst_robot))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'topic))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'topic))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'update) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendCMgrRobotUpdate-request>) istream)
  "Deserializes a message object of type '<SendCMgrRobotUpdate-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'dst_robot) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'dst_robot) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'topic) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'topic) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'update) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendCMgrRobotUpdate-request>)))
  "Returns string type for a service object of type '<SendCMgrRobotUpdate-request>"
  "adhoc_communication/SendCMgrRobotUpdateRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendCMgrRobotUpdate-request)))
  "Returns string type for a service object of type 'SendCMgrRobotUpdate-request"
  "adhoc_communication/SendCMgrRobotUpdateRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendCMgrRobotUpdate-request>)))
  "Returns md5sum for a message object of type '<SendCMgrRobotUpdate-request>"
  "2ccd371ff7aeb961749b74bac24a3996")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendCMgrRobotUpdate-request)))
  "Returns md5sum for a message object of type 'SendCMgrRobotUpdate-request"
  "2ccd371ff7aeb961749b74bac24a3996")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendCMgrRobotUpdate-request>)))
  "Returns full string definition for message of type '<SendCMgrRobotUpdate-request>"
  (cl:format cl:nil "string dst_robot~%string topic~%adhoc_communication/CMgrRobotUpdate update~%~%================================================================================~%MSG: adhoc_communication/CMgrRobotUpdate~%string robot_name~%string capabilities~%float32 energy~%adhoc_communication/CMgrDimensions dimensions~%string status~%string[] neighbors~%~%================================================================================~%MSG: adhoc_communication/CMgrDimensions~%float32 x~%float32 y~%float32 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendCMgrRobotUpdate-request)))
  "Returns full string definition for message of type 'SendCMgrRobotUpdate-request"
  (cl:format cl:nil "string dst_robot~%string topic~%adhoc_communication/CMgrRobotUpdate update~%~%================================================================================~%MSG: adhoc_communication/CMgrRobotUpdate~%string robot_name~%string capabilities~%float32 energy~%adhoc_communication/CMgrDimensions dimensions~%string status~%string[] neighbors~%~%================================================================================~%MSG: adhoc_communication/CMgrDimensions~%float32 x~%float32 y~%float32 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendCMgrRobotUpdate-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'dst_robot))
     4 (cl:length (cl:slot-value msg 'topic))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'update))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendCMgrRobotUpdate-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SendCMgrRobotUpdate-request
    (cl:cons ':dst_robot (dst_robot msg))
    (cl:cons ':topic (topic msg))
    (cl:cons ':update (update msg))
))
;//! \htmlinclude SendCMgrRobotUpdate-response.msg.html

(cl:defclass <SendCMgrRobotUpdate-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SendCMgrRobotUpdate-response (<SendCMgrRobotUpdate-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SendCMgrRobotUpdate-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SendCMgrRobotUpdate-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<SendCMgrRobotUpdate-response> is deprecated: use adhoc_communication-srv:SendCMgrRobotUpdate-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <SendCMgrRobotUpdate-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:status-val is deprecated.  Use adhoc_communication-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SendCMgrRobotUpdate-response>) ostream)
  "Serializes a message object of type '<SendCMgrRobotUpdate-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SendCMgrRobotUpdate-response>) istream)
  "Deserializes a message object of type '<SendCMgrRobotUpdate-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SendCMgrRobotUpdate-response>)))
  "Returns string type for a service object of type '<SendCMgrRobotUpdate-response>"
  "adhoc_communication/SendCMgrRobotUpdateResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendCMgrRobotUpdate-response)))
  "Returns string type for a service object of type 'SendCMgrRobotUpdate-response"
  "adhoc_communication/SendCMgrRobotUpdateResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SendCMgrRobotUpdate-response>)))
  "Returns md5sum for a message object of type '<SendCMgrRobotUpdate-response>"
  "2ccd371ff7aeb961749b74bac24a3996")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SendCMgrRobotUpdate-response)))
  "Returns md5sum for a message object of type 'SendCMgrRobotUpdate-response"
  "2ccd371ff7aeb961749b74bac24a3996")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SendCMgrRobotUpdate-response>)))
  "Returns full string definition for message of type '<SendCMgrRobotUpdate-response>"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SendCMgrRobotUpdate-response)))
  "Returns full string definition for message of type 'SendCMgrRobotUpdate-response"
  (cl:format cl:nil "uint8 status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SendCMgrRobotUpdate-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SendCMgrRobotUpdate-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SendCMgrRobotUpdate-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SendCMgrRobotUpdate)))
  'SendCMgrRobotUpdate-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SendCMgrRobotUpdate)))
  'SendCMgrRobotUpdate-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SendCMgrRobotUpdate)))
  "Returns string type for a service object of type '<SendCMgrRobotUpdate>"
  "adhoc_communication/SendCMgrRobotUpdate")