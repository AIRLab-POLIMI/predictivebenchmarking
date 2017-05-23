;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::MmControl)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'MmControl (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::MMCONTROL")
  (make-package "ADHOC_COMMUNICATION::MMCONTROL"))

(in-package "ROS")
;;//! \htmlinclude MmControl.msg.html


(defclass adhoc_communication::MmControl
  :super ros::object
  :slots (_src_robot _update_numbers ))

(defmethod adhoc_communication::MmControl
  (:init
   (&key
    ((:src_robot __src_robot) "")
    ((:update_numbers __update_numbers) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _src_robot (string __src_robot))
   (setq _update_numbers __update_numbers)
   self)
  (:src_robot
   (&optional __src_robot)
   (if __src_robot (setq _src_robot __src_robot)) _src_robot)
  (:update_numbers
   (&optional __update_numbers)
   (if __update_numbers (setq _update_numbers __update_numbers)) _update_numbers)
  (:serialization-length
   ()
   (+
    ;; string _src_robot
    4 (length _src_robot)
    ;; int32[] _update_numbers
    (* 4    (length _update_numbers)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _src_robot
       (write-long (length _src_robot) s) (princ _src_robot s)
     ;; int32[] _update_numbers
     (write-long (length _update_numbers) s)
     (dotimes (i (length _update_numbers))
       (write-long (elt _update_numbers i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _src_robot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _src_robot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int32[] _update_numbers
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _update_numbers (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _update_numbers i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get adhoc_communication::MmControl :md5sum-) "3d223057e1839a50fdaaef262568a5a7")
(setf (get adhoc_communication::MmControl :datatype-) "adhoc_communication/MmControl")
(setf (get adhoc_communication::MmControl :definition-)
      "string src_robot
int32[] update_numbers

")



(provide :adhoc_communication/MmControl "3d223057e1839a50fdaaef262568a5a7")


