
(cl:in-package :asdf)

(defsystem "map_merger-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :adhoc_communication-msg
)
  :components ((:file "_package")
    (:file "LogMaps" :depends-on ("_package_LogMaps"))
    (:file "_package_LogMaps" :depends-on ("_package"))
    (:file "TransformPoint" :depends-on ("_package_TransformPoint"))
    (:file "_package_TransformPoint" :depends-on ("_package"))
  ))