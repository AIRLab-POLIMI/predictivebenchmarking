Udev rules
==========

Udev Rules needed by the robocom
To install udev rules, execute:

sudo cp $(rospack find robocom)/udev/* /etc/udev/rules.d/
sudo udevadm control --reload-rules && sudo service udev restart && sudo udevadm trigger

