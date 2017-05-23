;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::GetNeighbors)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'GetNeighbors (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::GETNEIGHBORS")
  (make-package "ADHOC_COMMUNICATION::GETNEIGHBORS"))
(unless (find-package "ADHOC_COMMUNICATION::GETNEIGHBORSREQUEST")
  (make-package "ADHOC_COMMUNICATION::GETNEIGHBORSREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::GETNEIGHBORSRESPONSE")
  (make-package "ADHOC_COMMUNICATION::GETNEIGHBORSRESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::GetNeighborsRequest
  :super ros::object
  :slots ())

(defmethod adhoc_communication::GetNeighborsRequest
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

(defclass adhoc_communication::GetNeighborsResponse
  :super ros::object
  :slots (_neigbors ))

(defmethod adhoc_communication::GetNeighborsResponse
  (:init
   (&key
    ((:neigbors __neigbors) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _neigbors __neigbors)
   self)
  (:neigbors
   (&optional __neigbors)
   (if __neigbors (setq _neigbors __neigbors)) _neigbors)
  (:serialization-length
   ()
   (+
    ;; string[] _neigbors
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _neigbors)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _neigbors
     (write-long (length _neigbors) s)
     (dolist (elem _neigbors)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _neigbors
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _neigbors (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _neigbors i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(defclass adhoc_communication::GetNeighbors
  :super ros::object
  :slots ())

(setf (get adhoc_communication::GetNeighbors :md5sum-) "a51be085cd4a0fb160e82a9e1952784d")
(setf (get adhoc_communication::GetNeighbors :datatype-) "adhoc_communication/GetNeighbors")
(setf (get adhoc_communication::GetNeighbors :request) adhoc_communication::GetNeighborsRequest)
(setf (get adhoc_communication::GetNeighbors :response) adhoc_communication::GetNeighborsResponse)

(defmethod adhoc_communication::GetNeighborsRequest
  (:response () (instance adhoc_communication::GetNeighborsResponse :init)))

(setf (get adhoc_communication::GetNeighborsRequest :md5sum-) "a51be085cd4a0fb160e82a9e1952784d")
(setf (get adhoc_communication::GetNeighborsRequest :datatype-) "adhoc_communication/GetNeighborsRequest")
(setf (get adhoc_communication::GetNeighborsRequest :definition-)
      "---
string[] neigbors
")

(setf (get adhoc_communication::GetNeighborsResponse :md5sum-) "a51be085cd4a0fb160e82a9e1952784d")
(setf (get adhoc_communication::GetNeighborsResponse :datatype-) "adhoc_communication/GetNeighborsResponse")
(setf (get adhoc_communication::GetNeighborsResponse :definition-)
      "---
string[] neigbors
")



(provide :adhoc_communication/GetNeighbors "a51be085cd4a0fb160e82a9e1952784d")


