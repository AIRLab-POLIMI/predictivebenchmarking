;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::ExpCluster)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'ExpCluster (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::EXPCLUSTER")
  (make-package "ADHOC_COMMUNICATION::EXPCLUSTER"))

(in-package "ROS")
;;//! \htmlinclude ExpCluster.msg.html


(defclass adhoc_communication::ExpCluster
  :super ros::object
  :slots (_ids_contained _bid ))

(defmethod adhoc_communication::ExpCluster
  (:init
   (&key
    ((:ids_contained __ids_contained) (let (r) (dotimes (i 0) (push (instance adhoc_communication::ExpClusterElement :init) r)) r))
    ((:bid __bid) 0.0)
    )
   (send-super :init)
   (setq _ids_contained __ids_contained)
   (setq _bid (float __bid))
   self)
  (:ids_contained
   (&rest __ids_contained)
   (if (keywordp (car __ids_contained))
       (send* _ids_contained __ids_contained)
     (progn
       (if __ids_contained (setq _ids_contained (car __ids_contained)))
       _ids_contained)))
  (:bid
   (&optional __bid)
   (if __bid (setq _bid __bid)) _bid)
  (:serialization-length
   ()
   (+
    ;; adhoc_communication/ExpClusterElement[] _ids_contained
    (apply #'+ (send-all _ids_contained :serialization-length)) 4
    ;; float64 _bid
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; adhoc_communication/ExpClusterElement[] _ids_contained
     (write-long (length _ids_contained) s)
     (dolist (elem _ids_contained)
       (send elem :serialize s)
       )
     ;; float64 _bid
       (sys::poke _bid (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; adhoc_communication/ExpClusterElement[] _ids_contained
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _ids_contained (let (r) (dotimes (i n) (push (instance adhoc_communication::ExpClusterElement :init) r)) r))
     (dolist (elem- _ids_contained)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; float64 _bid
     (setq _bid (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get adhoc_communication::ExpCluster :md5sum-) "378b1f01ebed06706a22e7cc27608df5")
(setf (get adhoc_communication::ExpCluster :datatype-) "adhoc_communication/ExpCluster")
(setf (get adhoc_communication::ExpCluster :definition-)
      "ExpClusterElement[] ids_contained
float64 bid 

================================================================================
MSG: adhoc_communication/ExpClusterElement
int64 id
string detected_by_robot_str

")



(provide :adhoc_communication/ExpCluster "378b1f01ebed06706a22e7cc27608df5")


