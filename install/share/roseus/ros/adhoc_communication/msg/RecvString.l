;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::RecvString)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'RecvString (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::RECVSTRING")
  (make-package "ADHOC_COMMUNICATION::RECVSTRING"))

(in-package "ROS")
;;//! \htmlinclude RecvString.msg.html


(defclass adhoc_communication::RecvString
  :super ros::object
  :slots (_src_robot _data ))

(defmethod adhoc_communication::RecvString
  (:init
   (&key
    ((:src_robot __src_robot) "")
    ((:data __data) "")
    )
   (send-super :init)
   (setq _src_robot (string __src_robot))
   (setq _data (string __data))
   self)
  (:src_robot
   (&optional __src_robot)
   (if __src_robot (setq _src_robot __src_robot)) _src_robot)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; string _src_robot
    4 (length _src_robot)
    ;; string _data
    4 (length _data)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _src_robot
       (write-long (length _src_robot) s) (princ _src_robot s)
     ;; string _data
       (write-long (length _data) s) (princ _data s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _src_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _src_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _data
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _data (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get adhoc_communication::RecvString :md5sum-) "357efa7118aea6ce32be041203afb4ca")
(setf (get adhoc_communication::RecvString :datatype-) "adhoc_communication/RecvString")
(setf (get adhoc_communication::RecvString :definition-)
      "string src_robot
string data

")



(provide :adhoc_communication/RecvString "357efa7118aea6ce32be041203afb4ca")


