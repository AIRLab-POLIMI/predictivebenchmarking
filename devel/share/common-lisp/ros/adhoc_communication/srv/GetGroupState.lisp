; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude GetGroupState-request.msg.html

(cl:defclass <GetGroupState-request> (roslisp-msg-protocol:ros-message)
  ((group_name
    :reader group_name
    :initarg :group_name
    :type cl:string
    :initform ""))
)

(cl:defclass GetGroupState-request (<GetGroupState-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetGroupState-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetGroupState-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<GetGroupState-request> is deprecated: use adhoc_communication-srv:GetGroupState-request instead.")))

(cl:ensure-generic-function 'group_name-val :lambda-list '(m))
(cl:defmethod group_name-val ((m <GetGroupState-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:group_name-val is deprecated.  Use adhoc_communication-srv:group_name instead.")
  (group_name m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetGroupState-request>) ostream)
  "Serializes a message object of type '<GetGroupState-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'group_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'group_name))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetGroupState-request>) istream)
  "Deserializes a message object of type '<GetGroupState-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'group_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'group_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetGroupState-request>)))
  "Returns string type for a service object of type '<GetGroupState-request>"
  "adhoc_communication/GetGroupStateRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetGroupState-request)))
  "Returns string type for a service object of type 'GetGroupState-request"
  "adhoc_communication/GetGroupStateRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetGroupState-request>)))
  "Returns md5sum for a message object of type '<GetGroupState-request>"
  "3fd78af244ca7820f4d762caa767ec74")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetGroupState-request)))
  "Returns md5sum for a message object of type 'GetGroupState-request"
  "3fd78af244ca7820f4d762caa767ec74")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetGroupState-request>)))
  "Returns full string definition for message of type '<GetGroupState-request>"
  (cl:format cl:nil "string group_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetGroupState-request)))
  "Returns full string definition for message of type 'GetGroupState-request"
  (cl:format cl:nil "string group_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetGroupState-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'group_name))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetGroupState-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GetGroupState-request
    (cl:cons ':group_name (group_name msg))
))
;//! \htmlinclude GetGroupState-response.msg.html

(cl:defclass <GetGroupState-response> (roslisp-msg-protocol:ros-message)
  ((member
    :reader member
    :initarg :member
    :type cl:boolean
    :initform cl:nil)
   (activated
    :reader activated
    :initarg :activated
    :type cl:boolean
    :initform cl:nil)
   (connected
    :reader connected
    :initarg :connected
    :type cl:boolean
    :initform cl:nil)
   (root
    :reader root
    :initarg :root
    :type cl:boolean
    :initform cl:nil)
   (joining
    :reader joining
    :initarg :joining
    :type cl:boolean
    :initform cl:nil)
   (route_uplink
    :reader route_uplink
    :initarg :route_uplink
    :type cl:string
    :initform "")
   (downlinks
    :reader downlinks
    :initarg :downlinks
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element "")))
)

(cl:defclass GetGroupState-response (<GetGroupState-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetGroupState-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetGroupState-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<GetGroupState-response> is deprecated: use adhoc_communication-srv:GetGroupState-response instead.")))

(cl:ensure-generic-function 'member-val :lambda-list '(m))
(cl:defmethod member-val ((m <GetGroupState-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:member-val is deprecated.  Use adhoc_communication-srv:member instead.")
  (member m))

(cl:ensure-generic-function 'activated-val :lambda-list '(m))
(cl:defmethod activated-val ((m <GetGroupState-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:activated-val is deprecated.  Use adhoc_communication-srv:activated instead.")
  (activated m))

(cl:ensure-generic-function 'connected-val :lambda-list '(m))
(cl:defmethod connected-val ((m <GetGroupState-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:connected-val is deprecated.  Use adhoc_communication-srv:connected instead.")
  (connected m))

(cl:ensure-generic-function 'root-val :lambda-list '(m))
(cl:defmethod root-val ((m <GetGroupState-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:root-val is deprecated.  Use adhoc_communication-srv:root instead.")
  (root m))

(cl:ensure-generic-function 'joining-val :lambda-list '(m))
(cl:defmethod joining-val ((m <GetGroupState-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:joining-val is deprecated.  Use adhoc_communication-srv:joining instead.")
  (joining m))

(cl:ensure-generic-function 'route_uplink-val :lambda-list '(m))
(cl:defmethod route_uplink-val ((m <GetGroupState-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:route_uplink-val is deprecated.  Use adhoc_communication-srv:route_uplink instead.")
  (route_uplink m))

(cl:ensure-generic-function 'downlinks-val :lambda-list '(m))
(cl:defmethod downlinks-val ((m <GetGroupState-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:downlinks-val is deprecated.  Use adhoc_communication-srv:downlinks instead.")
  (downlinks m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetGroupState-response>) ostream)
  "Serializes a message object of type '<GetGroupState-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'member) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'activated) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'connected) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'root) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'joining) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'route_uplink))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'route_uplink))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'downlinks))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'downlinks))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetGroupState-response>) istream)
  "Deserializes a message object of type '<GetGroupState-response>"
    (cl:setf (cl:slot-value msg 'member) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'activated) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'connected) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'root) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'joining) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'route_uplink) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'route_uplink) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'downlinks) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'downlinks)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetGroupState-response>)))
  "Returns string type for a service object of type '<GetGroupState-response>"
  "adhoc_communication/GetGroupStateResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetGroupState-response)))
  "Returns string type for a service object of type 'GetGroupState-response"
  "adhoc_communication/GetGroupStateResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetGroupState-response>)))
  "Returns md5sum for a message object of type '<GetGroupState-response>"
  "3fd78af244ca7820f4d762caa767ec74")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetGroupState-response)))
  "Returns md5sum for a message object of type 'GetGroupState-response"
  "3fd78af244ca7820f4d762caa767ec74")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetGroupState-response>)))
  "Returns full string definition for message of type '<GetGroupState-response>"
  (cl:format cl:nil "bool member~%bool activated~%bool connected~%bool root~%bool joining~%string route_uplink~%string[] downlinks~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetGroupState-response)))
  "Returns full string definition for message of type 'GetGroupState-response"
  (cl:format cl:nil "bool member~%bool activated~%bool connected~%bool root~%bool joining~%string route_uplink~%string[] downlinks~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetGroupState-response>))
  (cl:+ 0
     1
     1
     1
     1
     1
     4 (cl:length (cl:slot-value msg 'route_uplink))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'downlinks) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetGroupState-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GetGroupState-response
    (cl:cons ':member (member msg))
    (cl:cons ':activated (activated msg))
    (cl:cons ':connected (connected msg))
    (cl:cons ':root (root msg))
    (cl:cons ':joining (joining msg))
    (cl:cons ':route_uplink (route_uplink msg))
    (cl:cons ':downlinks (downlinks msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GetGroupState)))
  'GetGroupState-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GetGroupState)))
  'GetGroupState-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetGroupState)))
  "Returns string type for a service object of type '<GetGroupState>"
  "adhoc_communication/GetGroupState")