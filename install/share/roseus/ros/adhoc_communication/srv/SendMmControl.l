;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::SendMmControl)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'SendMmControl (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::SENDMMCONTROL")
  (make-package "ADHOC_COMMUNICATION::SENDMMCONTROL"))
(unless (find-package "ADHOC_COMMUNICATION::SENDMMCONTROLREQUEST")
  (make-package "ADHOC_COMMUNICATION::SENDMMCONTROLREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::SENDMMCONTROLRESPONSE")
  (make-package "ADHOC_COMMUNICATION::SENDMMCONTROLRESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::SendMmControlRequest
  :super ros::object
  :slots (_dst_robot _topic _msg ))

(defmethod adhoc_communication::SendMmControlRequest
  (:init
   (&key
    ((:dst_robot __dst_robot) "")
    ((:topic __topic) "")
    ((:msg __msg) (instance adhoc_communication::MmControl :init))
    )
   (send-super :init)
   (setq _dst_robot (string __dst_robot))
   (setq _topic (string __topic))
   (setq _msg __msg)
   self)
  (:dst_robot
   (&optional __dst_robot)
   (if __dst_robot (setq _dst_robot __dst_robot)) _dst_robot)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
  (:msg
   (&rest __msg)
   (if (keywordp (car __msg))
       (send* _msg __msg)
     (progn
       (if __msg (setq _msg (car __msg)))
       _msg)))
  (:serialization-length
   ()
   (+
    ;; string _dst_robot
    4 (length _dst_robot)
    ;; string _topic
    4 (length _topic)
    ;; adhoc_communication/MmControl _msg
    (send _msg :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _dst_robot
       (write-long (length _dst_robot) s) (princ _dst_robot s)
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; adhoc_communication/MmControl _msg
       (send _msg :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _dst_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _dst_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; adhoc_communication/MmControl _msg
     (send _msg :deserialize buf ptr-) (incf ptr- (send _msg :serialization-length))
   ;;
   self)
  )

(defclass adhoc_communication::SendMmControlResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::SendMmControlResponse
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

(defclass adhoc_communication::SendMmControl
  :super ros::object
  :slots ())

(setf (get adhoc_communication::SendMmControl :md5sum-) "c76c9edaa817ebcfb6a616740eff76e8")
(setf (get adhoc_communication::SendMmControl :datatype-) "adhoc_communication/SendMmControl")
(setf (get adhoc_communication::SendMmControl :request) adhoc_communication::SendMmControlRequest)
(setf (get adhoc_communication::SendMmControl :response) adhoc_communication::SendMmControlResponse)

(defmethod adhoc_communication::SendMmControlRequest
  (:response () (instance adhoc_communication::SendMmControlResponse :init)))

(setf (get adhoc_communication::SendMmControlRequest :md5sum-) "c76c9edaa817ebcfb6a616740eff76e8")
(setf (get adhoc_communication::SendMmControlRequest :datatype-) "adhoc_communication/SendMmControlRequest")
(setf (get adhoc_communication::SendMmControlRequest :definition-)
      "string dst_robot
string topic
adhoc_communication/MmControl msg

================================================================================
MSG: adhoc_communication/MmControl
string src_robot
int32[] update_numbers
---
uint8 status

")

(setf (get adhoc_communication::SendMmControlResponse :md5sum-) "c76c9edaa817ebcfb6a616740eff76e8")
(setf (get adhoc_communication::SendMmControlResponse :datatype-) "adhoc_communication/SendMmControlResponse")
(setf (get adhoc_communication::SendMmControlResponse :definition-)
      "string dst_robot
string topic
adhoc_communication/MmControl msg

================================================================================
MSG: adhoc_communication/MmControl
string src_robot
int32[] update_numbers
---
uint8 status

")



(provide :adhoc_communication/SendMmControl "c76c9edaa817ebcfb6a616740eff76e8")


