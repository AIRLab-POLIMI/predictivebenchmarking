;; Auto-generated. Do not edit!


(when (boundp 'explorer::DistanceFromRobot)
  (if (not (find-package "EXPLORER"))
    (make-package "EXPLORER"))
  (shadow 'DistanceFromRobot (find-package "EXPLORER")))
(unless (find-package "EXPLORER::DISTANCEFROMROBOT")
  (make-package "EXPLORER::DISTANCEFROMROBOT"))
(unless (find-package "EXPLORER::DISTANCEFROMROBOTREQUEST")
  (make-package "EXPLORER::DISTANCEFROMROBOTREQUEST"))
(unless (find-package "EXPLORER::DISTANCEFROMROBOTRESPONSE")
  (make-package "EXPLORER::DISTANCEFROMROBOTRESPONSE"))

(in-package "ROS")





(defclass explorer::DistanceFromRobotRequest
  :super ros::object
  :slots (_x _y ))

(defmethod explorer::DistanceFromRobotRequest
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass explorer::DistanceFromRobotResponse
  :super ros::object
  :slots (_status _reachable _distance ))

(defmethod explorer::DistanceFromRobotResponse
  (:init
   (&key
    ((:status __status) 0)
    ((:reachable __reachable) 0)
    ((:distance __distance) 0.0)
    )
   (send-super :init)
   (setq _status (round __status))
   (setq _reachable (round __reachable))
   (setq _distance (float __distance))
   self)
  (:status
   (&optional __status)
   (if __status (setq _status __status)) _status)
  (:reachable
   (&optional __reachable)
   (if __reachable (setq _reachable __reachable)) _reachable)
  (:distance
   (&optional __distance)
   (if __distance (setq _distance __distance)) _distance)
  (:serialization-length
   ()
   (+
    ;; uint8 _status
    1
    ;; uint8 _reachable
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
     ;; uint8 _reachable
       (write-byte _reachable s)
     ;; float32 _distance
       (sys::poke _distance (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _status
     (setq _status (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _reachable
     (setq _reachable (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float32 _distance
     (setq _distance (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass explorer::DistanceFromRobot
  :super ros::object
  :slots ())

(setf (get explorer::DistanceFromRobot :md5sum-) "fcc6a54f128d10ae4d19b273bb4c2682")
(setf (get explorer::DistanceFromRobot :datatype-) "explorer/DistanceFromRobot")
(setf (get explorer::DistanceFromRobot :request) explorer::DistanceFromRobotRequest)
(setf (get explorer::DistanceFromRobot :response) explorer::DistanceFromRobotResponse)

(defmethod explorer::DistanceFromRobotRequest
  (:response () (instance explorer::DistanceFromRobotResponse :init)))

(setf (get explorer::DistanceFromRobotRequest :md5sum-) "fcc6a54f128d10ae4d19b273bb4c2682")
(setf (get explorer::DistanceFromRobotRequest :datatype-) "explorer/DistanceFromRobotRequest")
(setf (get explorer::DistanceFromRobotRequest :definition-)
      "float32 x
float32 y
---
uint8 status
uint8 reachable
float32 distance

")

(setf (get explorer::DistanceFromRobotResponse :md5sum-) "fcc6a54f128d10ae4d19b273bb4c2682")
(setf (get explorer::DistanceFromRobotResponse :datatype-) "explorer/DistanceFromRobotResponse")
(setf (get explorer::DistanceFromRobotResponse :definition-)
      "float32 x
float32 y
---
uint8 status
uint8 reachable
float32 distance

")



(provide :explorer/DistanceFromRobot "fcc6a54f128d10ae4d19b273bb4c2682")


