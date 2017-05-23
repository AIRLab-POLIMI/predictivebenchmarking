
(cl:in-package :asdf)

(defsystem "energy_mgmt-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AuctionResult" :depends-on ("_package_AuctionResult"))
    (:file "_package_AuctionResult" :depends-on ("_package"))
    (:file "battery_state" :depends-on ("_package_battery_state"))
    (:file "_package_battery_state" :depends-on ("_package"))
  ))