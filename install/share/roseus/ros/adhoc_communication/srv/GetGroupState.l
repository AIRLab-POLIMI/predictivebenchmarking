;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::GetGroupState)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'GetGroupState (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::GETGROUPSTATE")
  (make-package "ADHOC_COMMUNICATION::GETGROUPSTATE"))
(unless (find-package "ADHOC_COMMUNICATION::GETGROUPSTATEREQUEST")
  (make-package "ADHOC_COMMUNICATION::GETGROUPSTATEREQUEST"))
(unless (find-package "ADHOC_COMMUNICATION::GETGROUPSTATERESPONSE")
  (make-package "ADHOC_COMMUNICATION::GETGROUPSTATERESPONSE"))

(in-package "ROS")





(defclass adhoc_communication::GetGroupStateRequest
  :super ros::object
  :slots (_group_name ))

(defmethod adhoc_communication::GetGroupStateRequest
  (:init
   (&key
    ((:group_name __group_name) "")
    )
   (send-super :init)
   (setq _group_name (string __group_name))
   self)
  (:group_name
   (&optional __group_name)
   (if __group_name (setq _group_name __group_name)) _group_name)
  (:serialization-length
   ()
   (+
    ;; string _group_name
    4 (length _group_name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _group_name
       (write-long (length _group_name) s) (princ _group_name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _group_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _group_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass adhoc_communication::GetGroupStateResponse
  :super ros::object
  :slots (_member _activated _connected _root _joining _route_uplink _downlinks ))

(defmethod adhoc_communication::GetGroupStateResponse
  (:init
   (&key
    ((:member __member) nil)
    ((:activated __activated) nil)
    ((:connected __connected) nil)
    ((:root __root) nil)
    ((:joining __joining) nil)
    ((:route_uplink __route_uplink) "")
    ((:downlinks __downlinks) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _member __member)
   (setq _activated __activated)
   (setq _connected __connected)
   (setq _root __root)
   (setq _joining __joining)
   (setq _route_uplink (string __route_uplink))
   (setq _downlinks __downlinks)
   self)
  (:member
   (&optional __member)
   (if __member (setq _member __member)) _member)
  (:activated
   (&optional __activated)
   (if __activated (setq _activated __activated)) _activated)
  (:connected
   (&optional __connected)
   (if __connected (setq _connected __connected)) _connected)
  (:root
   (&optional __root)
   (if __root (setq _root __root)) _root)
  (:joining
   (&optional __joining)
   (if __joining (setq _joining __joining)) _joining)
  (:route_uplink
   (&optional __route_uplink)
   (if __route_uplink (setq _route_uplink __route_uplink)) _route_uplink)
  (:downlinks
   (&optional __downlinks)
   (if __downlinks (setq _downlinks __downlinks)) _downlinks)
  (:serialization-length
   ()
   (+
    ;; bool _member
    1
    ;; bool _activated
    1
    ;; bool _connected
    1
    ;; bool _root
    1
    ;; bool _joining
    1
    ;; string _route_uplink
    4 (length _route_uplink)
    ;; string[] _downlinks
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _downlinks)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _member
       (if _member (write-byte -1 s) (write-byte 0 s))
     ;; bool _activated
       (if _activated (write-byte -1 s) (write-byte 0 s))
     ;; bool _connected
       (if _connected (write-byte -1 s) (write-byte 0 s))
     ;; bool _root
       (if _root (write-byte -1 s) (write-byte 0 s))
     ;; bool _joining
       (if _joining (write-byte -1 s) (write-byte 0 s))
     ;; string _route_uplink
       (write-long (length _route_uplink) s) (princ _route_uplink s)
     ;; string[] _downlinks
     (write-long (length _downlinks) s)
     (dolist (elem _downlinks)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _member
     (setq _member (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _activated
     (setq _activated (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _connected
     (setq _connected (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _root
     (setq _root (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _joining
     (setq _joining (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _route_uplink
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _route_uplink (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string[] _downlinks
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _downlinks (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _downlinks i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(defclass adhoc_communication::GetGroupState
  :super ros::object
  :slots ())

(setf (get adhoc_communication::GetGroupState :md5sum-) "3fd78af244ca7820f4d762caa767ec74")
(setf (get adhoc_communication::GetGroupState :datatype-) "adhoc_communication/GetGroupState")
(setf (get adhoc_communication::GetGroupState :request) adhoc_communication::GetGroupStateRequest)
(setf (get adhoc_communication::GetGroupState :response) adhoc_communication::GetGroupStateResponse)

(defmethod adhoc_communication::GetGroupStateRequest
  (:response () (instance adhoc_communication::GetGroupStateResponse :init)))

(setf (get adhoc_communication::GetGroupStateRequest :md5sum-) "3fd78af244ca7820f4d762caa767ec74")
(setf (get adhoc_communication::GetGroupStateRequest :datatype-) "adhoc_communication/GetGroupStateRequest")
(setf (get adhoc_communication::GetGroupStateRequest :definition-)
      "string group_name
---
bool member
bool activated
bool connected
bool root
bool joining
string route_uplink
string[] downlinks

")

(setf (get adhoc_communication::GetGroupStateResponse :md5sum-) "3fd78af244ca7820f4d762caa767ec74")
(setf (get adhoc_communication::GetGroupStateResponse :datatype-) "adhoc_communication/GetGroupStateResponse")
(setf (get adhoc_communication::GetGroupStateResponse :definition-)
      "string group_name
---
bool member
bool activated
bool connected
bool root
bool joining
string route_uplink
string[] downlinks

")



(provide :adhoc_communication/GetGroupState "3fd78af244ca7820f4d762caa767ec74")


