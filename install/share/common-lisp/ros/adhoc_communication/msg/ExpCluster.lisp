; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-msg)


;//! \htmlinclude ExpCluster.msg.html

(cl:defclass <ExpCluster> (roslisp-msg-protocol:ros-message)
  ((ids_contained
    :reader ids_contained
    :initarg :ids_contained
    :type (cl:vector adhoc_communication-msg:ExpClusterElement)
   :initform (cl:make-array 0 :element-type 'adhoc_communication-msg:ExpClusterElement :initial-element (cl:make-instance 'adhoc_communication-msg:ExpClusterElement)))
   (bid
    :reader bid
    :initarg :bid
    :type cl:float
    :initform 0.0))
)

(cl:defclass ExpCluster (<ExpCluster>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ExpCluster>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ExpCluster)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-msg:<ExpCluster> is deprecated: use adhoc_communication-msg:ExpCluster instead.")))

(cl:ensure-generic-function 'ids_contained-val :lambda-list '(m))
(cl:defmethod ids_contained-val ((m <ExpCluster>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:ids_contained-val is deprecated.  Use adhoc_communication-msg:ids_contained instead.")
  (ids_contained m))

(cl:ensure-generic-function 'bid-val :lambda-list '(m))
(cl:defmethod bid-val ((m <ExpCluster>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:bid-val is deprecated.  Use adhoc_communication-msg:bid instead.")
  (bid m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ExpCluster>) ostream)
  "Serializes a message object of type '<ExpCluster>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'ids_contained))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'ids_contained))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'bid))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ExpCluster>) istream)
  "Deserializes a message object of type '<ExpCluster>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'ids_contained) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'ids_contained)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'adhoc_communication-msg:ExpClusterElement))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'bid) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ExpCluster>)))
  "Returns string type for a message object of type '<ExpCluster>"
  "adhoc_communication/ExpCluster")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExpCluster)))
  "Returns string type for a message object of type 'ExpCluster"
  "adhoc_communication/ExpCluster")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ExpCluster>)))
  "Returns md5sum for a message object of type '<ExpCluster>"
  "378b1f01ebed06706a22e7cc27608df5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ExpCluster)))
  "Returns md5sum for a message object of type 'ExpCluster"
  "378b1f01ebed06706a22e7cc27608df5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ExpCluster>)))
  "Returns full string definition for message of type '<ExpCluster>"
  (cl:format cl:nil "ExpClusterElement[] ids_contained~%float64 bid ~%~%================================================================================~%MSG: adhoc_communication/ExpClusterElement~%int64 id~%string detected_by_robot_str~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ExpCluster)))
  "Returns full string definition for message of type 'ExpCluster"
  (cl:format cl:nil "ExpClusterElement[] ids_contained~%float64 bid ~%~%================================================================================~%MSG: adhoc_communication/ExpClusterElement~%int64 id~%string detected_by_robot_str~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ExpCluster>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'ids_contained) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ExpCluster>))
  "Converts a ROS message object to a list"
  (cl:list 'ExpCluster
    (cl:cons ':ids_contained (ids_contained msg))
    (cl:cons ':bid (bid msg))
))
