;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::SendQuaternion)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'SendQuaternion (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::SENDQUATERNION")
  (make-package "ADHOC_COMMUNICATION::SENDQUATERNION"))
(unless (find-package "ADHOC_COMMUNICATION::SENDQUATERNIONREQUEST")
  (make-package "ADHOC_COMMUNICATION::SENDQUATERNIONREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::SENDQUATERNIONRESPONSE")
  (make-package "ADHOC_COMMUNICATION::SENDQUATERNIONRESPONSE"))

(in-package "ROS")

(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))




(defclass adhoc_communication::SendQuaternionRequest
  :super ros::object
  :slots (_dst_robot _topic _quaternion ))

(defmethod adhoc_communication::SendQuaternionRequest
  (:init
   (&key
    ((:dst_robot __dst_robot) "")
    ((:topic __topic) "")
    ((:quaternion __quaternion) (instance geometry_msgs::Quaternion :init))
    )
   (send-super :init)
   (setq _dst_robot (string __dst_robot))
   (setq _topic (string __topic))
   (setq _quaternion __quaternion)
   self)
  (:dst_robot
   (&optional __dst_robot)
   (if __dst_robot (setq _dst_robot __dst_robot)) _dst_robot)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
  (:quaternion
   (&rest __quaternion)
   (if (keywordp (car __quaternion))
       (send* _quaternion __quaternion)
     (progn
       (if __quaternion (setq _quaternion (car __quaternion)))
       _quaternion)))
  (:serialization-length
   ()
   (+
    ;; string _dst_robot
    4 (length _dst_robot)
    ;; string _topic
    4 (length _topic)
    ;; geometry_msgs/Quaternion _quaternion
    (send _quaternion :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _dst_robot
       (write-long (length _dst_robot) s) (princ _dst_robot s)
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; geometry_msgs/Quaternion _quaternion
       (send _quaternion :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _dst_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _dst_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; geometry_msgs/Quaternion _quaternion
     (send _quaternion :deserialize buf ptr-) (incf ptr- (send _quaternion :serialization-length))
   ;;
   self)
  )

(defclass adhoc_communication::SendQuaternionResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::SendQuaternionResponse
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

(defclass adhoc_communication::SendQuaternion
  :super ros::object
  :slots ())

(setf (get adhoc_communication::SendQuaternion :md5sum-) "6d4c9ce8c8598fcc5972b254856eb7e3")
(setf (get adhoc_communication::SendQuaternion :datatype-) "adhoc_communication/SendQuaternion")
(setf (get adhoc_communication::SendQuaternion :request) adhoc_communication::SendQuaternionRequest)
(setf (get adhoc_communication::SendQuaternion :response) adhoc_communication::SendQuaternionResponse)

(defmethod adhoc_communication::SendQuaternionRequest
  (:response () (instance adhoc_communication::SendQuaternionResponse :init)))

(setf (get adhoc_communication::SendQuaternionRequest :md5sum-) "6d4c9ce8c8598fcc5972b254856eb7e3")
(setf (get adhoc_communication::SendQuaternionRequest :datatype-) "adhoc_communication/SendQuaternionRequest")
(setf (get adhoc_communication::SendQuaternionRequest :definition-)
      "string dst_robot
string topic
geometry_msgs/Quaternion quaternion

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
---
uint8 status

")

(setf (get adhoc_communication::SendQuaternionResponse :md5sum-) "6d4c9ce8c8598fcc5972b254856eb7e3")
(setf (get adhoc_communication::SendQuaternionResponse :datatype-) "adhoc_communication/SendQuaternionResponse")
(setf (get adhoc_communication::SendQuaternionResponse :definition-)
      "string dst_robot
string topic
geometry_msgs/Quaternion quaternion

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
---
uint8 status

")



(provide :adhoc_communication/SendQuaternion "6d4c9ce8c8598fcc5972b254856eb7e3")


