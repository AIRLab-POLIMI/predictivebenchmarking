;; Auto-generated. Do not edit!


(when (boundp 'energy_mgmt::AuctionResult)
  (if (not (find-package "ENERGY_MGMT"))
    (make-package "ENERGY_MGMT"))
  (shadow 'AuctionResult (find-package "ENERGY_MGMT")))
(unless (find-package "ENERGY_MGMT::AUCTIONRESULT")
  (make-package "ENERGY_MGMT::AUCTIONRESULT"))

(in-package "ROS")
;;//! \htmlinclude AuctionResult.msg.html


(defclass energy_mgmt::AuctionResult
  :super ros::object
  :slots (_winner ))

(defmethod energy_mgmt::AuctionResult
  (:init
   (&key
    ((:winner __winner) nil)
    )
   (send-super :init)
   (setq _winner __winner)
   self)
  (:winner
   (&optional __winner)
   (if __winner (setq _winner __winner)) _winner)
  (:serialization-length
   ()
   (+
    ;; bool _winner
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _winner
       (if _winner (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _winner
     (setq _winner (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get energy_mgmt::AuctionResult :md5sum-) "970386071cec2ebdf79afc8a0312c15a")
(setf (get energy_mgmt::AuctionResult :datatype-) "energy_mgmt/AuctionResult")
(setf (get energy_mgmt::AuctionResult :definition-)
      "bool winner

")



(provide :energy_mgmt/AuctionResult "970386071cec2ebdf79afc8a0312c15a")


