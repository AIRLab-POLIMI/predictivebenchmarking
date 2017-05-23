; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-msg)


;//! \htmlinclude ExpFrontier.msg.html

(cl:defclass <ExpFrontier> (roslisp-msg-protocol:ros-message)
  ((frontier_element
    :reader frontier_element
    :initarg :frontier_element
    :type (cl:vector adhoc_communication-msg:ExpFrontierElement)
   :initform (cl:make-array 0 :element-type 'adhoc_communication-msg:ExpFrontierElement :initial-element (cl:make-instance 'adhoc_communication-msg:ExpFrontierElement))))
)

(cl:defclass ExpFrontier (<ExpFrontier>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ExpFrontier>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ExpFrontier)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-msg:<ExpFrontier> is deprecated: use adhoc_communication-msg:ExpFrontier instead.")))

(cl:ensure-generic-function 'frontier_element-val :lambda-list '(m))
(cl:defmethod frontier_element-val ((m <ExpFrontier>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:frontier_element-val is deprecated.  Use adhoc_communication-msg:frontier_element instead.")
  (frontier_element m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ExpFrontier>) ostream)
  "Serializes a message object of type '<ExpFrontier>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'frontier_element))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'frontier_element))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ExpFrontier>) istream)
  "Deserializes a message object of type '<ExpFrontier>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'frontier_element) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'frontier_element)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'adhoc_communication-msg:ExpFrontierElement))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ExpFrontier>)))
  "Returns string type for a message object of type '<ExpFrontier>"
  "adhoc_communication/ExpFrontier")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExpFrontier)))
  "Returns string type for a message object of type 'ExpFrontier"
  "adhoc_communication/ExpFrontier")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ExpFrontier>)))
  "Returns md5sum for a message object of type '<ExpFrontier>"
  "a022dc7f2d36765e856b2878d8a5476f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ExpFrontier)))
  "Returns md5sum for a message object of type 'ExpFrontier"
  "a022dc7f2d36765e856b2878d8a5476f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ExpFrontier>)))
  "Returns full string definition for message of type '<ExpFrontier>"
  (cl:format cl:nil "ExpFrontierElement[] frontier_element~%~%================================================================================~%MSG: adhoc_communication/ExpFrontierElement~%int64 id~%string detected_by_robot_str~%int64 detected_by_robot~%float64 robot_home_position_x~%float64 robot_home_position_y~%float64 x_coordinate~%float64 y_coordinate~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ExpFrontier)))
  "Returns full string definition for message of type 'ExpFrontier"
  (cl:format cl:nil "ExpFrontierElement[] frontier_element~%~%================================================================================~%MSG: adhoc_communication/ExpFrontierElement~%int64 id~%string detected_by_robot_str~%int64 detected_by_robot~%float64 robot_home_position_x~%float64 robot_home_position_y~%float64 x_coordinate~%float64 y_coordinate~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ExpFrontier>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'frontier_element) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ExpFrontier>))
  "Converts a ROS message object to a list"
  (cl:list 'ExpFrontier
    (cl:cons ':frontier_element (frontier_element msg))
))
