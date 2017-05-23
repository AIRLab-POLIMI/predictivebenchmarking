;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::SendEmDockingStation)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'SendEmDockingStation (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::SENDEMDOCKINGSTATION")
  (make-package "ADHOC_COMMUNICATION::SENDEMDOCKINGSTATION"))
(unless (find-package "ADHOC_COMMUNICATION::SENDEMDOCKINGSTATIONREQUEST")
  (make-package "ADHOC_COMMUNICATION::SENDEMDOCKINGSTATIONREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::SENDEMDOCKINGSTATIONRESPONSE")
  (make-package "ADHOC_COMMUNICATION::SENDEMDOCKINGSTATIONRESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::SendEmDockingStationRequest
  :super ros::object
  :slots (_topic _dst_robot _docking_station ))

(defmethod adhoc_communication::SendEmDockingStationRequest
  (:init
   (&key
    ((:topic __topic) "")
    ((:dst_robot __dst_robot) "")
    ((:docking_station __docking_station) (instance adhoc_communication::EmDockingStation :init))
    )
   (send-super :init)
   (setq _topic (string __topic))
   (setq _dst_robot (string __dst_robot))
   (setq _docking_station __docking_station)
   self)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
  (:dst_robot
   (&optional __dst_robot)
   (if __dst_robot (setq _dst_robot __dst_robot)) _dst_robot)
  (:docking_station
   (&rest __docking_station)
   (if (keywordp (car __docking_station))
       (send* _docking_station __docking_station)
     (progn
       (if __docking_station (setq _docking_station (car __docking_station)))
       _docking_station)))
  (:serialization-length
   ()
   (+
    ;; string _topic
    4 (length _topic)
    ;; string _dst_robot
    4 (length _dst_robot)
    ;; adhoc_communication/EmDockingStation _docking_station
    (send _docking_station :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; string _dst_robot
       (write-long (length _dst_robot) s) (princ _dst_robot s)
     ;; adhoc_communication/EmDockingStation _docking_station
       (send _docking_station :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _dst_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _dst_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; adhoc_communication/EmDockingStation _docking_station
     (send _docking_station :deserialize buf ptr-) (incf ptr- (send _docking_station :serialization-length))
   ;;
   self)
  )

(defclass adhoc_communication::SendEmDockingStationResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::SendEmDockingStationResponse
  (:init
   (&key
    ((:status __status) 0)
    )
   (send-super :init)
   (setq _status (round __status))
   self)
  (:status
   (&optional __status)
   (if __status (setq _status __status)) _status)
  (:serialization-length
   ()
   (+
    ;; uint8 _status
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _status
       (write-byte _status s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _status
     (setq _status (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(defclass adhoc_communication::SendEmDockingStation
  :super ros::object
  :slots ())

(setf (get adhoc_communication::SendEmDockingStation :md5sum-) "8f86c3f7e9c77062fc3c620d3c267397")
(setf (get adhoc_communication::SendEmDockingStation :datatype-) "adhoc_communication/SendEmDockingStation")
(setf (get adhoc_communication::SendEmDockingStation :request) adhoc_communication::SendEmDockingStationRequest)
(setf (get adhoc_communication::SendEmDockingStation :response) adhoc_communication::SendEmDockingStationResponse)

(defmethod adhoc_communication::SendEmDockingStationRequest
  (:response () (instance adhoc_communication::SendEmDockingStationResponse :init)))

(setf (get adhoc_communication::SendEmDockingStationRequest :md5sum-) "8f86c3f7e9c77062fc3c620d3c267397")
(setf (get adhoc_communication::SendEmDockingStationRequest :datatype-) "adhoc_communication/SendEmDockingStationRequest")
(setf (get adhoc_communication::SendEmDockingStationRequest :definition-)
      "string topic
string dst_robot
adhoc_communication/EmDockingStation docking_station

================================================================================
MSG: adhoc_communication/EmDockingStation
int32 id
float64 x
float64 y
---
uint8 status

")

(setf (get adhoc_communication::SendEmDockingStationResponse :md5sum-) "8f86c3f7e9c77062fc3c620d3c267397")
(setf (get adhoc_communication::SendEmDockingStationResponse :datatype-) "adhoc_communication/SendEmDockingStationResponse")
(setf (get adhoc_communication::SendEmDockingStationResponse :definition-)
      "string topic
string dst_robot
adhoc_communication/EmDockingStation docking_station

================================================================================
MSG: adhoc_communication/EmDockingStation
int32 id
float64 x
float64 y
---
uint8 status

")



(provide :adhoc_communication/SendEmDockingStation "8f86c3f7e9c77062fc3c620d3c267397")


