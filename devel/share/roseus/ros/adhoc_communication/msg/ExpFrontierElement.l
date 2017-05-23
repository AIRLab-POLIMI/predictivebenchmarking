;; Auto-generated. Do not edit!


(when (boundp 'adhoc_communication::ExpFrontierElement)
  (if (not (find-package "ADHOC_COMMUNICATION"))
    (make-package "ADHOC_COMMUNICATION"))
  (shadow 'ExpFrontierElement (find-package "ADHOC_COMMUNICATION")))
(unless (find-package "ADHOC_COMMUNICATION::EXPFRONTIERELEMENT")
  (make-package "ADHOC_COMMUNICATION::EXPFRONTIERELEMENT"))

(in-package "ROS")
;;//! \htmlinclude ExpFrontierElement.msg.html


(defclass adhoc_communication::ExpFrontierElement
  :super ros::object
  :slots (_id _detected_by_robot_str _detected_by_robot _robot_home_position_x _robot_home_position_y _x_coordinate _y_coordinate ))

(defmethod adhoc_communication::ExpFrontierElement
  (:init
   (&key
    ((:id __id) 0)
    ((:detected_by_robot_str __detected_by_robot_str) "")
    ((:detected_by_robot __detected_by_robot) 0)
    ((:robot_home_position_x __robot_home_position_x) 0.0)
    ((:robot_home_position_y __robot_home_position_y) 0.0)
    ((:x_coordinate __x_coordinate) 0.0)
    ((:y_coordinate __y_coordinate) 0.0)
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _detected_by_robot_str (string __detected_by_robot_str))
   (setq _detected_by_robot (round __detected_by_robot))
   (setq _robot_home_position_x (float __robot_home_position_x))
   (setq _robot_home_position_y (float __robot_home_position_y))
   (setq _x_coordinate (float __x_coordinate))
   (setq _y_coordinate (float __y_coordinate))
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:detected_by_robot_str
   (&optional __detected_by_robot_str)
   (if __detected_by_robot_str (setq _detected_by_robot_str __detected_by_robot_str)) _detected_by_robot_str)
  (:detected_by_robot
   (&optional __detected_by_robot)
   (if __detected_by_robot (setq _detected_by_robot __detected_by_robot)) _detected_by_robot)
  (:robot_home_position_x
   (&optional __robot_home_position_x)
   (if __robot_home_position_x (setq _robot_home_position_x __robot_home_position_x)) _robot_home_position_x)
  (:robot_home_position_y
   (&optional __robot_home_position_y)
   (if __robot_home_position_y (setq _robot_home_position_y __robot_home_position_y)) _robot_home_position_y)
  (:x_coordinate
   (&optional __x_coordinate)
   (if __x_coordinate (setq _x_coordinate __x_coordinate)) _x_coordinate)
  (:y_coordinate
   (&optional __y_coordinate)
   (if __y_coordinate (setq _y_coordinate __y_coordinate)) _y_coordinate)
  (:serialization-length
   ()
   (+
    ;; int64 _id
    8
    ;; string _detected_by_robot_str
    4 (length _detected_by_robot_str)
    ;; int64 _detected_by_robot
    8
    ;; float64 _robot_home_position_x
    8
    ;; float64 _robot_home_position_y
    8
    ;; float64 _x_coordinate
    8
    ;; float64 _y_coordinate
    8
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
     ;; int64 _detected_by_robot
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _detected_by_robot (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _detected_by_robot) (= (length (_detected_by_robot . bv)) 2)) ;; bignum
              (write-long (ash (elt (_detected_by_robot . bv) 0) 0) s)
              (write-long (ash (elt (_detected_by_robot . bv) 1) -1) s))
             ((and (class _detected_by_robot) (= (length (_detected_by_robot . bv)) 1)) ;; big1
              (write-long (elt (_detected_by_robot . bv) 0) s)
              (write-long (if (>= _detected_by_robot 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _detected_by_robot s)(write-long (if (>= _detected_by_robot 0) 0 #xffffffff) s)))
     ;; float64 _robot_home_position_x
       (sys::poke _robot_home_position_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _robot_home_position_y
       (sys::poke _robot_home_position_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _x_coordinate
       (sys::poke _x_coordinate (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y_coordinate
       (sys::poke _y_coordinate (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
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
   ;; int64 _detected_by_robot
#+(or :alpha :irix6 :x86_64)
      (setf _detected_by_robot (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _detected_by_robot (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; float64 _robot_home_position_x
     (setq _robot_home_position_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _robot_home_position_y
     (setq _robot_home_position_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _x_coordinate
     (setq _x_coordinate (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y_coordinate
     (setq _y_coordinate (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get adhoc_communication::ExpFrontierElement :md5sum-) "a783300e6ed76ebb52feb001fc044546")
(setf (get adhoc_communication::ExpFrontierElement :datatype-) "adhoc_communication/ExpFrontierElement")
(setf (get adhoc_communication::ExpFrontierElement :definition-)
      "int64 id
string detected_by_robot_str
int64 detected_by_robot
float64 robot_home_position_x
float64 robot_home_position_y
float64 x_coordinate
float64 y_coordinate

")



(provide :adhoc_communication/ExpFrontierElement "a783300e6ed76ebb52feb001fc044546")


