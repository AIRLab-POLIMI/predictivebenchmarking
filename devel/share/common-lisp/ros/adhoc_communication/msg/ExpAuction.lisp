; Auto-generated. Do not edit!


(cl:in-package adhoc_communication-msg)


;//! \htmlinclude ExpAuction.msg.html

(cl:defclass <ExpAuction> (roslisp-msg-protocol:ros-message)
  ((auction_status_message
    :reader auction_status_message
    :initarg :auction_status_message
    :type cl:boolean
    :initform cl:nil)
   (start_auction
    :reader start_auction
    :initarg :start_auction
    :type cl:boolean
    :initform cl:nil)
   (auction_finished
    :reader auction_finished
    :initarg :auction_finished
    :type cl:boolean
    :initform cl:nil)
   (occupied_ids
    :reader occupied_ids
    :initarg :occupied_ids
    :type (cl:vector adhoc_communication-msg:ExpAuctionElement)
   :initform (cl:make-array 0 :element-type 'adhoc_communication-msg:ExpAuctionElement :initial-element (cl:make-instance 'adhoc_communication-msg:ExpAuctionElement)))
   (requested_clusters
    :reader requested_clusters
    :initarg :requested_clusters
    :type (cl:vector adhoc_communication-msg:ExpCluster)
   :initform (cl:make-array 0 :element-type 'adhoc_communication-msg:ExpCluster :initial-element (cl:make-instance 'adhoc_communication-msg:ExpCluster)))
   (auction_id
    :reader auction_id
    :initarg :auction_id
    :type cl:integer
    :initform 0)
   (robot_name
    :reader robot_name
    :initarg :robot_name
    :type cl:string
    :initform "")
   (available_clusters
    :reader available_clusters
    :initarg :available_clusters
    :type (cl:vector adhoc_communication-msg:ExpCluster)
   :initform (cl:make-array 0 :element-type 'adhoc_communication-msg:ExpCluster :initial-element (cl:make-instance 'adhoc_communication-msg:ExpCluster))))
)

