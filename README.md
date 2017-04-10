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
  * As of now due to some bug, we need to create mongodb database and indexes. Following are the steps using cli.
    * mongo
    * use resumesdepot
    * db.createUser({user: "user",pwd: "securityrock",roles: [ "readWrite", "dbAdmin" ]})
    * db.resumes.ensureIndex({"$**":"text"})
   * /etc/init.d/start_webserver
   

# How To Use This Application:
* Following is representation of home page of this application. It provides some information about this app.
![](https://github.com/chiragadm/resumesdepot/blob/master/docs/home.jpeg)
* Following is representation of upload page. Resumes can be uploaded from here to the database.
![](https://github.com/chiragadm/resumesdepot/blob/master/docs/upload.jpeg)
* Following is representation of search page. It can provide all the resumes in database or you may search for specific ones.
![](https://github.com/chiragadm/resumesdepot/blob/master/docs/search.jpeg)
* Following is representation of detail resume page. Once you click on specific resume, it will take you to this page.
![](https://github.com/chiragadm/resumesdepot/blob/master/docs/detail.jpeg)
