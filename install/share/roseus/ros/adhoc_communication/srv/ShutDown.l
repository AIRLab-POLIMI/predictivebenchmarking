;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::ShutDown)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'ShutDown (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::SHUTDOWN")
  (make-package "ADHOC_COMMUNICATION::SHUTDOWN"))
(unless (find-package "ADHOC_COMMUNICATION::SHUTDOWNREQUEST")
  (make-package "ADHOC_COMMUNICATION::SHUTDOWNREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::SHUTDOWNRESPONSE")
  (make-package "ADHOC_COMMUNICATION::SHUTDOWNRESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::ShutDownRequest
  :super ros::object
  :slots ())

(defmethod adhoc_communication::ShutDownRequest
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

(defclass adhoc_communication::ShutDownResponse
  :super ros::object
  :slots ())

(defmethod adhoc_communication::ShutDownResponse
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

(defclass adhoc_communication::ShutDown
  :super ros::object
  :slots ())

(setf (get adhoc_communication::ShutDown :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get adhoc_communication::ShutDown :datatype-) "adhoc_communication/ShutDown")
(setf (get adhoc_communication::ShutDown :request) adhoc_communication::ShutDownRequest)
(setf (get adhoc_communication::ShutDown :response) adhoc_communication::ShutDownResponse)

(defmethod adhoc_communication::ShutDownRequest
  (:response () (instance adhoc_communication::ShutDownResponse :init)))

(setf (get adhoc_communication::ShutDownRequest :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get adhoc_communication::ShutDownRequest :datatype-) "adhoc_communication/ShutDownRequest")
(setf (get adhoc_communication::ShutDownRequest :definition-)
      "---

")

(setf (get adhoc_communication::ShutDownResponse :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get adhoc_communication::ShutDownResponse :datatype-) "adhoc_communication/ShutDownResponse")
(setf (get adhoc_communication::ShutDownResponse :definition-)
      "---

")



(provide :adhoc_communication/ShutDown "d41d8cd98f00b204e9800998ecf8427e")


