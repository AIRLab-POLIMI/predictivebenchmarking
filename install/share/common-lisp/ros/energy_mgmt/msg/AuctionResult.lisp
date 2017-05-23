; Auto-generated. Do not edit!


(cl:in-package energy_mgmt-msg)


;//! \htmlinclude AuctionResult.msg.html

(cl:defclass <AuctionResult> (roslisp-msg-protocol:ros-message)
  ((winner
    :reader winner
    :initarg :winner
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass AuctionResult (<AuctionResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AuctionResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AuctionResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name energy_mgmt-msg:<AuctionResult> is deprecated: use energy_mgmt-msg:AuctionResult instead.")))

(cl:ensure-generic-function 'winner-val :lambda-list '(m))
(cl:defmethod winner-val ((m <AuctionResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader energy_mgmt-msg:winner-val is deprecated.  Use energy_mgmt-msg:winner instead.")
  (winner m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AuctionResult>) ostream)
  "Serializes a message object of type '<AuctionResult>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'winner) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AuctionResult>) istream)
  "Deserializes a message object of type '<AuctionResult>"
    (cl:setf (cl:slot-value msg 'winner) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AuctionResult>)))
  "Returns string type for a message object of type '<AuctionResult>"
  "energy_mgmt/AuctionResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AuctionResult)))
  "Returns string type for a message object of type 'AuctionResult"
  "energy_mgmt/AuctionResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AuctionResult>)))
  "Returns md5sum for a message object of type '<AuctionResult>"
  "970386071cec2ebdf79afc8a0312c15a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AuctionResult)))
  "Returns md5sum for a message object of type 'AuctionResult"
  "970386071cec2ebdf79afc8a0312c15a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AuctionResult>)))
  "Returns full string definition for message of type '<AuctionResult>"
  (cl:format cl:nil "bool winner~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AuctionResult)))
  "Returns full string definition for message of type 'AuctionResult"
  (cl:format cl:nil "bool winner~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AuctionResult>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AuctionResult>))
  "Converts a ROS message object to a list"
  (cl:list 'AuctionResult
    (cl:cons ':winner (winner msg))
))
