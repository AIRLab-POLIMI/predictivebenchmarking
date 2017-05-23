;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::SendExpFrontier2)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'SendExpFrontier2 (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::SENDEXPFRONTIER2")
  (make-package "ADHOC_COMMUNICATION::SENDEXPFRONTIER2"))
(unless (find-package "ADHOC_COMMUNICATION::SENDEXPFRONTIER2REQUEST")
  (make-package "ADHOC_COMMUNICATION::SENDEXPFRONTIER2REQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::SENDEXPFRONTIER2RESPONSE")
  (make-package "ADHOC_COMMUNICATION::SENDEXPFRONTIER2RESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::SendExpFrontier2Request
  :super ros::object
  :slots (_dst_robot _topic _frontier ))

(defmethod adhoc_communication::SendExpFrontier2Request
  (:init
   (&key
    ((:dst_robot __dst_robot) "")
    ((:topic __topic) "")
    ((:frontier __frontier) (instance adhoc_communication::ExpFrontierElement :init))
    )
   (send-super :init)
   (setq _dst_robot (string __dst_robot))
   (setq _topic (string __topic))
   (setq _frontier __frontier)
   self)
  (:dst_robot
   (&optional __dst_robot)
   (if __dst_robot (setq _dst_robot __dst_robot)) _dst_robot)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
  (:frontier
   (&rest __frontier)
   (if (keywordp (car __frontier))
       (send* _frontier __frontier)
     (progn
       (if __frontier (setq _frontier (car __frontier)))
       _frontier)))
  (:serialization-length
   ()
   (+
    ;; string _dst_robot
    4 (length _dst_robot)
    ;; string _topic
    4 (length _topic)
    ;; adhoc_communication/ExpFrontierElement _frontier
    (send _frontier :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _dst_robot
       (write-long (length _dst_robot) s) (princ _dst_robot s)
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; adhoc_communication/ExpFrontierElement _frontier
       (send _frontier :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _dst_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _dst_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; adhoc_communication/ExpFrontierElement _frontier
     (send _frontier :deserialize buf ptr-) (incf ptr- (send _frontier :serialization-length))
   ;;
   self)
  )

(defclass adhoc_communication::SendExpFrontier2Response
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::SendExpFrontier2Response
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

(defclass adhoc_communication::SendExpFrontier2
  :super ros::object
  :slots ())

(setf (get adhoc_communication::SendExpFrontier2 :md5sum-) "c95ef85b5ba5b536a769a25a3d571277")
(setf (get adhoc_communication::SendExpFrontier2 :datatype-) "adhoc_communication/SendExpFrontier2")
(setf (get adhoc_communication::SendExpFrontier2 :request) adhoc_communication::SendExpFrontier2Request)
(setf (get adhoc_communication::SendExpFrontier2 :response) adhoc_communication::SendExpFrontier2Response)

(defmethod adhoc_communication::SendExpFrontier2Request
  (:response () (instance adhoc_communication::SendExpFrontier2Response :init)))

(setf (get adhoc_communication::SendExpFrontier2Request :md5sum-) "c95ef85b5ba5b536a769a25a3d571277")
(setf (get adhoc_communication::SendExpFrontier2Request :datatype-) "adhoc_communication/SendExpFrontier2Request")
(setf (get adhoc_communication::SendExpFrontier2Request :definition-)
      "string dst_robot
string topic
adhoc_communication/ExpFrontierElement frontier

================================================================================
MSG: adhoc_communication/ExpFrontierElement
int64 id
string detected_by_robot_str
int64 detected_by_robot
float64 robot_home_position_x
float64 robot_home_position_y
float64 x_coordinate
float64 y_coordinate
float64 bid
---
uint8 status

")

(setf (get adhoc_communication::SendExpFrontier2Response :md5sum-) "c95ef85b5ba5b536a769a25a3d571277")
(setf (get adhoc_communication::SendExpFrontier2Response :datatype-) "adhoc_communication/SendExpFrontier2Response")
(setf (get adhoc_communication::SendExpFrontier2Response :definition-)
      "string dst_robot
string topic
adhoc_communication/ExpFrontierElement frontier

================================================================================
MSG: adhoc_communication/ExpFrontierElement
int64 id
string detected_by_robot_str
int64 detected_by_robot
float64 robot_home_position_x
float64 robot_home_position_y
float64 x_coordinate
float64 y_coordinate
float64 bid
---
uint8 status

")



(provide :adhoc_communication/SendExpFrontier2 "c95ef85b5ba5b536a769a25a3d571277")


