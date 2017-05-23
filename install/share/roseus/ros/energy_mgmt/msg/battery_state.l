;; Auto-generated. Do not edit!


(when (boundp 'energy_mgmt::battery_state)
  (if (not (find-package "ENERGY_MGMT"))
    (make-package "ENERGY_MGMT"))
  (shadow 'battery_state (find-package "ENERGY_MGMT")))
(unless (find-package "ENERGY_MGMT::BATTERY_STATE")
  (make-package "ENERGY_MGMT::BATTERY_STATE"))

(in-package "ROS")
;;//! \htmlinclude battery_state.msg.html


(defclass energy_mgmt::battery_state
  :super ros::object
  :slots (_charging _soc _remaining_time_charge _remaining_time_run _remaining_distance ))

(defmethod energy_mgmt::battery_state
  (:init
   (&key
    ((:charging __charging) nil)
    ((:soc __soc) 0.0)
    ((:remaining_time_charge __remaining_time_charge) 0.0)
    ((:remaining_time_run __remaining_time_run) 0.0)
    ((:remaining_distance __remaining_distance) 0.0)
    )
   (send-super :init)
   (setq _charging __charging)
   (setq _soc (float __soc))
   (setq _remaining_time_charge (float __remaining_time_charge))
   (setq _remaining_time_run (float __remaining_time_run))
   (setq _remaining_distance (float __remaining_distance))
   self)
  (:charging
   (&optional __charging)
   (if __charging (setq _charging __charging)) _charging)
  (:soc
   (&optional __soc)
   (if __soc (setq _soc __soc)) _soc)
  (:remaining_time_charge
   (&optional __remaining_time_charge)
   (if __remaining_time_charge (setq _remaining_time_charge __remaining_time_charge)) _remaining_time_charge)
  (:remaining_time_run
   (&optional __remaining_time_run)
   (if __remaining_time_run (setq _remaining_time_run __remaining_time_run)) _remaining_time_run)
  (:remaining_distance
   (&optional __remaining_distance)
   (if __remaining_distance (setq _remaining_distance __remaining_distance)) _remaining_distance)
  (:serialization-length
   ()
   (+
    ;; bool _charging
    1
    ;; float32 _soc
    4
    ;; float32 _remaining_time_charge
    4
    ;; float32 _remaining_time_run
    4
    ;; float32 _remaining_distance
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _charging
       (if _charging (write-byte -1 s) (write-byte 0 s))
     ;; float32 _soc
       (sys::poke _soc (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _remaining_time_charge
       (sys::poke _remaining_time_charge (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _remaining_time_run
       (sys::poke _remaining_time_run (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _remaining_distance
       (sys::poke _remaining_distance (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _charging
     (setq _charging (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float32 _soc
     (setq _soc (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _remaining_time_charge
     (setq _remaining_time_charge (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _remaining_time_run
     (setq _remaining_time_run (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _remaining_distance
     (setq _remaining_distance (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get energy_mgmt::battery_state :md5sum-) "ae34ca1536c302c535b231631ea2d4bc")
(setf (get energy_mgmt::battery_state :datatype-) "energy_mgmt/battery_state")
(setf (get energy_mgmt::battery_state :definition-)
      "bool charging
float32 soc
float32 remaining_time_charge
float32 remaining_time_run
float32 remaining_distance

")



(provide :energy_mgmt/battery_state "ae34ca1536c302c535b231631ea2d4bc")


