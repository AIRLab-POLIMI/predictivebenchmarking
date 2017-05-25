
(cl:in-package :asdf)

(defsystem "nav2d_operator-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "cmd" :depends-on ("_package_cmd"))
    (:file "_package_cmd" :depends-on ("_package"))
  ))