(cl:defclass ExpAuction (<ExpAuction>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ExpAuction>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ExpAuction)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name adhoc_communication-msg:<ExpAuction> is deprecated: use adhoc_communication-msg:ExpAuction instead.")))

(cl:ensure-generic-function 'auction_status_message-val :lambda-list '(m))
(cl:defmethod auction_status_message-val ((m <ExpAuction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:auction_status_message-val is deprecated.  Use adhoc_communication-msg:auction_status_message instead.")
  (auction_status_message m))

(cl:ensure-generic-function 'start_auction-val :lambda-list '(m))
(cl:defmethod start_auction-val ((m <ExpAuction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:start_auction-val is deprecated.  Use adhoc_communication-msg:start_auction instead.")
  (start_auction m))

(cl:ensure-generic-function 'auction_finished-val :lambda-list '(m))
(cl:defmethod auction_finished-val ((m <ExpAuction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:auction_finished-val is deprecated.  Use adhoc_communication-msg:auction_finished instead.")
  (auction_finished m))

(cl:ensure-generic-function 'occupied_ids-val :lambda-list '(m))
(cl:defmethod occupied_ids-val ((m <ExpAuction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:occupied_ids-val is deprecated.  Use adhoc_communication-msg:occupied_ids instead.")
  (occupied_ids m))

(cl:ensure-generic-function 'requested_clusters-val :lambda-list '(m))
(cl:defmethod requested_clusters-val ((m <ExpAuction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:requested_clusters-val is deprecated.  Use adhoc_communication-msg:requested_clusters instead.")
  (requested_clusters m))

(cl:ensure-generic-function 'auction_id-val :lambda-list '(m))
(cl:defmethod auction_id-val ((m <ExpAuction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:auction_id-val is deprecated.  Use adhoc_communication-msg:auction_id instead.")
  (auction_id m))

(cl:ensure-generic-function 'robot_name-val :lambda-list '(m))
(cl:defmethod robot_name-val ((m <ExpAuction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:robot_name-val is deprecated.  Use adhoc_communication-msg:robot_name instead.")
  (robot_name m))

(cl:ensure-generic-function 'available_clusters-val :lambda-list '(m))
(cl:defmethod available_clusters-val ((m <ExpAuction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader adhoc_communication-msg:available_clusters-val is deprecated.  Use adhoc_communication-msg:available_clusters instead.")
  (available_clusters m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ExpAuction>) ostream)
  "Serializes a message object of type '<ExpAuction>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'auction_status_message) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'start_auction) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'auction_finished) 1 0)) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'occupied_ids))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'occupied_ids))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'requested_clusters))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'requested_clusters))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'auction_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'auction_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'auction_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'auction_id)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'robot_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'robot_name))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'available_clusters))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'available_clusters))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ExpAuction>) istream)
  "Deserializes a message object of type '<ExpAuction>"
    (cl:setf (cl:slot-value msg 'auction_status_message) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'start_auction) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'auction_finished) (cl:not (cl:zerop (cl:read-byte istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'occupied_ids) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'occupied_ids)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'adhoc_communication-msg:ExpAuctionElement))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'requested_clusters) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'requested_clusters)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'adhoc_communication-msg:ExpCluster))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'auction_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'auction_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'auction_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'auction_id)) (cl:read-byte istream))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'robot_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'robot_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'available_clusters) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'available_clusters)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'adhoc_communication-msg:ExpCluster))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ExpAuction>)))
  "Returns string type for a message object of type '<ExpAuction>"
  "adhoc_communication/ExpAuction")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExpAuction)))
  "Returns string type for a message object of type 'ExpAuction"
  "adhoc_communication/ExpAuction")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ExpAuction>)))
  "Returns md5sum for a message object of type '<ExpAuction>"
  "99f1253490d52d5e7eb6095beeea2711")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ExpAuction)))
  "Returns md5sum for a message object of type 'ExpAuction"
  "99f1253490d52d5e7eb6095beeea2711")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ExpAuction>)))
  "Returns full string definition for message of type '<ExpAuction>"
  (cl:format cl:nil "bool auction_status_message~%bool start_auction~%bool auction_finished~%ExpAuctionElement[] occupied_ids~%ExpCluster[] requested_clusters~%uint32 auction_id~%string robot_name~%ExpCluster[] available_clusters~%~%================================================================================~%MSG: adhoc_communication/ExpAuctionElement~%int64 id~%string detected_by_robot_str~%~%================================================================================~%MSG: adhoc_communication/ExpCluster~%ExpClusterElement[] ids_contained~%float64 bid ~%~%================================================================================~%MSG: adhoc_communication/ExpClusterElement~%int64 id~%string detected_by_robot_str~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ExpAuction)))
  "Returns full string definition for message of type 'ExpAuction"
  (cl:format cl:nil "bool auction_status_message~%bool start_auction~%bool auction_finished~%ExpAuctionElement[] occupied_ids~%ExpCluster[] requested_clusters~%uint32 auction_id~%string robot_name~%ExpCluster[] available_clusters~%~%================================================================================~%MSG: adhoc_communication/ExpAuctionElement~%int64 id~%string detected_by_robot_str~%~%================================================================================~%MSG: adhoc_communication/ExpCluster~%ExpClusterElement[] ids_contained~%float64 bid ~%~%================================================================================~%MSG: adhoc_communication/ExpClusterElement~%int64 id~%string detected_by_robot_str~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ExpAuction>))
  (cl:+ 0
     1
     1
     1
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'occupied_ids) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'requested_clusters) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4
     4 (cl:length (cl:slot-value msg 'robot_name))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'available_clusters) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ExpAuction>))
  "Converts a ROS message object to a list"
  (cl:list 'ExpAuction
    (cl:cons ':auction_status_message (auction_status_message msg))
    (cl:cons ':start_auction (start_auction msg))
    (cl:cons ':auction_finished (auction_finished msg))
    (cl:cons ':occupied_ids (occupied_ids msg))
    (cl:cons ':requested_clusters (requested_clusters msg))
    (cl:cons ':auction_id (auction_id msg))
    (cl:cons ':robot_name (robot_name msg))
    (cl:cons ':available_clusters (available_clusters msg))
))
