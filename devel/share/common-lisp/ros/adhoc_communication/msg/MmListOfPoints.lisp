; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-msg)


;//! \htmlinclude MmListOfPoints.msg.html

(cl:defclass <MmListOfPoints> (roslisp-msg-protocol:ros-message)
  ((positions
    :reader positions
    :initarg :positions
    :type (cl:vector adhoc_communication-msg:MmPoint)
   :initform (cl:make-array 0 :element-type 'adhoc_communication-msg:MmPoint :initial-element (cl:make-instance 'adhoc_communication-msg:MmPoint))))
)

(cl:defclass MmListOfPoints (<MmListOfPoints>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MmListOfPoints>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MmListOfPoints)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-msg:<MmListOfPoints> is deprecated: use adhoc_communication-msg:MmListOfPoints instead.")))

(cl:ensure-generic-function 'positions-val :lambda-list '(m))
(cl:defmethod positions-val ((m <MmListOfPoints>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:positions-val is deprecated.  Use adhoc_communication-msg:positions instead.")
  (positions m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MmListOfPoints>) ostream)
  "Serializes a message object of type '<MmListOfPoints>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'positions))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'positions))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MmListOfPoints>) istream)
  "Deserializes a message object of type '<MmListOfPoints>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'positions) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'positions)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'adhoc_communication-msg:MmPoint))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MmListOfPoints>)))
  "Returns string type for a message object of type '<MmListOfPoints>"
  "adhoc_communication/MmListOfPoints")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MmListOfPoints)))
  "Returns string type for a message object of type 'MmListOfPoints"
  "adhoc_communication/MmListOfPoints")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MmListOfPoints>)))
  "Returns md5sum for a message object of type '<MmListOfPoints>"
  "e9cd3295535d71bbe517f47d6becc28b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MmListOfPoints)))
  "Returns md5sum for a message object of type 'MmListOfPoints"
  "e9cd3295535d71bbe517f47d6becc28b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MmListOfPoints>)))
  "Returns full string definition for message of type '<MmListOfPoints>"
  (cl:format cl:nil "adhoc_communication/MmPoint[] positions~%~%================================================================================~%MSG: adhoc_communication/MmPoint~%string src_robot~%float64 x~%float64 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MmListOfPoints)))
  "Returns full string definition for message of type 'MmListOfPoints"
  (cl:format cl:nil "adhoc_communication/MmPoint[] positions~%~%================================================================================~%MSG: adhoc_communication/MmPoint~%string src_robot~%float64 x~%float64 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MmListOfPoints>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'positions) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MmListOfPoints>))
  "Converts a ROS message object to a list"
  (cl:list 'MmListOfPoints
    (cl:cons ':positions (positions msg))
))
