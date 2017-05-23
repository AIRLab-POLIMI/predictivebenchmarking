; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-msg)


;//! \htmlinclude MmRobotPosition.msg.html

(cl:defclass <MmRobotPosition> (roslisp-msg-protocol:ros-message)
  ((src_robot
    :reader src_robot
    :initarg :src_robot
    :type cl:string
    :initform "")
   (position
    :reader position
    :initarg :position
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped)))
)

(cl:defclass MmRobotPosition (<MmRobotPosition>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MmRobotPosition>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MmRobotPosition)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-msg:<MmRobotPosition> is deprecated: use adhoc_communication-msg:MmRobotPosition instead.")))

(cl:ensure-generic-function 'src_robot-val :lambda-list '(m))
(cl:defmethod src_robot-val ((m <MmRobotPosition>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:src_robot-val is deprecated.  Use adhoc_communication-msg:src_robot instead.")
  (src_robot m))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <MmRobotPosition>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:position-val is deprecated.  Use adhoc_communication-msg:position instead.")
  (position m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MmRobotPosition>) ostream)
  "Serializes a message object of type '<MmRobotPosition>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'src_robot))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'src_robot))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'position) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MmRobotPosition>) istream)
  "Deserializes a message object of type '<MmRobotPosition>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'src_robot) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'src_robot) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'position) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MmRobotPosition>)))
  "Returns string type for a message object of type '<MmRobotPosition>"
  "adhoc_communication/MmRobotPosition")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MmRobotPosition)))
  "Returns string type for a message object of type 'MmRobotPosition"
  "adhoc_communication/MmRobotPosition")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MmRobotPosition>)))
  "Returns md5sum for a message object of type '<MmRobotPosition>"
  "b110eae90e8648401835f8c826926f86")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MmRobotPosition)))
  "Returns md5sum for a message object of type 'MmRobotPosition"
  "b110eae90e8648401835f8c826926f86")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MmRobotPosition>)))
  "Returns full string definition for message of type '<MmRobotPosition>"
  (cl:format cl:nil "string src_robot~%geometry_msgs/PoseStamped position~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MmRobotPosition)))
  "Returns full string definition for message of type 'MmRobotPosition"
  (cl:format cl:nil "string src_robot~%geometry_msgs/PoseStamped position~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MmRobotPosition>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'src_robot))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'position))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MmRobotPosition>))
  "Converts a ROS message object to a list"
  (cl:list 'MmRobotPosition
    (cl:cons ':src_robot (src_robot msg))
    (cl:cons ':position (position msg))
))
