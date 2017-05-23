;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::ExpFrontier)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'ExpFrontier (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::EXPFRONTIER")
  (make-package "ADHOC_COMMUNICATION::EXPFRONTIER"))

(in-package "ROS")
;;//! \htmlinclude ExpFrontier.msg.html


(defclass adhoc_communication::ExpFrontier
  :super ros::object
  :slots (_frontier_element ))

(defmethod adhoc_communication::ExpFrontier
  (:init
   (&key
    ((:frontier_element __frontier_element) (let (r) (dotimes (i 0) (push (instance adhoc_communication::ExpFrontierElement :init) r)) r))
    )
   (send-super :init)
   (setq _frontier_element __frontier_element)
   self)
  (:frontier_element
   (&rest __frontier_element)
   (if (keywordp (car __frontier_element))
       (send* _frontier_element __frontier_element)
     (progn
       (if __frontier_element (setq _frontier_element (car __frontier_element)))
       _frontier_element)))
  (:serialization-length
   ()
   (+
    ;; adhoc_communication/ExpFrontierElement[] _frontier_element
    (apply #'+ (send-all _frontier_element :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; adhoc_communication/ExpFrontierElement[] _frontier_element
     (write-long (length _frontier_element) s)
     (dolist (elem _frontier_element)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; adhoc_communication/ExpFrontierElement[] _frontier_element
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _frontier_element (let (r) (dotimes (i n) (push (instance adhoc_communication::ExpFrontierElement :init) r)) r))
     (dolist (elem- _frontier_element)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get adhoc_communication::ExpFrontier :md5sum-) "a022dc7f2d36765e856b2878d8a5476f")
(setf (get adhoc_communication::ExpFrontier :datatype-) "adhoc_communication/ExpFrontier")
(setf (get adhoc_communication::ExpFrontier :definition-)
      "ExpFrontierElement[] frontier_element

================================================================================
MSG: adhoc_communication/ExpFrontierElement
int64 id
string detected_by_robot_str
int64 detected_by_robot
float64 robot_home_position_x
float64 robot_home_position_y
float64 x_coordinate
float64 y_coordinate

")



(provide :adhoc_communication/ExpFrontier "a022dc7f2d36765e856b2878d8a5476f")


