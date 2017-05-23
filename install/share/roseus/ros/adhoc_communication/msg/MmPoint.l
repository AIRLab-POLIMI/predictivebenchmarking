;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::MmPoint)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'MmPoint (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::MMPOINT")
  (make-package "ADHOC_COMMUNICATION::MMPOINT"))

(in-package "ROS")
;;//! \htmlinclude MmPoint.msg.html


(defclass adhoc_communication::MmPoint
  :super ros::object
  :slots (_src_robot _x _y ))

(defmethod adhoc_communication::MmPoint
  (:init
   (&key
    ((:src_robot __src_robot) "")
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    )
   (send-super :init)
   (setq _src_robot (string __src_robot))
   (setq _x (float __x))
   (setq _y (float __y))
   self)
  (:src_robot
   (&optional __src_robot)
   (if __src_robot (setq _src_robot __src_robot)) _src_robot)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:serialization-length
   ()
   (+
    ;; string _src_robot
    4 (length _src_robot)
    ;; float64 _x
    8
    ;; float64 _y
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _src_robot
       (write-long (length _src_robot) s) (princ _src_robot s)
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _src_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _src_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get adhoc_communication::MmPoint :md5sum-) "bf827d01cbf6a28b70ad364cdc656d65")
(setf (get adhoc_communication::MmPoint :datatype-) "adhoc_communication/MmPoint")
(setf (get adhoc_communication::MmPoint :definition-)
      "string src_robot
float64 x
float64 y

")



(provide :adhoc_communication/MmPoint "bf827d01cbf6a28b70ad364cdc656d65")


