;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::SendString)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'SendString (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::SENDSTRING")
  (make-package "ADHOC_COMMUNICATION::SENDSTRING"))
(unless (find-package "ADHOC_COMMUNICATION::SENDSTRINGREQUEST")
  (make-package "ADHOC_COMMUNICATION::SENDSTRINGREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::SENDSTRINGRESPONSE")
  (make-package "ADHOC_COMMUNICATION::SENDSTRINGRESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::SendStringRequest
  :super ros::object
  :slots (_dst_robot _topic _data ))

(defmethod adhoc_communication::SendStringRequest
  (:init
   (&key
    ((:dst_robot __dst_robot) "")
    ((:topic __topic) "")
    ((:data __data) "")
    )
   (send-super :init)
   (setq _dst_robot (string __dst_robot))
   (setq _topic (string __topic))
   (setq _data (string __data))
   self)
  (:dst_robot
   (&optional __dst_robot)
   (if __dst_robot (setq _dst_robot __dst_robot)) _dst_robot)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; string _dst_robot
    4 (length _dst_robot)
    ;; string _topic
    4 (length _topic)
    ;; string _data
    4 (length _data)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _dst_robot
       (write-long (length _dst_robot) s) (princ _dst_robot s)
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; string _data
       (write-long (length _data) s) (princ _data s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _dst_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _dst_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _data
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _data (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass adhoc_communication::SendStringResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::SendStringResponse
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

(defclass adhoc_communication::SendString
  :super ros::object
  :slots ())

(setf (get adhoc_communication::SendString :md5sum-) "8a764bb571d04dc3b4afbd463166996e")
(setf (get adhoc_communication::SendString :datatype-) "adhoc_communication/SendString")
(setf (get adhoc_communication::SendString :request) adhoc_communication::SendStringRequest)
(setf (get adhoc_communication::SendString :response) adhoc_communication::SendStringResponse)

(defmethod adhoc_communication::SendStringRequest
  (:response () (instance adhoc_communication::SendStringResponse :init)))

(setf (get adhoc_communication::SendStringRequest :md5sum-) "8a764bb571d04dc3b4afbd463166996e")
(setf (get adhoc_communication::SendStringRequest :datatype-) "adhoc_communication/SendStringRequest")
(setf (get adhoc_communication::SendStringRequest :definition-)
      "string dst_robot
string topic
string data
---
uint8 status

")

(setf (get adhoc_communication::SendStringResponse :md5sum-) "8a764bb571d04dc3b4afbd463166996e")
(setf (get adhoc_communication::SendStringResponse :datatype-) "adhoc_communication/SendStringResponse")
(setf (get adhoc_communication::SendStringResponse :definition-)
      "string dst_robot
string topic
string data
---
uint8 status

")



(provide :adhoc_communication/SendString "8a764bb571d04dc3b4afbd463166996e")


