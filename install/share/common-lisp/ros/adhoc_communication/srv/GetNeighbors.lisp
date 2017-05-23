; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-srv)


;//! \htmlinclude GetNeighbors-request.msg.html

(cl:defclass <GetNeighbors-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass GetNeighbors-request (<GetNeighbors-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetNeighbors-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetNeighbors-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<GetNeighbors-request> is deprecated: use adhoc_communication-srv:GetNeighbors-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetNeighbors-request>) ostream)
  "Serializes a message object of type '<GetNeighbors-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetNeighbors-request>) istream)
  "Deserializes a message object of type '<GetNeighbors-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetNeighbors-request>)))
  "Returns string type for a service object of type '<GetNeighbors-request>"
  "adhoc_communication/GetNeighborsRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetNeighbors-request)))
  "Returns string type for a service object of type 'GetNeighbors-request"
  "adhoc_communication/GetNeighborsRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetNeighbors-request>)))
  "Returns md5sum for a message object of type '<GetNeighbors-request>"
  "a51be085cd4a0fb160e82a9e1952784d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetNeighbors-request)))
  "Returns md5sum for a message object of type 'GetNeighbors-request"
  "a51be085cd4a0fb160e82a9e1952784d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetNeighbors-request>)))
  "Returns full string definition for message of type '<GetNeighbors-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetNeighbors-request)))
  "Returns full string definition for message of type 'GetNeighbors-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetNeighbors-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetNeighbors-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GetNeighbors-request
))
;//! \htmlinclude GetNeighbors-response.msg.html

(cl:defclass <GetNeighbors-response> (roslisp-msg-protocol:ros-message)
  ((neigbors
    :reader neigbors
    :initarg :neigbors
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element "")))
)

(cl:defclass GetNeighbors-response (<GetNeighbors-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetNeighbors-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetNeighbors-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-srv:<GetNeighbors-response> is deprecated: use adhoc_communication-srv:GetNeighbors-response instead.")))

(cl:ensure-generic-function 'neigbors-val :lambda-list '(m))
(cl:defmethod neigbors-val ((m <GetNeighbors-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-srv:neigbors-val is deprecated.  Use adhoc_communication-srv:neigbors instead.")
  (neigbors m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetNeighbors-response>) ostream)
  "Serializes a message object of type '<GetNeighbors-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'neigbors))))
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
   (cl:slot-value msg 'neigbors))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetNeighbors-response>) istream)
  "Deserializes a message object of type '<GetNeighbors-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'neigbors) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'neigbors)))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetNeighbors-response>)))
  "Returns string type for a service object of type '<GetNeighbors-response>"
  "adhoc_communication/GetNeighborsResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetNeighbors-response)))
  "Returns string type for a service object of type 'GetNeighbors-response"
  "adhoc_communication/GetNeighborsResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetNeighbors-response>)))
  "Returns md5sum for a message object of type '<GetNeighbors-response>"
  "a51be085cd4a0fb160e82a9e1952784d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetNeighbors-response)))
  "Returns md5sum for a message object of type 'GetNeighbors-response"
  "a51be085cd4a0fb160e82a9e1952784d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetNeighbors-response>)))
  "Returns full string definition for message of type '<GetNeighbors-response>"
  (cl:format cl:nil "string[] neigbors~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetNeighbors-response)))
  "Returns full string definition for message of type 'GetNeighbors-response"
  (cl:format cl:nil "string[] neigbors~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetNeighbors-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'neigbors) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetNeighbors-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GetNeighbors-response
    (cl:cons ':neigbors (neigbors msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GetNeighbors)))
  'GetNeighbors-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GetNeighbors)))
  'GetNeighbors-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetNeighbors)))
  "Returns string type for a service object of type '<GetNeighbors>"
  "adhoc_communication/GetNeighbors")