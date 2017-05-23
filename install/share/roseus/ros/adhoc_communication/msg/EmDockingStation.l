;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::EmDockingStation)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'EmDockingStation (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::EMDOCKINGSTATION")
  (make-package "ADHOC_COMMUNICATION::EMDOCKINGSTATION"))

(in-package "ROS")
;;//! \htmlinclude EmDockingStation.msg.html


(defclass adhoc_communication::EmDockingStation
  :super ros::object
  :slots (_id _x _y _vacant ))

(defmethod adhoc_communication::EmDockingStation
  (:init
   (&key
    ((:id __id) 0)
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:vacant __vacant) nil)
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _vacant __vacant)
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:vacant
   (&optional __vacant)
   (if __vacant (setq _vacant __vacant)) _vacant)
  (:serialization-length
   ()
   (+
    ;; int32 _id
    4
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; bool _vacant
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _id
       (write-long _id s)
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; bool _vacant
       (if _vacant (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _id
     (setq _id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; bool _vacant
     (setq _vacant (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get adhoc_communication::EmDockingStation :md5sum-) "02e4453bcd60ac3df68a333e1d9e1373")
(setf (get adhoc_communication::EmDockingStation :datatype-) "adhoc_communication/EmDockingStation")
(setf (get adhoc_communication::EmDockingStation :definition-)
      "int32 id
float64 x
float64 y
bool vacant
")



(provide :adhoc_communication/EmDockingStation "02e4453bcd60ac3df68a333e1d9e1373")


