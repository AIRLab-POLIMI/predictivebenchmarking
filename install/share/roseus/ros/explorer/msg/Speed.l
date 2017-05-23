;; Auto-generated. Do not edit!


(when (boundp 'explorer::Speed)
  (if (not (find-package "EXPLORER"))
    (make-package "EXPLORER"))
  (shadow 'Speed (find-package "EXPLORER")))
(unless (find-package "EXPLORER::SPEED")
  (make-package "EXPLORER::SPEED"))

(in-package "ROS")
;;//! \htmlinclude Speed.msg.html


(defclass explorer::Speed
  :super ros::object
  :slots (_avg_speed ))

(defmethod explorer::Speed
  (:init
   (&key
    ((:avg_speed __avg_speed) 0.0)
    )
   (send-super :init)
   (setq _avg_speed (float __avg_speed))
   self)
  (:avg_speed
   (&optional __avg_speed)
   (if __avg_speed (setq _avg_speed __avg_speed)) _avg_speed)
  (:serialization-length
   ()
   (+
    ;; float32 _avg_speed
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _avg_speed
       (sys::poke _avg_speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _avg_speed
     (setq _avg_speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get explorer::Speed :md5sum-) "ab71c17b247789c29752d16cf36898a8")
(setf (get explorer::Speed :datatype-) "explorer/Speed")
(setf (get explorer::Speed :definition-)
      "float32 avg_speed

")



(provide :explorer/Speed "ab71c17b247789c29752d16cf36898a8")


