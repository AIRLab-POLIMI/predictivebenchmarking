; Auto-generated. Do not edit!


(cl:in-package nav2d_navigator-msg)


;//! \htmlinclude MoveToPosition2DGoal.msg.html

(cl:defclass <MoveToPosition2DGoal> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (target_pose
    :reader target_pose
    :initarg :target_pose
    :type geometry_msgs-msg:Pose2D
    :initform (cl:make-instance 'geometry_msgs-msg:Pose2D))
   (target_distance
    :reader target_distance
    :initarg :target_distance
    :type cl:float
    :initform 0.0)
   (target_angle
    :reader target_angle
    :initarg :target_angle
    :type cl:float
    :initform 0.0))
)

(cl:defclass MoveToPosition2DGoal (<MoveToPosition2DGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoveToPosition2DGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoveToPosition2DGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nav2d_navigator-msg:<MoveToPosition2DGoal> is deprecated: use nav2d_navigator-msg:MoveToPosition2DGoal instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <MoveToPosition2DGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nav2d_navigator-msg:header-val is deprecated.  Use nav2d_navigator-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'target_pose-val :lambda-list '(m))
(cl:defmethod target_pose-val ((m <MoveToPosition2DGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nav2d_navigator-msg:target_pose-val is deprecated.  Use nav2d_navigator-msg:target_pose instead.")
  (target_pose m))

(cl:ensure-generic-function 'target_distance-val :lambda-list '(m))
(cl:defmethod target_distance-val ((m <MoveToPosition2DGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nav2d_navigator-msg:target_distance-val is deprecated.  Use nav2d_navigator-msg:target_distance instead.")
  (target_distance m))

(cl:ensure-generic-function 'target_angle-val :lambda-list '(m))
(cl:defmethod target_angle-val ((m <MoveToPosition2DGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nav2d_navigator-msg:target_angle-val is deprecated.  Use nav2d_navigator-msg:target_angle instead.")
  (target_angle m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoveToPosition2DGoal>) ostream)
  "Serializes a message object of type '<MoveToPosition2DGoal>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'target_pose) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'target_distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'target_angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoveToPosition2DGoal>) istream)
  "Deserializes a message object of type '<MoveToPosition2DGoal>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'target_pose) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_distance) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_angle) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoveToPosition2DGoal>)))
  "Returns string type for a message object of type '<MoveToPosition2DGoal>"
  "nav2d_navigator/MoveToPosition2DGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveToPosition2DGoal)))
  "Returns string type for a message object of type 'MoveToPosition2DGoal"
  "nav2d_navigator/MoveToPosition2DGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoveToPosition2DGoal>)))
  "Returns md5sum for a message object of type '<MoveToPosition2DGoal>"
  "471d15abce131270d05238fa2475ae64")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoveToPosition2DGoal)))
  "Returns md5sum for a message object of type 'MoveToPosition2DGoal"
  "471d15abce131270d05238fa2475ae64")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoveToPosition2DGoal>)))
  "Returns full string definition for message of type '<MoveToPosition2DGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%std_msgs/Header header~%geometry_msgs/Pose2D target_pose~%float32 target_distance~%float32 target_angle~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoveToPosition2DGoal)))
  "Returns full string definition for message of type 'MoveToPosition2DGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%std_msgs/Header header~%geometry_msgs/Pose2D target_pose~%float32 target_distance~%float32 target_angle~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoveToPosition2DGoal>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'target_pose))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoveToPosition2DGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'MoveToPosition2DGoal
    (cl:cons ':header (header msg))
    (cl:cons ':target_pose (target_pose msg))
    (cl:cons ':target_distance (target_distance msg))
    (cl:cons ':target_angle (target_angle msg))
))
