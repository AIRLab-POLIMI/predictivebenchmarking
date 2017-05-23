;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::BroadcastCMgrRobotUpdate)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'BroadcastCMgrRobotUpdate (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::BROADCASTCMGRROBOTUPDATE")
  (make-package "ADHOC_COMMUNICATION::BROADCASTCMGRROBOTUPDATE"))
(unless (find-package "ADHOC_COMMUNICATION::BROADCASTCMGRROBOTUPDATEREQUEST")
  (make-package "ADHOC_COMMUNICATION::BROADCASTCMGRROBOTUPDATEREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::BROADCASTCMGRROBOTUPDATERESPONSE")
  (make-package "ADHOC_COMMUNICATION::BROADCASTCMGRROBOTUPDATERESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::BroadcastCMgrRobotUpdateRequest
  :super ros::object
  :slots (_topic _update _hop_limit ))

(defmethod adhoc_communication::BroadcastCMgrRobotUpdateRequest
  (:init
   (&key
    ((:topic __topic) "")
    ((:update __update) (instance adhoc_communication::CMgrRobotUpdate :init))
    ((:hop_limit __hop_limit) 0)
    )
   (send-super :init)
   (setq _topic (string __topic))
   (setq _update __update)
   (setq _hop_limit (round __hop_limit))
   self)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
  (:update
   (&rest __update)
   (if (keywordp (car __update))
       (send* _update __update)
     (progn
       (if __update (setq _update (car __update)))
       _update)))
  (:hop_limit
   (&optional __hop_limit)
   (if __hop_limit (setq _hop_limit __hop_limit)) _hop_limit)
  (:serialization-length
   ()
   (+
    ;; string _topic
    4 (length _topic)
    ;; adhoc_communication/CMgrRobotUpdate _update
    (send _update :serialization-length)
    ;; uint8 _hop_limit
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; adhoc_communication/CMgrRobotUpdate _update
       (send _update :serialize s)
     ;; uint8 _hop_limit
       (write-byte _hop_limit s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; adhoc_communication/CMgrRobotUpdate _update
     (send _update :deserialize buf ptr-) (incf ptr- (send _update :serialization-length))
   ;; uint8 _hop_limit
     (setq _hop_limit (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(defclass adhoc_communication::BroadcastCMgrRobotUpdateResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::BroadcastCMgrRobotUpdateResponse
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

(defclass adhoc_communication::BroadcastCMgrRobotUpdate
  :super ros::object
  :slots ())

(setf (get adhoc_communication::BroadcastCMgrRobotUpdate :md5sum-) "4f803d834e6e3f0165ecc26babd1f3f1")
(setf (get adhoc_communication::BroadcastCMgrRobotUpdate :datatype-) "adhoc_communication/BroadcastCMgrRobotUpdate")
(setf (get adhoc_communication::BroadcastCMgrRobotUpdate :request) adhoc_communication::BroadcastCMgrRobotUpdateRequest)
(setf (get adhoc_communication::BroadcastCMgrRobotUpdate :response) adhoc_communication::BroadcastCMgrRobotUpdateResponse)

(defmethod adhoc_communication::BroadcastCMgrRobotUpdateRequest
  (:response () (instance adhoc_communication::BroadcastCMgrRobotUpdateResponse :init)))

(setf (get adhoc_communication::BroadcastCMgrRobotUpdateRequest :md5sum-) "4f803d834e6e3f0165ecc26babd1f3f1")
(setf (get adhoc_communication::BroadcastCMgrRobotUpdateRequest :datatype-) "adhoc_communication/BroadcastCMgrRobotUpdateRequest")
(setf (get adhoc_communication::BroadcastCMgrRobotUpdateRequest :definition-)
      "string topic
adhoc_communication/CMgrRobotUpdate update
uint8 hop_limit

================================================================================
MSG: adhoc_communication/CMgrRobotUpdate
string robot_name
string capabilities
float32 energy
adhoc_communication/CMgrDimensions dimensions
string status
string[] neighbors

================================================================================
MSG: adhoc_communication/CMgrDimensions
float32 x
float32 y
float32 z
---
uint8 status

")

(setf (get adhoc_communication::BroadcastCMgrRobotUpdateResponse :md5sum-) "4f803d834e6e3f0165ecc26babd1f3f1")
(setf (get adhoc_communication::BroadcastCMgrRobotUpdateResponse :datatype-) "adhoc_communication/BroadcastCMgrRobotUpdateResponse")
(setf (get adhoc_communication::BroadcastCMgrRobotUpdateResponse :definition-)
      "string topic
adhoc_communication/CMgrRobotUpdate update
uint8 hop_limit

================================================================================
MSG: adhoc_communication/CMgrRobotUpdate
string robot_name
string capabilities
float32 energy
adhoc_communication/CMgrDimensions dimensions
string status
string[] neighbors

================================================================================
MSG: adhoc_communication/CMgrDimensions
float32 x
float32 y
float32 z
---
uint8 status

")



(provide :adhoc_communication/BroadcastCMgrRobotUpdate "4f803d834e6e3f0165ecc26babd1f3f1")


