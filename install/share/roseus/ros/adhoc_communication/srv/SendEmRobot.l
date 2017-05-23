;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::SendEmRobot)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'SendEmRobot (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::SENDEMROBOT")
  (make-package "ADHOC_COMMUNICATION::SENDEMROBOT"))
(unless (find-package "ADHOC_COMMUNICATION::SENDEMROBOTREQUEST")
  (make-package "ADHOC_COMMUNICATION::SENDEMROBOTREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::SENDEMROBOTRESPONSE")
  (make-package "ADHOC_COMMUNICATION::SENDEMROBOTRESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::SendEmRobotRequest
  :super ros::object
  :slots (_topic _dst_robot _robot ))

(defmethod adhoc_communication::SendEmRobotRequest
  (:init
   (&key
    ((:topic __topic) "")
    ((:dst_robot __dst_robot) "")
    ((:robot __robot) (instance adhoc_communication::EmRobot :init))
    )
   (send-super :init)
   (setq _topic (string __topic))
   (setq _dst_robot (string __dst_robot))
   (setq _robot __robot)
   self)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
  (:dst_robot
   (&optional __dst_robot)
   (if __dst_robot (setq _dst_robot __dst_robot)) _dst_robot)
  (:robot
   (&rest __robot)
   (if (keywordp (car __robot))
       (send* _robot __robot)
     (progn
       (if __robot (setq _robot (car __robot)))
       _robot)))
  (:serialization-length
   ()
   (+
    ;; string _topic
    4 (length _topic)
    ;; string _dst_robot
    4 (length _dst_robot)
    ;; adhoc_communication/EmRobot _robot
    (send _robot :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; string _dst_robot
       (write-long (length _dst_robot) s) (princ _dst_robot s)
     ;; adhoc_communication/EmRobot _robot
       (send _robot :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _dst_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _dst_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; adhoc_communication/EmRobot _robot
     (send _robot :deserialize buf ptr-) (incf ptr- (send _robot :serialization-length))
   ;;
   self)
  )

(defclass adhoc_communication::SendEmRobotResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::SendEmRobotResponse
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

(defclass adhoc_communication::SendEmRobot
  :super ros::object
  :slots ())

(setf (get adhoc_communication::SendEmRobot :md5sum-) "3d9be68bdd2f929d348378e69f0dc7c2")
(setf (get adhoc_communication::SendEmRobot :datatype-) "adhoc_communication/SendEmRobot")
(setf (get adhoc_communication::SendEmRobot :request) adhoc_communication::SendEmRobotRequest)
(setf (get adhoc_communication::SendEmRobot :response) adhoc_communication::SendEmRobotResponse)

(defmethod adhoc_communication::SendEmRobotRequest
  (:response () (instance adhoc_communication::SendEmRobotResponse :init)))

(setf (get adhoc_communication::SendEmRobotRequest :md5sum-) "3d9be68bdd2f929d348378e69f0dc7c2")
(setf (get adhoc_communication::SendEmRobotRequest :datatype-) "adhoc_communication/SendEmRobotRequest")
(setf (get adhoc_communication::SendEmRobotRequest :definition-)
      "string topic
string dst_robot
adhoc_communication/EmRobot robot

================================================================================
MSG: adhoc_communication/EmRobot
int32 id
int32 state # see energy_mgmt/docking.h
int32 selected_ds #the id of the docking stationc currelty selected by the robot to recharge
float32 x    #robot x-coordinate (in the reference system of the sending robot, not in the one of the receiver)
float32 y    #robot y-coordinate (in the reference system of the sending robot, not in the one of the receiver)
---
uint8 status

")

(setf (get adhoc_communication::SendEmRobotResponse :md5sum-) "3d9be68bdd2f929d348378e69f0dc7c2")
(setf (get adhoc_communication::SendEmRobotResponse :datatype-) "adhoc_communication/SendEmRobotResponse")
(setf (get adhoc_communication::SendEmRobotResponse :definition-)
      "string topic
string dst_robot
adhoc_communication/EmRobot robot

================================================================================
MSG: adhoc_communication/EmRobot
int32 id
int32 state # see energy_mgmt/docking.h
int32 selected_ds #the id of the docking stationc currelty selected by the robot to recharge
float32 x    #robot x-coordinate (in the reference system of the sending robot, not in the one of the receiver)
float32 y    #robot y-coordinate (in the reference system of the sending robot, not in the one of the receiver)
---
uint8 status

")



(provide :adhoc_communication/SendEmRobot "3d9be68bdd2f929d348378e69f0dc7c2")


