;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::SendExpAuction)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'SendExpAuction (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::SENDEXPAUCTION")
  (make-package "ADHOC_COMMUNICATION::SENDEXPAUCTION"))
(unless (find-package "ADHOC_COMMUNICATION::SENDEXPAUCTIONREQUEST")
  (make-package "ADHOC_COMMUNICATION::SENDEXPAUCTIONREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::SENDEXPAUCTIONRESPONSE")
  (make-package "ADHOC_COMMUNICATION::SENDEXPAUCTIONRESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::SendExpAuctionRequest
  :super ros::object
  :slots (_topic _dst_robot _auction ))

(defmethod adhoc_communication::SendExpAuctionRequest
  (:init
   (&key
    ((:topic __topic) "")
    ((:dst_robot __dst_robot) "")
    ((:auction __auction) (instance adhoc_communication::ExpAuction :init))
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
    ;; adhoc_communication/ExpAuction _auction
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
     ;; adhoc_communication/ExpAuction _auction
       (send _auction :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _dst_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _dst_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; adhoc_communication/ExpAuction _auction
     (send _auction :deserialize buf ptr-) (incf ptr- (send _auction :serialization-length))
   ;;
   self)
  )

(defclass adhoc_communication::SendExpAuctionResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::SendExpAuctionResponse
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

(defclass adhoc_communication::SendExpAuction
  :super ros::object
  :slots ())

(setf (get adhoc_communication::SendExpAuction :md5sum-) "ff9ea50dac4ae5fb2075cab78b2fc2b9")
(setf (get adhoc_communication::SendExpAuction :datatype-) "adhoc_communication/SendExpAuction")
(setf (get adhoc_communication::SendExpAuction :request) adhoc_communication::SendExpAuctionRequest)
(setf (get adhoc_communication::SendExpAuction :response) adhoc_communication::SendExpAuctionResponse)

(defmethod adhoc_communication::SendExpAuctionRequest
  (:response () (instance adhoc_communication::SendExpAuctionResponse :init)))

(setf (get adhoc_communication::SendExpAuctionRequest :md5sum-) "ff9ea50dac4ae5fb2075cab78b2fc2b9")
(setf (get adhoc_communication::SendExpAuctionRequest :datatype-) "adhoc_communication/SendExpAuctionRequest")
(setf (get adhoc_communication::SendExpAuctionRequest :definition-)
      "string topic
string dst_robot
adhoc_communication/ExpAuction auction

================================================================================
MSG: adhoc_communication/ExpAuction
bool auction_status_message
bool start_auction
bool auction_finished
ExpAuctionElement[] occupied_ids
ExpCluster[] requested_clusters
uint32 auction_id
string robot_name
ExpCluster[] available_clusters

================================================================================
MSG: adhoc_communication/ExpAuctionElement
int64 id
string detected_by_robot_str

================================================================================
MSG: adhoc_communication/ExpCluster
ExpClusterElement[] ids_contained
float64 bid 

================================================================================
MSG: adhoc_communication/ExpClusterElement
int64 id
string detected_by_robot_str
---
uint8 status

")

(setf (get adhoc_communication::SendExpAuctionResponse :md5sum-) "ff9ea50dac4ae5fb2075cab78b2fc2b9")
(setf (get adhoc_communication::SendExpAuctionResponse :datatype-) "adhoc_communication/SendExpAuctionResponse")
(setf (get adhoc_communication::SendExpAuctionResponse :definition-)
      "string topic
string dst_robot
adhoc_communication/ExpAuction auction

================================================================================
MSG: adhoc_communication/ExpAuction
bool auction_status_message
bool start_auction
bool auction_finished
ExpAuctionElement[] occupied_ids
ExpCluster[] requested_clusters
uint32 auction_id
string robot_name
ExpCluster[] available_clusters

================================================================================
MSG: adhoc_communication/ExpAuctionElement
int64 id
string detected_by_robot_str

================================================================================
MSG: adhoc_communication/ExpCluster
ExpClusterElement[] ids_contained
float64 bid 

================================================================================
MSG: adhoc_communication/ExpClusterElement
int64 id
string detected_by_robot_str
---
uint8 status

")



(provide :adhoc_communication/SendExpAuction "ff9ea50dac4ae5fb2075cab78b2fc2b9")


