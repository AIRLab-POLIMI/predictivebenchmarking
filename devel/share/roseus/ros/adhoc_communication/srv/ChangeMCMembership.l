;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::ChangeMCMembership)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'ChangeMCMembership (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::CHANGEMCMEMBERSHIP")
  (make-package "ADHOC_COMMUNICATION::CHANGEMCMEMBERSHIP"))
(unless (find-package "ADHOC_COMMUNICATION::CHANGEMCMEMBERSHIPREQUEST")
  (make-package "ADHOC_COMMUNICATION::CHANGEMCMEMBERSHIPREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::CHANGEMCMEMBERSHIPRESPONSE")
  (make-package "ADHOC_COMMUNICATION::CHANGEMCMEMBERSHIPRESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::ChangeMCMembershipRequest
  :super ros::object
  :slots (_group_name _action ))

(defmethod adhoc_communication::ChangeMCMembershipRequest
  (:init
   (&key
    ((:group_name __group_name) "")
    ((:action __action) 0)
    )
   (send-super :init)
   (setq _group_name (string __group_name))
   (setq _action (round __action))
   self)
  (:group_name
   (&optional __group_name)
   (if __group_name (setq _group_name __group_name)) _group_name)
  (:action
   (&optional __action)
   (if __action (setq _action __action)) _action)
  (:serialization-length
   ()
   (+
    ;; string _group_name
    4 (length _group_name)
    ;; uint8 _action
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _group_name
       (write-long (length _group_name) s) (princ _group_name s)
     ;; uint8 _action
       (write-byte _action s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _group_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _group_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; uint8 _action
     (setq _action (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(defclass adhoc_communication::ChangeMCMembershipResponse
  :super ros::object
  :slots (_status ))

(defmethod adhoc_communication::ChangeMCMembershipResponse
  (:init
   (&key
    ((:status __status) 0)
    )
   (send-super :init)
   (setq _status (round __status))
   self)
  (:status
   (&optional __status)
   (if __status (setq _status __status)) _status)
  (:serialization-length
   ()
   (+
    ;; uint8 _status
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _status
       (write-byte _status s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _status
     (setq _status (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(defclass adhoc_communication::ChangeMCMembership
  :super ros::object
  :slots ())

(setf (get adhoc_communication::ChangeMCMembership :md5sum-) "49d7b72f6cfca8396fbad0de3d98f799")
(setf (get adhoc_communication::ChangeMCMembership :datatype-) "adhoc_communication/ChangeMCMembership")
(setf (get adhoc_communication::ChangeMCMembership :request) adhoc_communication::ChangeMCMembershipRequest)
(setf (get adhoc_communication::ChangeMCMembership :response) adhoc_communication::ChangeMCMembershipResponse)

(defmethod adhoc_communication::ChangeMCMembershipRequest
  (:response () (instance adhoc_communication::ChangeMCMembershipResponse :init)))

(setf (get adhoc_communication::ChangeMCMembershipRequest :md5sum-) "49d7b72f6cfca8396fbad0de3d98f799")
(setf (get adhoc_communication::ChangeMCMembershipRequest :datatype-) "adhoc_communication/ChangeMCMembershipRequest")
(setf (get adhoc_communication::ChangeMCMembershipRequest :definition-)
      "string group_name
uint8 action
---
uint8 status

")

(setf (get adhoc_communication::ChangeMCMembershipResponse :md5sum-) "49d7b72f6cfca8396fbad0de3d98f799")
(setf (get adhoc_communication::ChangeMCMembershipResponse :datatype-) "adhoc_communication/ChangeMCMembershipResponse")
(setf (get adhoc_communication::ChangeMCMembershipResponse :definition-)
      "string group_name
uint8 action
---
uint8 status

")



(provide :adhoc_communication/ChangeMCMembership "49d7b72f6cfca8396fbad0de3d98f799")


