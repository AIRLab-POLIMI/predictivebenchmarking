
(cl:in-package :asdf)

(defsystem "explorer-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Frontier" :depends-on ("_package_Frontier"))
    (:file "_package_Frontier" :depends-on ("_package"))
    (:file "Speed" :depends-on ("_package_Speed"))
    (:file "_package_Speed" :depends-on ("_package"))
  ))