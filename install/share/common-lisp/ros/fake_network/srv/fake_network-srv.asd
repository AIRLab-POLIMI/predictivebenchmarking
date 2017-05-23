
(cl:in-package :asdf)

(defsystem "fake_network-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "RobotPosition" :depends-on ("_package_RobotPosition"))
    (:file "_package_RobotPosition" :depends-on ("_package"))
    (:file "SendMessage" :depends-on ("_package_SendMessage"))
    (:file "_package_SendMessage" :depends-on ("_package"))
  ))