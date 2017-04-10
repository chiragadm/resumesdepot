#!/usr/bin/bash
mongo 127.0.0.1 <<EOF
use resumesdepot
db.createUser({user: "user",pwd: "securityrock",roles: [ "readWrite", "dbAdmin" ]})
db.resumes.ensureIndex({"$**":"text"})
quit()
EOF
