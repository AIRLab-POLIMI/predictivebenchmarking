;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::CMgrRobotUpdate)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'CMgrRobotUpdate (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::CMGRROBOTUPDATE")
  (make-package "ADHOC_COMMUNICATION::CMGRROBOTUPDATE"))

(in-package "ROS")
;;//! \htmlinclude CMgrRobotUpdate.msg.html


(defclass adhoc_communication::CMgrRobotUpdate
  :super ros::object
  :slots (_robot_name _capabilities _energy _dimensions _status _neighbors ))

(defmethod adhoc_communication::CMgrRobotUpdate
  (:init
   (&key
    ((:robot_name __robot_name) "")
    ((:capabilities __capabilities) "")
    ((:energy __energy) 0.0)
    ((:dimensions __dimensions) (instance adhoc_communication::CMgrDimensions :init))
    ((:status __status) "")
    ((:neighbors __neighbors) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _robot_name (string __robot_name))
   (setq _capabilities (string __capabilities))
   (setq _energy (float __energy))
   (setq _dimensions __dimensions)
   (setq _status (string __status))
   (setq _neighbors __neighbors)
   self)
  (:robot_name
   (&optional __robot_name)
   (if __robot_name (setq _robot_name __robot_name)) _robot_name)
  (:capabilities
   (&optional __capabilities)
   (if __capabilities (setq _capabilities __capabilities)) _capabilities)
  (:energy
   (&optional __energy)
   (if __energy (setq _energy __energy)) _energy)
  (:dimensions
   (&rest __dimensions)
   (if (keywordp (car __dimensions))
       (send* _dimensions __dimensions)
     (progn
       (if __dimensions (setq _dimensions (car __dimensions)))
       _dimensions)))
  (:status
   (&optional __status)
   (if __status (setq _status __status)) _status)
  (:neighbors
   (&optional __neighbors)
   (if __neighbors (setq _neighbors __neighbors)) _neighbors)
  (:serialization-length
   ()
   (+
    ;; string _robot_name
    4 (length _robot_name)
    ;; string _capabilities
    4 (length _capabilities)
    ;; float32 _energy
    4
    ;; adhoc_communication/CMgrDimensions _dimensions
    (send _dimensions :serialization-length)
    ;; string _status
    4 (length _status)
    ;; string[] _neighbors
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _neighbors)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _robot_name
       (write-long (length _robot_name) s) (princ _robot_name s)
     ;; string _capabilities
       (write-long (length _capabilities) s) (princ _capabilities s)
     ;; float32 _energy
       (sys::poke _energy (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; adhoc_communication/CMgrDimensions _dimensions
       (send _dimensions :serialize s)
     ;; string _status
       (write-long (length _status) s) (princ _status s)
     ;; string[] _neighbors
     (write-long (length _neighbors) s)
     (dolist (elem _neighbors)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _robot_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _robot_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _capabilities
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _capabilities (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _energy
     (setq _energy (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; adhoc_communication/CMgrDimensions _dimensions
     (send _dimensions :deserialize buf ptr-) (incf ptr- (send _dimensions :serialization-length))
   ;; string _status
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _status (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string[] _neighbors
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _neighbors (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _neighbors i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(setf (get adhoc_communication::CMgrRobotUpdate :md5sum-) "624d872396e6c4effefdaa51af9e8904")
(setf (get adhoc_communication::CMgrRobotUpdate :datatype-) "adhoc_communication/CMgrRobotUpdate")
(setf (get adhoc_communication::CMgrRobotUpdate :definition-)
      "string robot_name
string capabilities
float32 energy
adhoc_communication/CMgrDimensions dimensions
string status
string[] neighbors

================================================================================
MSG: adhoc_communication/CMgrDimensions
float32 x
float32 y
float32 z

")



(provide :adhoc_communication/CMgrRobotUpdate "624d872396e6c4effefdaa51af9e8904")


