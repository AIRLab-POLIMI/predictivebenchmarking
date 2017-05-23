;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::ExpAuction)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'ExpAuction (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::EXPAUCTION")
  (make-package "ADHOC_COMMUNICATION::EXPAUCTION"))

(in-package "ROS")
;;//! \htmlinclude ExpAuction.msg.html


(defclass adhoc_communication::ExpAuction
  :super ros::object
  :slots (_auction_status_message _start_auction _auction_finished _occupied_ids _requested_clusters _auction_id _robot_name _available_clusters ))

(defmethod adhoc_communication::ExpAuction
  (:init
   (&key
    ((:auction_status_message __auction_status_message) nil)
    ((:start_auction __start_auction) nil)
    ((:auction_finished __auction_finished) nil)
    ((:occupied_ids __occupied_ids) (let (r) (dotimes (i 0) (push (instance adhoc_communication::ExpAuctionElement :init) r)) r))
    ((:requested_clusters __requested_clusters) (let (r) (dotimes (i 0) (push (instance adhoc_communication::ExpCluster :init) r)) r))
    ((:auction_id __auction_id) 0)
    ((:robot_name __robot_name) "")
    ((:available_clusters __available_clusters) (let (r) (dotimes (i 0) (push (instance adhoc_communication::ExpCluster :init) r)) r))
    )
   (send-super :init)
   (setq _auction_status_message __auction_status_message)
   (setq _start_auction __start_auction)
   (setq _auction_finished __auction_finished)
   (setq _occupied_ids __occupied_ids)
   (setq _requested_clusters __requested_clusters)
   (setq _auction_id (round __auction_id))
   (setq _robot_name (string __robot_name))
   (setq _available_clusters __available_clusters)
   self)
  (:auction_status_message
   (&optional __auction_status_message)
   (if __auction_status_message (setq _auction_status_message __auction_status_message)) _auction_status_message)
  (:start_auction
   (&optional __start_auction)
   (if __start_auction (setq _start_auction __start_auction)) _start_auction)
  (:auction_finished
   (&optional __auction_finished)
   (if __auction_finished (setq _auction_finished __auction_finished)) _auction_finished)
  (:occupied_ids
   (&rest __occupied_ids)
   (if (keywordp (car __occupied_ids))
       (send* _occupied_ids __occupied_ids)
     (progn
       (if __occupied_ids (setq _occupied_ids (car __occupied_ids)))
       _occupied_ids)))
  (:requested_clusters
   (&rest __requested_clusters)
   (if (keywordp (car __requested_clusters))
       (send* _requested_clusters __requested_clusters)
     (progn
       (if __requested_clusters (setq _requested_clusters (car __requested_clusters)))
       _requested_clusters)))
  (:auction_id
   (&optional __auction_id)
   (if __auction_id (setq _auction_id __auction_id)) _auction_id)
  (:robot_name
   (&optional __robot_name)
   (if __robot_name (setq _robot_name __robot_name)) _robot_name)
  (:available_clusters
   (&rest __available_clusters)
   (if (keywordp (car __available_clusters))
       (send* _available_clusters __available_clusters)
     (progn
       (if __available_clusters (setq _available_clusters (car __available_clusters)))
       _available_clusters)))
  (:serialization-length
   ()
   (+
    ;; bool _auction_status_message
    1
    ;; bool _start_auction
    1
    ;; bool _auction_finished
    1
    ;; adhoc_communication/ExpAuctionElement[] _occupied_ids
    (apply #'+ (send-all _occupied_ids :serialization-length)) 4
    ;; adhoc_communication/ExpCluster[] _requested_clusters
    (apply #'+ (send-all _requested_clusters :serialization-length)) 4
    ;; uint32 _auction_id
    4
    ;; string _robot_name
    4 (length _robot_name)
    ;; adhoc_communication/ExpCluster[] _available_clusters
    (apply #'+ (send-all _available_clusters :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _auction_status_message
       (if _auction_status_message (write-byte -1 s) (write-byte 0 s))
     ;; bool _start_auction
       (if _start_auction (write-byte -1 s) (write-byte 0 s))
     ;; bool _auction_finished
       (if _auction_finished (write-byte -1 s) (write-byte 0 s))
     ;; adhoc_communication/ExpAuctionElement[] _occupied_ids
     (write-long (length _occupied_ids) s)
     (dolist (elem _occupied_ids)
       (send elem :serialize s)
       )
     ;; adhoc_communication/ExpCluster[] _requested_clusters
     (write-long (length _requested_clusters) s)
     (dolist (elem _requested_clusters)
       (send elem :serialize s)
       )
     ;; uint32 _auction_id
       (write-long _auction_id s)
     ;; string _robot_name
       (write-long (length _robot_name) s) (princ _robot_name s)
     ;; adhoc_communication/ExpCluster[] _available_clusters
     (write-long (length _available_clusters) s)
     (dolist (elem _available_clusters)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _auction_status_message
     (setq _auction_status_message (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _start_auction
     (setq _start_auction (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _auction_finished
     (setq _auction_finished (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; adhoc_communication/ExpAuctionElement[] _occupied_ids
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _occupied_ids (let (r) (dotimes (i n) (push (instance adhoc_communication::ExpAuctionElement :init) r)) r))
     (dolist (elem- _occupied_ids)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; adhoc_communication/ExpCluster[] _requested_clusters
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _requested_clusters (let (r) (dotimes (i n) (push (instance adhoc_communication::ExpCluster :init) r)) r))
     (dolist (elem- _requested_clusters)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; uint32 _auction_id
     (setq _auction_id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string _robot_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _robot_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; adhoc_communication/ExpCluster[] _available_clusters
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _available_clusters (let (r) (dotimes (i n) (push (instance adhoc_communication::ExpCluster :init) r)) r))
     (dolist (elem- _available_clusters)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get adhoc_communication::ExpAuction :md5sum-) "99f1253490d52d5e7eb6095beeea2711")
(setf (get adhoc_communication::ExpAuction :datatype-) "adhoc_communication/ExpAuction")
(setf (get adhoc_communication::ExpAuction :definition-)
      "bool auction_status_message
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

")



(provide :adhoc_communication/ExpAuction "99f1253490d52d5e7eb6095beeea2711")


