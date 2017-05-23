;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::SendEmAuction)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'SendEmAuction (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::SENDEMAUCTION")
  (make-package "ADHOC_COMMUNICATION::SENDEMAUCTION"))
(unless (find-package "ADHOC_COMMUNICATION::SENDEMAUCTIONREQUEST")
  (make-package "ADHOC_COMMUNICATION::SENDEMAUCTIONREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::SENDEMAUCTIONRESPONSE")
  (make-package "ADHOC_COMMUNICATION::SENDEMAUCTIONRESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::SendEmAuctionRequest
  :super ros::object
  :slots (_topic _dst_robot _auction ))

(defmethod adhoc_communication::SendEmAuctionRequest
  (:init
   (&key
    ((:topic __topic) "")
    ((:dst_robot __dst_robot) "")
    ((:auction __auction) (instance adhoc_communication::EmAuction :init))
    )
   (send-super :init)
   (setq _topic (string __topic))
   (setq _dst_robot (string __dst_robot))
   (setq _auction __auction)
   self)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
  (:dst_robot
   (&optional __dst_robot)
   (if __dst_robot (setq _dst_robot __dst_robot)) _dst_robot)
  (:auction
   (&rest __auction)
   (if (keywordp (car __auction))
       (send* _auction __auction)
     (progn
       (if __auction (setq _auction (car __auction)))
       _auction)))
  (:serialization-length
   ()
   (+
    ;; string _topic
    4 (length _topic)
    ;; string _dst_robot
    4 (length _dst_robot)
    ;; adhoc_communication/EmAuction _auction
    (send _auction :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; string _dst_robot
       (write-long (length _dst_robot) s) (princ _dst_robot s)
     ;; adhoc_communication/EmAuction _auction
       (send _auction :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _dst_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _dst_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; adhoc_communication/EmAuction _auction
     (send _auction :deserialize buf ptr-) (incf ptr- (send _auction :serialization-length))
   ;;
   self)
  )

(defclass adhoc_communication::SendEmAuctionResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::SendEmAuctionResponse
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

(defclass adhoc_communication::SendEmAuction
  :super ros::object
  :slots ())

(setf (get adhoc_communication::SendEmAuction :md5sum-) "c8c30dfd876c5f060f1c0f80b80a6768")
(setf (get adhoc_communication::SendEmAuction :datatype-) "adhoc_communication/SendEmAuction")
(setf (get adhoc_communication::SendEmAuction :request) adhoc_communication::SendEmAuctionRequest)
(setf (get adhoc_communication::SendEmAuction :response) adhoc_communication::SendEmAuctionResponse)

(defmethod adhoc_communication::SendEmAuctionRequest
  (:response () (instance adhoc_communication::SendEmAuctionResponse :init)))

(setf (get adhoc_communication::SendEmAuctionRequest :md5sum-) "c8c30dfd876c5f060f1c0f80b80a6768")
(setf (get adhoc_communication::SendEmAuctionRequest :datatype-) "adhoc_communication/SendEmAuctionRequest")
(setf (get adhoc_communication::SendEmAuctionRequest :definition-)
      "string topic
string dst_robot
adhoc_communication/EmAuction auction

================================================================================
MSG: adhoc_communication/EmAuction
uint32 auction
uint32 robot
uint32 docking_station
float32 bid
---
uint8 status

")

(setf (get adhoc_communication::SendEmAuctionResponse :md5sum-) "c8c30dfd876c5f060f1c0f80b80a6768")
(setf (get adhoc_communication::SendEmAuctionResponse :datatype-) "adhoc_communication/SendEmAuctionResponse")
(setf (get adhoc_communication::SendEmAuctionResponse :definition-)
      "string topic
string dst_robot
adhoc_communication/EmAuction auction

================================================================================
MSG: adhoc_communication/EmAuction
uint32 auction
uint32 robot
uint32 docking_station
float32 bid
---
uint8 status

")



(provide :adhoc_communication/SendEmAuction "c8c30dfd876c5f060f1c0f80b80a6768")


