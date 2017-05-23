;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::SendCMgrRobotUpdate)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'SendCMgrRobotUpdate (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::SENDCMGRROBOTUPDATE")
  (make-package "ADHOC_COMMUNICATION::SENDCMGRROBOTUPDATE"))
(unless (find-package "ADHOC_COMMUNICATION::SENDCMGRROBOTUPDATEREQUEST")
  (make-package "ADHOC_COMMUNICATION::SENDCMGRROBOTUPDATEREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::SENDCMGRROBOTUPDATERESPONSE")
  (make-package "ADHOC_COMMUNICATION::SENDCMGRROBOTUPDATERESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::SendCMgrRobotUpdateRequest
  :super ros::object
  :slots (_dst_robot _topic _update ))

(defmethod adhoc_communication::SendCMgrRobotUpdateRequest
  (:init
   (&key
    ((:dst_robot __dst_robot) "")
    ((:topic __topic) "")
    ((:update __update) (instance adhoc_communication::CMgrRobotUpdate :init))
    )
   (send-super :init)
   (setq _dst_robot (string __dst_robot))
   (setq _topic (string __topic))
   (setq _update __update)
   self)
  (:dst_robot
   (&optional __dst_robot)
   (if __dst_robot (setq _dst_robot __dst_robot)) _dst_robot)
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
  (:serialization-length
   ()
   (+
    ;; string _dst_robot
    4 (length _dst_robot)
    ;; string _topic
    4 (length _topic)
    ;; adhoc_communication/CMgrRobotUpdate _update
    (send _update :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _dst_robot
       (write-long (length _dst_robot) s) (princ _dst_robot s)
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; adhoc_communication/CMgrRobotUpdate _update
       (send _update :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _dst_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _dst_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; adhoc_communication/CMgrRobotUpdate _update
     (send _update :deserialize buf ptr-) (incf ptr- (send _update :serialization-length))
   ;;
   self)
  )

(defclass adhoc_communication::SendCMgrRobotUpdateResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::SendCMgrRobotUpdateResponse
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

(defclass adhoc_communication::SendCMgrRobotUpdate
  :super ros::object
  :slots ())

(setf (get adhoc_communication::SendCMgrRobotUpdate :md5sum-) "2ccd371ff7aeb961749b74bac24a3996")
(setf (get adhoc_communication::SendCMgrRobotUpdate :datatype-) "adhoc_communication/SendCMgrRobotUpdate")
(setf (get adhoc_communication::SendCMgrRobotUpdate :request) adhoc_communication::SendCMgrRobotUpdateRequest)
(setf (get adhoc_communication::SendCMgrRobotUpdate :response) adhoc_communication::SendCMgrRobotUpdateResponse)

(defmethod adhoc_communication::SendCMgrRobotUpdateRequest
  (:response () (instance adhoc_communication::SendCMgrRobotUpdateResponse :init)))

(setf (get adhoc_communication::SendCMgrRobotUpdateRequest :md5sum-) "2ccd371ff7aeb961749b74bac24a3996")
(setf (get adhoc_communication::SendCMgrRobotUpdateRequest :datatype-) "adhoc_communication/SendCMgrRobotUpdateRequest")
(setf (get adhoc_communication::SendCMgrRobotUpdateRequest :definition-)
      "string dst_robot
string topic
adhoc_communication/CMgrRobotUpdate update

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

(setf (get adhoc_communication::SendCMgrRobotUpdateResponse :md5sum-) "2ccd371ff7aeb961749b74bac24a3996")
(setf (get adhoc_communication::SendCMgrRobotUpdateResponse :datatype-) "adhoc_communication/SendCMgrRobotUpdateResponse")
(setf (get adhoc_communication::SendCMgrRobotUpdateResponse :definition-)
      "string dst_robot
string topic
adhoc_communication/CMgrRobotUpdate update

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



(provide :adhoc_communication/SendCMgrRobotUpdate "2ccd371ff7aeb961749b74bac24a3996")


