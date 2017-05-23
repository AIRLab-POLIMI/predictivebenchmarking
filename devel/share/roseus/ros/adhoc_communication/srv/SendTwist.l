;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::SendTwist)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'SendTwist (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::SENDTWIST")
  (make-package "ADHOC_COMMUNICATION::SENDTWIST"))
(unless (find-package "ADHOC_COMMUNICATION::SENDTWISTREQUEST")
  (make-package "ADHOC_COMMUNICATION::SENDTWISTREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::SENDTWISTRESPONSE")
  (make-package "ADHOC_COMMUNICATION::SENDTWISTRESPONSE"))

(in-package "ROS")

(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))




(defclass adhoc_communication::SendTwistRequest
  :super ros::object
  :slots (_dst_robot _topic _twist ))

(defmethod adhoc_communication::SendTwistRequest
  (:init
   (&key
    ((:dst_robot __dst_robot) "")
    ((:topic __topic) "")
    ((:twist __twist) (instance geometry_msgs::Twist :init))
    )
   (send-super :init)
   (setq _dst_robot (string __dst_robot))
   (setq _topic (string __topic))
   (setq _twist __twist)
   self)
  (:dst_robot
   (&optional __dst_robot)
   (if __dst_robot (setq _dst_robot __dst_robot)) _dst_robot)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
  (:twist
   (&rest __twist)
   (if (keywordp (car __twist))
       (send* _twist __twist)
     (progn
       (if __twist (setq _twist (car __twist)))
       _twist)))
  (:serialization-length
   ()
   (+
    ;; string _dst_robot
    4 (length _dst_robot)
    ;; string _topic
    4 (length _topic)
    ;; geometry_msgs/Twist _twist
    (send _twist :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _dst_robot
       (write-long (length _dst_robot) s) (princ _dst_robot s)
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; geometry_msgs/Twist _twist
       (send _twist :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _dst_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _dst_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; geometry_msgs/Twist _twist
     (send _twist :deserialize buf ptr-) (incf ptr- (send _twist :serialization-length))
   ;;
   self)
  )

(defclass adhoc_communication::SendTwistResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::SendTwistResponse
  (:init
   (&key
    ((:status __status) 0)
    )
   (send-super :init)
   (setq _status (round __status))
   self)
  (:status
   (&optional __status)
   (if __status (setq _status __status)) _status)
  (:serialization-length
   ()
   (+
    ;; uint8 _status
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _status
       (write-byte _status s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _status
     (setq _status (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(defclass adhoc_communication::SendTwist
  :super ros::object
  :slots ())

(setf (get adhoc_communication::SendTwist :md5sum-) "46299e0838939232782f7a144baadd0c")
(setf (get adhoc_communication::SendTwist :datatype-) "adhoc_communication/SendTwist")
(setf (get adhoc_communication::SendTwist :request) adhoc_communication::SendTwistRequest)
(setf (get adhoc_communication::SendTwist :response) adhoc_communication::SendTwistResponse)

(defmethod adhoc_communication::SendTwistRequest
  (:response () (instance adhoc_communication::SendTwistResponse :init)))

(setf (get adhoc_communication::SendTwistRequest :md5sum-) "46299e0838939232782f7a144baadd0c")
(setf (get adhoc_communication::SendTwistRequest :datatype-) "adhoc_communication/SendTwistRequest")
(setf (get adhoc_communication::SendTwistRequest :definition-)
      "string dst_robot
string topic
geometry_msgs/Twist twist

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
---
uint8 status

")

(setf (get adhoc_communication::SendTwistResponse :md5sum-) "46299e0838939232782f7a144baadd0c")
(setf (get adhoc_communication::SendTwistResponse :datatype-) "adhoc_communication/SendTwistResponse")
(setf (get adhoc_communication::SendTwistResponse :definition-)
      "string dst_robot
string topic
geometry_msgs/Twist twist

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
---
uint8 status

")



(provide :adhoc_communication/SendTwist "46299e0838939232782f7a144baadd0c")


