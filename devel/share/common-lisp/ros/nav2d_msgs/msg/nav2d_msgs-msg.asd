
(cl:in-package :asdf)

(defsystem "nav2d_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :sensor_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "LocalizedScan" :depends-on ("_package_LocalizedScan"))
    (:file "_package_LocalizedScan" :depends-on ("_package"))
    (:file "RobotPose" :depends-on ("_package_RobotPose"))
    (:file "_package_RobotPose" :depends-on ("_package"))
  ))