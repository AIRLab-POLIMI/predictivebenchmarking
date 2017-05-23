
(cl:in-package :asdf)

(defsystem "fake_network-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "NetworkMessage" :depends-on ("_package_NetworkMessage"))
    (:file "_package_NetworkMessage" :depends-on ("_package"))
  ))