;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::EmAuction)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'EmAuction (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::EMAUCTION")
  (make-package "ADHOC_COMMUNICATION::EMAUCTION"))

(in-package "ROS")
;;//! \htmlinclude EmAuction.msg.html


(defclass adhoc_communication::EmAuction
  :super ros::object
  :slots (_auction _robot _docking_station _bid ))

(defmethod adhoc_communication::EmAuction
  (:init
   (&key
    ((:auction __auction) 0)
    ((:robot __robot) 0)
    ((:docking_station __docking_station) 0)
    ((:bid __bid) 0.0)
    )
   (send-super :init)
   (setq _auction (round __auction))
   (setq _robot (round __robot))
   (setq _docking_station (round __docking_station))
   (setq _bid (float __bid))
   self)
  (:auction
   (&optional __auction)
   (if __auction (setq _auction __auction)) _auction)
  (:robot
   (&optional __robot)
   (if __robot (setq _robot __robot)) _robot)
  (:docking_station
   (&optional __docking_station)
   (if __docking_station (setq _docking_station __docking_station)) _docking_station)
  (:bid
   (&optional __bid)
   (if __bid (setq _bid __bid)) _bid)
  (:serialization-length
   ()
   (+
    ;; uint32 _auction
    4
    ;; uint32 _robot
    4
    ;; uint32 _docking_station
    4
    ;; float32 _bid
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _auction
       (write-long _auction s)
     ;; uint32 _robot
       (write-long _robot s)
     ;; uint32 _docking_station
       (write-long _docking_station s)
     ;; float32 _bid
       (sys::poke _bid (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _auction
     (setq _auction (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint32 _robot
     (setq _robot (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint32 _docking_station
     (setq _docking_station (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _bid
     (setq _bid (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get adhoc_communication::EmAuction :md5sum-) "942c2474214e04f260e8c0832e6a1dad")
(setf (get adhoc_communication::EmAuction :datatype-) "adhoc_communication/EmAuction")
(setf (get adhoc_communication::EmAuction :definition-)
      "uint32 auction
uint32 robot
uint32 docking_station
float32 bid

")



(provide :adhoc_communication/EmAuction "942c2474214e04f260e8c0832e6a1dad")


