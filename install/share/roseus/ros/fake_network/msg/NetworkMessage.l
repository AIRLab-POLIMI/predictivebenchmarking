;; Auto-generated. Do not edit!


(when (boundp 'fake_network::NetworkMessage)
  (if (not (find-package "FAKE_NETWORK"))
    (make-package "FAKE_NETWORK"))
  (shadow 'NetworkMessage (find-package "FAKE_NETWORK")))
(unless (find-package "FAKE_NETWORK::NETWORKMESSAGE")
  (make-package "FAKE_NETWORK::NETWORKMESSAGE"))

(in-package "ROS")
;;//! \htmlinclude NetworkMessage.msg.html


(defclass fake_network::NetworkMessage
  :super ros::object
  :slots (_source_robot _payload _data_type _topic ))

(defmethod fake_network::NetworkMessage
  (:init
   (&key
    ((:source_robot __source_robot) "")
    ((:payload __payload) "")
    ((:data_type __data_type) 0)
    ((:topic __topic) "")
    )
   (send-super :init)
   (setq _source_robot (string __source_robot))
   (setq _payload (string __payload))
   (setq _data_type (round __data_type))
   (setq _topic (string __topic))
   self)
  (:source_robot
   (&optional __source_robot)
   (if __source_robot (setq _source_robot __source_robot)) _source_robot)
  (:payload
   (&optional __payload)
   (if __payload (setq _payload __payload)) _payload)
  (:data_type
   (&optional __data_type)
   (if __data_type (setq _data_type __data_type)) _data_type)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
  (:serialization-length
   ()
   (+
    ;; string _source_robot
    4 (length _source_robot)
    ;; string _payload
    4 (length _payload)
    ;; uint8 _data_type
    1
    ;; string _topic
    4 (length _topic)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _source_robot
       (write-long (length _source_robot) s) (princ _source_robot s)
     ;; string _payload
       (write-long (length _payload) s) (princ _payload s)
     ;; uint8 _data_type
       (write-byte _data_type s)
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _source_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _source_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _payload
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _payload (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; uint8 _data_type
     (setq _data_type (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get fake_network::NetworkMessage :md5sum-) "67d28fd41fb2346145ecac16f2c7c957")
(setf (get fake_network::NetworkMessage :datatype-) "fake_network/NetworkMessage")
(setf (get fake_network::NetworkMessage :definition-)
      "string source_robot
string payload
uint8 data_type
string topic

")



(provide :fake_network/NetworkMessage "67d28fd41fb2346145ecac16f2c7c957")

