;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::SendExpFrontier)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'SendExpFrontier (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::SENDEXPFRONTIER")
  (make-package "ADHOC_COMMUNICATION::SENDEXPFRONTIER"))
(unless (find-package "ADHOC_COMMUNICATION::SENDEXPFRONTIERREQUEST")
  (make-package "ADHOC_COMMUNICATION::SENDEXPFRONTIERREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::SENDEXPFRONTIERRESPONSE")
  (make-package "ADHOC_COMMUNICATION::SENDEXPFRONTIERRESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::SendExpFrontierRequest
  :super ros::object
  :slots (_dst_robot _topic _frontier ))

(defmethod adhoc_communication::SendExpFrontierRequest
  (:init
   (&key
    ((:dst_robot __dst_robot) "")
    ((:topic __topic) "")
    ((:frontier __frontier) (instance adhoc_communication::ExpFrontier :init))
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
    ;; adhoc_communication/ExpFrontier _frontier
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
     ;; adhoc_communication/ExpFrontier _frontier
       (send _frontier :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _dst_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _dst_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; adhoc_communication/ExpFrontier _frontier
     (send _frontier :deserialize buf ptr-) (incf ptr- (send _frontier :serialization-length))
   ;;
   self)
  )

(defclass adhoc_communication::SendExpFrontierResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::SendExpFrontierResponse
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

(defclass adhoc_communication::SendExpFrontier
  :super ros::object
  :slots ())

(setf (get adhoc_communication::SendExpFrontier :md5sum-) "d7217cbccb23cf4e4e1279a92f585b8a")
(setf (get adhoc_communication::SendExpFrontier :datatype-) "adhoc_communication/SendExpFrontier")
(setf (get adhoc_communication::SendExpFrontier :request) adhoc_communication::SendExpFrontierRequest)
(setf (get adhoc_communication::SendExpFrontier :response) adhoc_communication::SendExpFrontierResponse)

(defmethod adhoc_communication::SendExpFrontierRequest
  (:response () (instance adhoc_communication::SendExpFrontierResponse :init)))

(setf (get adhoc_communication::SendExpFrontierRequest :md5sum-) "d7217cbccb23cf4e4e1279a92f585b8a")
(setf (get adhoc_communication::SendExpFrontierRequest :datatype-) "adhoc_communication/SendExpFrontierRequest")
(setf (get adhoc_communication::SendExpFrontierRequest :definition-)
      "string dst_robot
string topic
adhoc_communication/ExpFrontier frontier

================================================================================
MSG: adhoc_communication/ExpFrontier
ExpFrontierElement[] frontier_element

================================================================================
MSG: adhoc_communication/ExpFrontierElement
int64 id
string detected_by_robot_str
int64 detected_by_robot
float64 robot_home_position_x
float64 robot_home_position_y
float64 x_coordinate
float64 y_coordinate
---
uint8 status

")

(setf (get adhoc_communication::SendExpFrontierResponse :md5sum-) "d7217cbccb23cf4e4e1279a92f585b8a")
(setf (get adhoc_communication::SendExpFrontierResponse :datatype-) "adhoc_communication/SendExpFrontierResponse")
(setf (get adhoc_communication::SendExpFrontierResponse :definition-)
      "string dst_robot
string topic
adhoc_communication/ExpFrontier frontier

================================================================================
MSG: adhoc_communication/ExpFrontier
ExpFrontierElement[] frontier_element

================================================================================
MSG: adhoc_communication/ExpFrontierElement
int64 id
string detected_by_robot_str
int64 detected_by_robot
float64 robot_home_position_x
float64 robot_home_position_y
float64 x_coordinate
float64 y_coordinate
---
uint8 status

")



(provide :adhoc_communication/SendExpFrontier "d7217cbccb23cf4e4e1279a92f585b8a")


