;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::SendExpCluster)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'SendExpCluster (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::SENDEXPCLUSTER")
  (make-package "ADHOC_COMMUNICATION::SENDEXPCLUSTER"))
(unless (find-package "ADHOC_COMMUNICATION::SENDEXPCLUSTERREQUEST")
  (make-package "ADHOC_COMMUNICATION::SENDEXPCLUSTERREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::SENDEXPCLUSTERRESPONSE")
  (make-package "ADHOC_COMMUNICATION::SENDEXPCLUSTERRESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::SendExpClusterRequest
  :super ros::object
  :slots (_topic _dst_robot _cluster ))

(defmethod adhoc_communication::SendExpClusterRequest
  (:init
   (&key
    ((:topic __topic) "")
    ((:dst_robot __dst_robot) "")
    ((:cluster __cluster) (instance adhoc_communication::ExpCluster :init))
    )
   (send-super :init)
   (setq _topic (string __topic))
   (setq _dst_robot (string __dst_robot))
   (setq _cluster __cluster)
   self)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
  (:dst_robot
   (&optional __dst_robot)
   (if __dst_robot (setq _dst_robot __dst_robot)) _dst_robot)
  (:cluster
   (&rest __cluster)
   (if (keywordp (car __cluster))
       (send* _cluster __cluster)
     (progn
       (if __cluster (setq _cluster (car __cluster)))
       _cluster)))
  (:serialization-length
   ()
   (+
    ;; string _topic
    4 (length _topic)
    ;; string _dst_robot
    4 (length _dst_robot)
    ;; adhoc_communication/ExpCluster _cluster
    (send _cluster :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; string _dst_robot
       (write-long (length _dst_robot) s) (princ _dst_robot s)
     ;; adhoc_communication/ExpCluster _cluster
       (send _cluster :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _dst_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _dst_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; adhoc_communication/ExpCluster _cluster
     (send _cluster :deserialize buf ptr-) (incf ptr- (send _cluster :serialization-length))
   ;;
   self)
  )

(defclass adhoc_communication::SendExpClusterResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::SendExpClusterResponse
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

(defclass adhoc_communication::SendExpCluster
  :super ros::object
  :slots ())

(setf (get adhoc_communication::SendExpCluster :md5sum-) "356dd4b5adb461bab3c183a7d7c21532")
(setf (get adhoc_communication::SendExpCluster :datatype-) "adhoc_communication/SendExpCluster")
(setf (get adhoc_communication::SendExpCluster :request) adhoc_communication::SendExpClusterRequest)
(setf (get adhoc_communication::SendExpCluster :response) adhoc_communication::SendExpClusterResponse)

(defmethod adhoc_communication::SendExpClusterRequest
  (:response () (instance adhoc_communication::SendExpClusterResponse :init)))

(setf (get adhoc_communication::SendExpClusterRequest :md5sum-) "356dd4b5adb461bab3c183a7d7c21532")
(setf (get adhoc_communication::SendExpClusterRequest :datatype-) "adhoc_communication/SendExpClusterRequest")
(setf (get adhoc_communication::SendExpClusterRequest :definition-)
      "string topic
string dst_robot
adhoc_communication/ExpCluster cluster

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

(setf (get adhoc_communication::SendExpClusterResponse :md5sum-) "356dd4b5adb461bab3c183a7d7c21532")
(setf (get adhoc_communication::SendExpClusterResponse :datatype-) "adhoc_communication/SendExpClusterResponse")
(setf (get adhoc_communication::SendExpClusterResponse :definition-)
      "string topic
string dst_robot
adhoc_communication/ExpCluster cluster

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



(provide :adhoc_communication/SendExpCluster "356dd4b5adb461bab3c183a7d7c21532")


