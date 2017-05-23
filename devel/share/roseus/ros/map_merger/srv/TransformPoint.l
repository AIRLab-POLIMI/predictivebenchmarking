;; Auto-generated. Do not edit!


(when (boundp 'map_merger::TransformPoint)
  (if (not (find-package "MAP_MERGER"))
    (make-package "MAP_MERGER"))
  (shadow 'TransformPoint (find-package "MAP_MERGER")))
(unless (find-package "MAP_MERGER::TRANSFORMPOINT")
  (make-package "MAP_MERGER::TRANSFORMPOINT"))
(unless (find-package "MAP_MERGER::TRANSFORMPOINTREQUEST")
  (make-package "MAP_MERGER::TRANSFORMPOINTREQUEST"))
(unless (find-package "MAP_MERGER::TRANSFORMPOINTRESPONSE")
  (make-package "MAP_MERGER::TRANSFORMPOINTRESPONSE"))

(in-package "ROS")

(if (not (find-package "ADHOC_COMMUNICATION"))
  (ros::roseus-add-msgs "adhoc_communication"))


(if (not (find-package "ADHOC_COMMUNICATION"))
  (ros::roseus-add-msgs "adhoc_communication"))


(defclass map_merger::TransformPointRequest
  :super ros::object
  :slots (_point ))

(defmethod map_merger::TransformPointRequest
  (:init
   (&key
    ((:point __point) (instance adhoc_communication::MmPoint :init))
    )
   (send-super :init)
   (setq _point __point)
   self)
  (:point
   (&rest __point)
   (if (keywordp (car __point))
       (send* _point __point)
     (progn
       (if __point (setq _point (car __point)))
       _point)))
  (:serialization-length
   ()
   (+
    ;; adhoc_communication/MmPoint _point
    (send _point :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; adhoc_communication/MmPoint _point
       (send _point :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; adhoc_communication/MmPoint _point
     (send _point :deserialize buf ptr-) (incf ptr- (send _point :serialization-length))
   ;;
   self)
  )

(defclass map_merger::TransformPointResponse
  :super ros::object
  :slots (_point ))

(defmethod map_merger::TransformPointResponse
  (:init
   (&key
    ((:point __point) (instance adhoc_communication::MmPoint :init))
    )
   (send-super :init)
   (setq _point __point)
   self)
  (:point
   (&rest __point)
   (if (keywordp (car __point))
       (send* _point __point)
     (progn
       (if __point (setq _point (car __point)))
       _point)))
  (:serialization-length
   ()
   (+
    ;; adhoc_communication/MmPoint _point
    (send _point :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; adhoc_communication/MmPoint _point
       (send _point :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; adhoc_communication/MmPoint _point
     (send _point :deserialize buf ptr-) (incf ptr- (send _point :serialization-length))
   ;;
   self)
  )

(defclass map_merger::TransformPoint
  :super ros::object
  :slots ())

(setf (get map_merger::TransformPoint :md5sum-) "118b08a194ba8d774bcc2a526a4b8444")
(setf (get map_merger::TransformPoint :datatype-) "map_merger/TransformPoint")
(setf (get map_merger::TransformPoint :request) map_merger::TransformPointRequest)
(setf (get map_merger::TransformPoint :response) map_merger::TransformPointResponse)

(defmethod map_merger::TransformPointRequest
  (:response () (instance map_merger::TransformPointResponse :init)))

(setf (get map_merger::TransformPointRequest :md5sum-) "118b08a194ba8d774bcc2a526a4b8444")
(setf (get map_merger::TransformPointRequest :datatype-) "map_merger/TransformPointRequest")
(setf (get map_merger::TransformPointRequest :definition-)
      "adhoc_communication/MmPoint point

================================================================================
MSG: adhoc_communication/MmPoint
string src_robot
float64 x
float64 y
---
adhoc_communication/MmPoint point


================================================================================
MSG: adhoc_communication/MmPoint
string src_robot
float64 x
float64 y
")

(setf (get map_merger::TransformPointResponse :md5sum-) "118b08a194ba8d774bcc2a526a4b8444")
(setf (get map_merger::TransformPointResponse :datatype-) "map_merger/TransformPointResponse")
(setf (get map_merger::TransformPointResponse :definition-)
      "adhoc_communication/MmPoint point

================================================================================
MSG: adhoc_communication/MmPoint
string src_robot
float64 x
float64 y
---
adhoc_communication/MmPoint point


================================================================================
MSG: adhoc_communication/MmPoint
string src_robot
float64 x
float64 y
")



(provide :map_merger/TransformPoint "118b08a194ba8d774bcc2a526a4b8444")


