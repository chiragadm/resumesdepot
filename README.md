# ResumesDepot

ResumesDepot is an application that let you store your JSON format based resumes to cloud and query it for later use. It uses Django framework for frontend and mongodb for backend.

# Installation:
Following are prerequisites softwares.
* Linux based OS
* Python3 (prefer 3.4 or above)
* Python3 Modules:
  * django
  * mongoengine
  * requests
* mongodb
* # Ansible Playbook Install Processs:
  * install_with_ansible directory provides ansible-playbook to install this application on AWS ec2 (RehdHat x86 7) instance. You may run following command to install this applicaton.
  * cd install_with_ansible
  * Add your ec2 instance name below [ec2] section in "inventory.txt" file.
  * You will also need your ec2 instance key file. Please keep it handy.
  * Run following command:
  * ansible-playbook -u ec2-user --key-file=YourKeyFile  -i inventory.txt  ./install_resumesdepot_app.yml

