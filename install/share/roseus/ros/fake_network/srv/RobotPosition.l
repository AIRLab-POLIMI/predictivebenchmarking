;; Auto-generated. Do not edit!


(when (boundp 'fake_network::RobotPosition)
  (if (not (find-package "FAKE_NETWORK"))
    (make-package "FAKE_NETWORK"))
  (shadow 'RobotPosition (find-package "FAKE_NETWORK")))
(unless (find-package "FAKE_NETWORK::ROBOTPOSITION")
  (make-package "FAKE_NETWORK::ROBOTPOSITION"))
(unless (find-package "FAKE_NETWORK::ROBOTPOSITIONREQUEST")
  (make-package "FAKE_NETWORK::ROBOTPOSITIONREQUEST"))
(unless (find-package "FAKE_NETWORK::ROBOTPOSITIONRESPONSE")
  (make-package "FAKE_NETWORK::ROBOTPOSITIONRESPONSE"))

(in-package "ROS")





(defclass fake_network::RobotPositionRequest
  :super ros::object
  :slots (_s ))

(defmethod fake_network::RobotPositionRequest
  (:init
   (&key
    ((:s __s) "")
    )
   (send-super :init)
   (setq _s (string __s))
   self)
  (:s
   (&optional __s)
   (if __s (setq _s __s)) _s)
  (:serialization-length
   ()
   (+
    ;; string _s
    4 (length _s)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _s
       (write-long (length _s) s) (princ _s s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _s
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _s (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass fake_network::RobotPositionResponse
  :super ros::object
  :slots (_status _x _y ))

(defmethod fake_network::RobotPositionResponse
  (:init
   (&key
    ((:status __status) 0)
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    )
   (send-super :init)
   (setq _status (round __status))
   (setq _x (float __x))
   (setq _y (float __y))
   self)
  (:status
   (&optional __status)
   (if __status (setq _status __status)) _status)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:serialization-length
   ()
   (+
    ;; uint8 _status
    1
    ;; float32 _x
    4
    ;; float32 _y
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _status
       (write-byte _status s)
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _status
     (setq _status (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass fake_network::RobotPosition
  :super ros::object
  :slots ())

(setf (get fake_network::RobotPosition :md5sum-) "23c69c8103af21e37240b074f5348b77")
(setf (get fake_network::RobotPosition :datatype-) "fake_network/RobotPosition")
(setf (get fake_network::RobotPosition :request) fake_network::RobotPositionRequest)
(setf (get fake_network::RobotPosition :response) fake_network::RobotPositionResponse)

(defmethod fake_network::RobotPositionRequest
  (:response () (instance fake_network::RobotPositionResponse :init)))

(setf (get fake_network::RobotPositionRequest :md5sum-) "23c69c8103af21e37240b074f5348b77")
(setf (get fake_network::RobotPositionRequest :datatype-) "fake_network/RobotPositionRequest")
(setf (get fake_network::RobotPositionRequest :definition-)
      "string s
---
uint8 status
float32 x
float32 y

")

(setf (get fake_network::RobotPositionResponse :md5sum-) "23c69c8103af21e37240b074f5348b77")
(setf (get fake_network::RobotPositionResponse :datatype-) "fake_network/RobotPositionResponse")
(setf (get fake_network::RobotPositionResponse :definition-)
      "string s
---
uint8 status
float32 x
float32 y

")



(provide :fake_network/RobotPosition "23c69c8103af21e37240b074f5348b77")


