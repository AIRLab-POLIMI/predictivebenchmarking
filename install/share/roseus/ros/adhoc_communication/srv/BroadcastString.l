;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::BroadcastString)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'BroadcastString (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::BROADCASTSTRING")
  (make-package "ADHOC_COMMUNICATION::BROADCASTSTRING"))
(unless (find-package "ADHOC_COMMUNICATION::BROADCASTSTRINGREQUEST")
  (make-package "ADHOC_COMMUNICATION::BROADCASTSTRINGREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::BROADCASTSTRINGRESPONSE")
  (make-package "ADHOC_COMMUNICATION::BROADCASTSTRINGRESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::BroadcastStringRequest
  :super ros::object
  :slots (_topic _data _hop_limit ))

(defmethod adhoc_communication::BroadcastStringRequest
  (:init
   (&key
    ((:topic __topic) "")
    ((:data __data) "")
    ((:hop_limit __hop_limit) 0)
    )
   (send-super :init)
   (setq _topic (string __topic))
   (setq _data (string __data))
   (setq _hop_limit (round __hop_limit))
   self)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:hop_limit
   (&optional __hop_limit)
   (if __hop_limit (setq _hop_limit __hop_limit)) _hop_limit)
  (:serialization-length
   ()
   (+
    ;; string _topic
    4 (length _topic)
    ;; string _data
    4 (length _data)
    ;; uint8 _hop_limit
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; string _data
       (write-long (length _data) s) (princ _data s)
     ;; uint8 _hop_limit
       (write-byte _hop_limit s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _data
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _data (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; uint8 _hop_limit
     (setq _hop_limit (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(defclass adhoc_communication::BroadcastStringResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::BroadcastStringResponse
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

(defclass adhoc_communication::BroadcastString
  :super ros::object
  :slots ())

(setf (get adhoc_communication::BroadcastString :md5sum-) "79e1c1b930819d5a990dea57200bd10a")
(setf (get adhoc_communication::BroadcastString :datatype-) "adhoc_communication/BroadcastString")
(setf (get adhoc_communication::BroadcastString :request) adhoc_communication::BroadcastStringRequest)
(setf (get adhoc_communication::BroadcastString :response) adhoc_communication::BroadcastStringResponse)

(defmethod adhoc_communication::BroadcastStringRequest
  (:response () (instance adhoc_communication::BroadcastStringResponse :init)))

(setf (get adhoc_communication::BroadcastStringRequest :md5sum-) "79e1c1b930819d5a990dea57200bd10a")
(setf (get adhoc_communication::BroadcastStringRequest :datatype-) "adhoc_communication/BroadcastStringRequest")
(setf (get adhoc_communication::BroadcastStringRequest :definition-)
      "string topic
string data
uint8 hop_limit
---
uint8 status

")

(setf (get adhoc_communication::BroadcastStringResponse :md5sum-) "79e1c1b930819d5a990dea57200bd10a")
(setf (get adhoc_communication::BroadcastStringResponse :datatype-) "adhoc_communication/BroadcastStringResponse")
(setf (get adhoc_communication::BroadcastStringResponse :definition-)
      "string topic
string data
uint8 hop_limit
---
uint8 status

")



(provide :adhoc_communication/BroadcastString "79e1c1b930819d5a990dea57200bd10a")


