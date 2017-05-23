;; Auto-generated. Do not edit!


(when (boundp 'map_merger::LogMaps)
  (if (not (find-package "MAP_MERGER"))
    (make-package "MAP_MERGER"))
  (shadow 'LogMaps (find-package "MAP_MERGER")))
(unless (find-package "MAP_MERGER::LOGMAPS")
  (make-package "MAP_MERGER::LOGMAPS"))
(unless (find-package "MAP_MERGER::LOGMAPSREQUEST")
  (make-package "MAP_MERGER::LOGMAPSREQUEST"))
(unless (find-package "MAP_MERGER::LOGMAPSRESPONSE")
  (make-package "MAP_MERGER::LOGMAPSRESPONSE"))

(in-package "ROS")





(defclass map_merger::LogMapsRequest
  :super ros::object
  :slots (_log ))

(defmethod map_merger::LogMapsRequest
  (:init
   (&key
    ((:log __log) 0)
    )
   (send-super :init)
   (setq _log (round __log))
   self)
  (:log
   (&optional __log)
   (if __log (setq _log __log)) _log)
  (:serialization-length
   ()
   (+
    ;; uint16 _log
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint16 _log
       (write-word _log s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint16 _log
     (setq _log (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(defclass map_merger::LogMapsResponse
  :super ros::object
  :slots ())

(defmethod map_merger::LogMapsResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass map_merger::LogMaps
  :super ros::object
  :slots ())

(setf (get map_merger::LogMaps :md5sum-) "bb54d185c1070cbf70d4cfb2996c18fd")
(setf (get map_merger::LogMaps :datatype-) "map_merger/LogMaps")
(setf (get map_merger::LogMaps :request) map_merger::LogMapsRequest)
(setf (get map_merger::LogMaps :response) map_merger::LogMapsResponse)

(defmethod map_merger::LogMapsRequest
  (:response () (instance map_merger::LogMapsResponse :init)))

(setf (get map_merger::LogMapsRequest :md5sum-) "bb54d185c1070cbf70d4cfb2996c18fd")
(setf (get map_merger::LogMapsRequest :datatype-) "map_merger/LogMapsRequest")
(setf (get map_merger::LogMapsRequest :definition-)
      "uint16 log
---

")

(setf (get map_merger::LogMapsResponse :md5sum-) "bb54d185c1070cbf70d4cfb2996c18fd")
(setf (get map_merger::LogMapsResponse :datatype-) "map_merger/LogMapsResponse")
(setf (get map_merger::LogMapsResponse :definition-)
      "uint16 log
---

")



(provide :map_merger/LogMaps "bb54d185c1070cbf70d4cfb2996c18fd")


