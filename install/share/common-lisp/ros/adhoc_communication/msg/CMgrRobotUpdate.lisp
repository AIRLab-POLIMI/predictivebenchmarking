; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-msg)


;//! \htmlinclude CMgrRobotUpdate.msg.html

(cl:defclass <CMgrRobotUpdate> (roslisp-msg-protocol:ros-message)
  ((robot_name
    :reader robot_name
    :initarg :robot_name
    :type cl:string
    :initform "")
   (capabilities
    :reader capabilities
    :initarg :capabilities
    :type cl:string
    :initform "")
   (energy
    :reader energy
    :initarg :energy
    :type cl:float
    :initform 0.0)
   (dimensions
    :reader dimensions
    :initarg :dimensions
    :type adhoc_communication-msg:CMgrDimensions
    :initform (cl:make-instance 'adhoc_communication-msg:CMgrDimensions))
   (status
    :reader status
    :initarg :status
    :type cl:string
    :initform "")
   (neighbors
    :reader neighbors
    :initarg :neighbors
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element "")))
)

(cl:defclass CMgrRobotUpdate (<CMgrRobotUpdate>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CMgrRobotUpdate>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CMgrRobotUpdate)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-msg:<CMgrRobotUpdate> is deprecated: use adhoc_communication-msg:CMgrRobotUpdate instead.")))

(cl:ensure-generic-function 'robot_name-val :lambda-list '(m))
(cl:defmethod robot_name-val ((m <CMgrRobotUpdate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:robot_name-val is deprecated.  Use adhoc_communication-msg:robot_name instead.")
  (robot_name m))

(cl:ensure-generic-function 'capabilities-val :lambda-list '(m))
(cl:defmethod capabilities-val ((m <CMgrRobotUpdate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:capabilities-val is deprecated.  Use adhoc_communication-msg:capabilities instead.")
  (capabilities m))

(cl:ensure-generic-function 'energy-val :lambda-list '(m))
(cl:defmethod energy-val ((m <CMgrRobotUpdate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:energy-val is deprecated.  Use adhoc_communication-msg:energy instead.")
  (energy m))

(cl:ensure-generic-function 'dimensions-val :lambda-list '(m))
(cl:defmethod dimensions-val ((m <CMgrRobotUpdate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:dimensions-val is deprecated.  Use adhoc_communication-msg:dimensions instead.")
  (dimensions m))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <CMgrRobotUpdate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:status-val is deprecated.  Use adhoc_communication-msg:status instead.")
  (status m))

(cl:ensure-generic-function 'neighbors-val :lambda-list '(m))
(cl:defmethod neighbors-val ((m <CMgrRobotUpdate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:neighbors-val is deprecated.  Use adhoc_communication-msg:neighbors instead.")
  (neighbors m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CMgrRobotUpdate>) ostream)
  "Serializes a message object of type '<CMgrRobotUpdate>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'robot_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'robot_name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'capabilities))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'capabilities))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'energy))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'dimensions) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'status))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'status))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'neighbors))))
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
   (cl:slot-value msg 'neighbors))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CMgrRobotUpdate>) istream)
  "Deserializes a message object of type '<CMgrRobotUpdate>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'robot_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'robot_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'capabilities) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'capabilities) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'energy) (roslisp-utils:decode-single-float-bits bits)))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'dimensions) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'status) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'status) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'neighbors) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'neighbors)))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CMgrRobotUpdate>)))
  "Returns string type for a message object of type '<CMgrRobotUpdate>"
  "adhoc_communication/CMgrRobotUpdate")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CMgrRobotUpdate)))
  "Returns string type for a message object of type 'CMgrRobotUpdate"
  "adhoc_communication/CMgrRobotUpdate")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CMgrRobotUpdate>)))
  "Returns md5sum for a message object of type '<CMgrRobotUpdate>"
  "624d872396e6c4effefdaa51af9e8904")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CMgrRobotUpdate)))
  "Returns md5sum for a message object of type 'CMgrRobotUpdate"
  "624d872396e6c4effefdaa51af9e8904")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CMgrRobotUpdate>)))
  "Returns full string definition for message of type '<CMgrRobotUpdate>"
  (cl:format cl:nil "string robot_name~%string capabilities~%float32 energy~%adhoc_communication/CMgrDimensions dimensions~%string status~%string[] neighbors~%~%================================================================================~%MSG: adhoc_communication/CMgrDimensions~%float32 x~%float32 y~%float32 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CMgrRobotUpdate)))
  "Returns full string definition for message of type 'CMgrRobotUpdate"
  (cl:format cl:nil "string robot_name~%string capabilities~%float32 energy~%adhoc_communication/CMgrDimensions dimensions~%string status~%string[] neighbors~%~%================================================================================~%MSG: adhoc_communication/CMgrDimensions~%float32 x~%float32 y~%float32 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CMgrRobotUpdate>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'robot_name))
     4 (cl:length (cl:slot-value msg 'capabilities))
     4
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'dimensions))
     4 (cl:length (cl:slot-value msg 'status))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'neighbors) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CMgrRobotUpdate>))
  "Converts a ROS message object to a list"
  (cl:list 'CMgrRobotUpdate
    (cl:cons ':robot_name (robot_name msg))
    (cl:cons ':capabilities (capabilities msg))
    (cl:cons ':energy (energy msg))
    (cl:cons ':dimensions (dimensions msg))
    (cl:cons ':status (status msg))
    (cl:cons ':neighbors (neighbors msg))
))
