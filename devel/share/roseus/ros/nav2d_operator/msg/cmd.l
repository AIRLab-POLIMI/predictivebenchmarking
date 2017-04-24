;; Auto-generated. Do not edit!


(when (boundp 'nav2d_operator::cmd)
  (if (not (find-package "NAV2D_OPERATOR"))
    (make-package "NAV2D_OPERATOR"))
  (shadow 'cmd (find-package "NAV2D_OPERATOR")))
(unless (find-package "NAV2D_OPERATOR::CMD")
  (make-package "NAV2D_OPERATOR::CMD"))

(in-package "ROS")
;;//! \htmlinclude cmd.msg.html


(defclass nav2d_operator::cmd
  :super ros::object
  :slots (_Velocity _Turn _Mode ))

(defmethod nav2d_operator::cmd
  (:init
   (&key
    ((:Velocity __Velocity) 0.0)
    ((:Turn __Turn) 0.0)
    ((:Mode __Mode) 0)
    )
   (send-super :init)
   (setq _Velocity (float __Velocity))
   (setq _Turn (float __Turn))
   (setq _Mode (round __Mode))
   self)
  (:Velocity
   (&optional __Velocity)
   (if __Velocity (setq _Velocity __Velocity)) _Velocity)
  (:Turn
   (&optional __Turn)
   (if __Turn (setq _Turn __Turn)) _Turn)
  (:Mode
   (&optional __Mode)
   (if __Mode (setq _Mode __Mode)) _Mode)
  (:serialization-length
   ()
   (+
    ;; float64 _Velocity
    8
    ;; float64 _Turn
    8
    ;; int8 _Mode
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _Velocity
       (sys::poke _Velocity (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Turn
       (sys::poke _Turn (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int8 _Mode
       (write-byte _Mode s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _Velocity
     (setq _Velocity (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Turn
     (setq _Turn (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int8 _Mode
     (setq _Mode (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _Mode 127) (setq _Mode (- _Mode 256)))
   ;;
   self)
  )

(setf (get nav2d_operator::cmd :md5sum-) "90c9a043660646e2102f124332ecb8b7")
(setf (get nav2d_operator::cmd :datatype-) "nav2d_operator/cmd")
(setf (get nav2d_operator::cmd :definition-)
      "float64 Velocity
float64 Turn
int8    Mode

")



(provide :nav2d_operator/cmd "90c9a043660646e2102f124332ecb8b7")


