;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::SendMmPoint)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'SendMmPoint (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::SENDMMPOINT")
  (make-package "ADHOC_COMMUNICATION::SENDMMPOINT"))
(unless (find-package "ADHOC_COMMUNICATION::SENDMMPOINTREQUEST")
  (make-package "ADHOC_COMMUNICATION::SENDMMPOINTREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::SENDMMPOINTRESPONSE")
  (make-package "ADHOC_COMMUNICATION::SENDMMPOINTRESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::SendMmPointRequest
  :super ros::object
  :slots (_dst_robot _topic _point ))

(defmethod adhoc_communication::SendMmPointRequest
  (:init
   (&key
    ((:dst_robot __dst_robot) "")
    ((:topic __topic) "")
    ((:point __point) (instance adhoc_communication::MmPoint :init))
    )
   (send-super :init)
   (setq _dst_robot (string __dst_robot))
   (setq _topic (string __topic))
   (setq _point __point)
   self)
  (:dst_robot
   (&optional __dst_robot)
   (if __dst_robot (setq _dst_robot __dst_robot)) _dst_robot)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
  (:point
   (&rest __point)
   (if (keywordp (car __point))
       (send* _point __point)
     (progn
       (if __point (setq _point (car __point)))
       _point)))
  (:serialization-length
   ()
   (+
    ;; string _dst_robot
    4 (length _dst_robot)
    ;; string _topic
    4 (length _topic)
    ;; adhoc_communication/MmPoint _point
    (send _point :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _dst_robot
       (write-long (length _dst_robot) s) (princ _dst_robot s)
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; adhoc_communication/MmPoint _point
       (send _point :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _dst_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _dst_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; adhoc_communication/MmPoint _point
     (send _point :deserialize buf ptr-) (incf ptr- (send _point :serialization-length))
   ;;
   self)
  )

(defclass adhoc_communication::SendMmPointResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::SendMmPointResponse
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

(defclass adhoc_communication::SendMmPoint
  :super ros::object
  :slots ())

(setf (get adhoc_communication::SendMmPoint :md5sum-) "caf6ffd259d365577a9cd46d32b9cb17")
(setf (get adhoc_communication::SendMmPoint :datatype-) "adhoc_communication/SendMmPoint")
(setf (get adhoc_communication::SendMmPoint :request) adhoc_communication::SendMmPointRequest)
(setf (get adhoc_communication::SendMmPoint :response) adhoc_communication::SendMmPointResponse)

(defmethod adhoc_communication::SendMmPointRequest
  (:response () (instance adhoc_communication::SendMmPointResponse :init)))

(setf (get adhoc_communication::SendMmPointRequest :md5sum-) "caf6ffd259d365577a9cd46d32b9cb17")
(setf (get adhoc_communication::SendMmPointRequest :datatype-) "adhoc_communication/SendMmPointRequest")
(setf (get adhoc_communication::SendMmPointRequest :definition-)
      "string dst_robot
string topic
adhoc_communication/MmPoint point

================================================================================
MSG: adhoc_communication/MmPoint
string src_robot
float64 x
float64 y
---
uint8 status

")

(setf (get adhoc_communication::SendMmPointResponse :md5sum-) "caf6ffd259d365577a9cd46d32b9cb17")
(setf (get adhoc_communication::SendMmPointResponse :datatype-) "adhoc_communication/SendMmPointResponse")
(setf (get adhoc_communication::SendMmPointResponse :definition-)
      "string dst_robot
string topic
adhoc_communication/MmPoint point

================================================================================
MSG: adhoc_communication/MmPoint
string src_robot
float64 x
float64 y
---
uint8 status

")



(provide :adhoc_communication/SendMmPoint "caf6ffd259d365577a9cd46d32b9cb17")


