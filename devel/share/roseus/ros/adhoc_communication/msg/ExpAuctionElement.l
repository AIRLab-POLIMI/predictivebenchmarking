;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::ExpAuctionElement)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'ExpAuctionElement (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::EXPAUCTIONELEMENT")
  (make-package "ADHOC_COMMUNICATION::EXPAUCTIONELEMENT"))

(in-package "ROS")
;;//! \htmlinclude ExpAuctionElement.msg.html


(defclass adhoc_communication::ExpAuctionElement
  :super ros::object
  :slots (_id _detected_by_robot_str ))

(defmethod adhoc_communication::ExpAuctionElement
  (:init
   (&key
    ((:id __id) 0)
    ((:detected_by_robot_str __detected_by_robot_str) "")
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _detected_by_robot_str (string __detected_by_robot_str))
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:detected_by_robot_str
   (&optional __detected_by_robot_str)
   (if __detected_by_robot_str (setq _detected_by_robot_str __detected_by_robot_str)) _detected_by_robot_str)
  (:serialization-length
   ()
   (+
    ;; int64 _id
    8
    ;; string _detected_by_robot_str
    4 (length _detected_by_robot_str)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _id
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _id (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _id) (= (length (_id . bv)) 2)) ;; bignum
              (write-long (ash (elt (_id . bv) 0) 0) s)
              (write-long (ash (elt (_id . bv) 1) -1) s))
             ((and (class _id) (= (length (_id . bv)) 1)) ;; big1
              (write-long (elt (_id . bv) 0) s)
              (write-long (if (>= _id 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _id s)(write-long (if (>= _id 0) 0 #xffffffff) s)))
     ;; string _detected_by_robot_str
       (write-long (length _detected_by_robot_str) s) (princ _detected_by_robot_str s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _id
#+(or :alpha :irix6 :x86_64)
      (setf _id (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _id (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; string _detected_by_robot_str
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _detected_by_robot_str (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get adhoc_communication::ExpAuctionElement :md5sum-) "4c7924311e9f149f7f5025e4bf173fd7")
(setf (get adhoc_communication::ExpAuctionElement :datatype-) "adhoc_communication/ExpAuctionElement")
(setf (get adhoc_communication::ExpAuctionElement :definition-)
      "int64 id
string detected_by_robot_str

")



(provide :adhoc_communication/ExpAuctionElement "4c7924311e9f149f7f5025e4bf173fd7")


