;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::MmListOfPoints)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'MmListOfPoints (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::MMLISTOFPOINTS")
  (make-package "ADHOC_COMMUNICATION::MMLISTOFPOINTS"))

(in-package "ROS")
;;//! \htmlinclude MmListOfPoints.msg.html


(defclass adhoc_communication::MmListOfPoints
  :super ros::object
  :slots (_positions ))

(defmethod adhoc_communication::MmListOfPoints
  (:init
   (&key
    ((:positions __positions) (let (r) (dotimes (i 0) (push (instance adhoc_communication::MmPoint :init) r)) r))
    )
   (send-super :init)
   (setq _positions __positions)
   self)
  (:positions
   (&rest __positions)
   (if (keywordp (car __positions))
       (send* _positions __positions)
     (progn
       (if __positions (setq _positions (car __positions)))
       _positions)))
  (:serialization-length
   ()
   (+
    ;; adhoc_communication/MmPoint[] _positions
    (apply #'+ (send-all _positions :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; adhoc_communication/MmPoint[] _positions
     (write-long (length _positions) s)
     (dolist (elem _positions)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; adhoc_communication/MmPoint[] _positions
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _positions (let (r) (dotimes (i n) (push (instance adhoc_communication::MmPoint :init) r)) r))
     (dolist (elem- _positions)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get adhoc_communication::MmListOfPoints :md5sum-) "e9cd3295535d71bbe517f47d6becc28b")
(setf (get adhoc_communication::MmListOfPoints :datatype-) "adhoc_communication/MmListOfPoints")
(setf (get adhoc_communication::MmListOfPoints :definition-)
      "adhoc_communication/MmPoint[] positions

================================================================================
MSG: adhoc_communication/MmPoint
string src_robot
float64 x
float64 y

")



(provide :adhoc_communication/MmListOfPoints "e9cd3295535d71bbe517f47d6becc28b")


