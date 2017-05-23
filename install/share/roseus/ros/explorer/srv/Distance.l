;; Auto-generated. Do not edit!


(when (boundp 'explorer::Distance)
  (if (not (find-package "EXPLORER"))
    (make-package "EXPLORER"))
  (shadow 'Distance (find-package "EXPLORER")))
(unless (find-package "EXPLORER::DISTANCE")
  (make-package "EXPLORER::DISTANCE"))
(unless (find-package "EXPLORER::DISTANCEREQUEST")
  (make-package "EXPLORER::DISTANCEREQUEST"))
(unless (find-package "EXPLORER::DISTANCERESPONSE")
  (make-package "EXPLORER::DISTANCERESPONSE"))

(in-package "ROS")





(defclass explorer::DistanceRequest
  :super ros::object
  :slots (_x1 _y1 _x2 _y2 ))

(defmethod explorer::DistanceRequest
  (:init
   (&key
    ((:x1 __x1) 0.0)
    ((:y1 __y1) 0.0)
    ((:x2 __x2) 0.0)
    ((:y2 __y2) 0.0)
    )
   (send-super :init)
   (setq _x1 (float __x1))
   (setq _y1 (float __y1))
   (setq _x2 (float __x2))
   (setq _y2 (float __y2))
   self)
  (:x1
   (&optional __x1)
   (if __x1 (setq _x1 __x1)) _x1)
  (:y1
   (&optional __y1)
   (if __y1 (setq _y1 __y1)) _y1)
  (:x2
   (&optional __x2)
   (if __x2 (setq _x2 __x2)) _x2)
  (:y2
   (&optional __y2)
   (if __y2 (setq _y2 __y2)) _y2)
  (:serialization-length
   ()
   (+
    ;; float32 _x1
    4
    ;; float32 _y1
    4
    ;; float32 _x2
    4
    ;; float32 _y2
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x1
       (sys::poke _x1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y1
       (sys::poke _y1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _x2
       (sys::poke _x2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y2
       (sys::poke _y2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x1
     (setq _x1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y1
     (setq _y1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _x2
     (setq _x2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y2
     (setq _y2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass explorer::DistanceResponse
  :super ros::object
  :slots (_status _distance ))

(defmethod explorer::DistanceResponse
  (:init
   (&key
    ((:status __status) 0)
    ((:distance __distance) 0.0)
    )
   (send-super :init)
   (setq _status (round __status))
   (setq _distance (float __distance))
   self)
  (:status
   (&optional __status)
   (if __status (setq _status __status)) _status)
  (:distance
   (&optional __distance)
   (if __distance (setq _distance __distance)) _distance)
  (:serialization-length
   ()
   (+
    ;; uint8 _status
    1
    ;; float32 _distance
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _status
       (write-byte _status s)
     ;; float32 _distance
       (sys::poke _distance (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _status
     (setq _status (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float32 _distance
     (setq _distance (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass explorer::Distance
  :super ros::object
  :slots ())

(setf (get explorer::Distance :md5sum-) "a709d085eafc08a7a947afad7963fe2c")
(setf (get explorer::Distance :datatype-) "explorer/Distance")
(setf (get explorer::Distance :request) explorer::DistanceRequest)
(setf (get explorer::Distance :response) explorer::DistanceResponse)

(defmethod explorer::DistanceRequest
  (:response () (instance explorer::DistanceResponse :init)))

(setf (get explorer::DistanceRequest :md5sum-) "a709d085eafc08a7a947afad7963fe2c")
(setf (get explorer::DistanceRequest :datatype-) "explorer/DistanceRequest")
(setf (get explorer::DistanceRequest :definition-)
      "float32 x1
float32 y1
float32 x2
float32 y2
---
uint8 status
float32 distance

")

(setf (get explorer::DistanceResponse :md5sum-) "a709d085eafc08a7a947afad7963fe2c")
(setf (get explorer::DistanceResponse :datatype-) "explorer/DistanceResponse")
(setf (get explorer::DistanceResponse :definition-)
      "float32 x1
float32 y1
float32 x2
float32 y2
---
uint8 status
float32 distance

")



(provide :explorer/Distance "a709d085eafc08a7a947afad7963fe2c")


