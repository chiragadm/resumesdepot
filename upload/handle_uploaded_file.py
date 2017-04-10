import json
import subprocess
from resumesdepot.settings import _MONGODB_HOST, _MONGODB_NAME, _MONGODB_USER, _MONGODB_PASSWD

_MONGODB_COLLECTION = "resumes"

def try_this(in_var, in_type):
    try:
        if isinstance(in_var, in_type):
            return True
        else:
            return False
    except:
        return False

# Following fuction will verify uploaded file JSON schema
def verify(file):
    with open(file, 'r') as upload_file:
        file_content = upload_file.read()
    upload_file.close()
    try:
        chk_json = json.loads(file_content)
    except:
        rc = {'isjson': False, 'error': True, 'info': "File is not Json"}
        return rc
    try:
        a = try_this(chk_json["basics"], dict)
        if a == False:
            return {'isjson': True, 'error': True, 'info': "No basics object!"}

        a = try_this(chk_json["basics"]["name"], str)
        if a == False:
            return {'isjson': True, 'error': True, 'info': "Issue with basics->name object!"}

        a = try_this(chk_json["basics"]["label"], str)
        if a == False:
            return {'isjson': True, 'error': True, 'info': "Issue with basics->label object!"}

        a = try_this(chk_json["basics"]["email"], str)
        if a == False:
            return {'isjson': True, 'error': True, 'info': "Issue with basics->email object!"}

        a = try_this(chk_json["basics"]["phone"], str)
        if a == False:
            return {'isjson': True, 'error': True, 'info': "Issue with basics->phone object!"}

        a = try_this(chk_json["basics"]["summary"], str)
        if a == False:
            return {'isjson': True, 'error': True, 'info': "Issue with basics->summary object!"}

        a = try_this(chk_json["basics"]["location"], dict)
        if a == False:
            return {'isjson': True, 'error': True, 'info': "Issue with basics->location object!"}

        a = try_this(chk_json["basics"]["location"]["address"], str)
        if a == False:
            return {'isjson': True, 'error': True, 'info': "Issue with basics->location->address object!"}

        a = try_this(chk_json["basics"]["location"]["postalCode"], str)
        if a == False:
            return {'isjson': True, 'error': True, 'info': "Issue with basics->location->postalCode object!"}

        a = try_this(chk_json["basics"]["location"]["city"], str)
        if a == False:
            return {'isjson': True, 'error': True, 'info': "Issue with basics->location->city object!"}

        a = try_this(chk_json["basics"]["location"]["city"], str)
        if a == False:
            return {'isjson': True, 'error': True, 'info': "Issue with basics->location->city object!"}

    except:
            rc = {'isjson': True, 'error': True, 'info': "Issue with basics object in json. Please look at Json file"}
            return rc

    try:
        a = try_this(chk_json["work"], list )
        if a == False:
            return {'isjson': True, 'error': True, 'info': "No work object!"}

        for work_elm in chk_json["work"]:
            a = try_this(work_elm["company"], str)
            if a == False:
                return {'isjson': True, 'error': True, 'info': "Issue with work->company object!"}

            a = try_this(work_elm["position"], str)
            if a == False:
                return {'isjson': True, 'error': True, 'info': "Issue with work->position object!"}

            a = try_this(work_elm["startDate"], str)
            if a == False:
                return {'isjson': True, 'error': True, 'info': "Issue with work->startDate object!"}

            a = try_this(work_elm["endDate"], str)
            if a == False:
                return {'isjson': True, 'error': True, 'info': "Issue with work->endDate object!"}

            a = try_this(work_elm["summary"], str)
            if a == False:
                return {'isjson': True, 'error': True, 'info': "Issue with work->summary object!"}

            a = try_this(work_elm["highlights"], list)
            if a == False:
                return {'isjson': True, 'error': True, 'info': "Issue with work->highlights object!"}

    except:
            rc = {'isjson': True, 'error': True, 'info': "Issue with work object in json. Please look at Json file"}
            return rc

    try:
        a = try_this(chk_json["education"], list )
        if a == False:
            return {'isjson': True, 'error': True, 'info': "No education object!"}

        for education_elm in chk_json["education"]:
            a = try_this(education_elm["institution"], str)
            if a == False:
                return {'isjson': True, 'error': True, 'info': "Issue with education->institution object!"}

            a = try_this(education_elm["area"], str)
            if a == False:
                return {'isjson': True, 'error': True, 'info': "Issue with education->area object!"}

    except:
            rc = {'isjson': True, 'error': True, 'info': "Issue with education object in json. Please look at Json file"}
            return rc

    try:
        a = try_this(chk_json["skills"], list )
        if a == False:
            return {'isjson': True, 'error': True, 'info': "No skills object!"}

        for skills_elm in chk_json["skills"]:
            a = try_this(skills_elm["name"], str)
            if a == False:
                return {'isjson': True, 'error': True, 'info': "Issue with skills->name object!"}

            a = try_this(skills_elm["keywords"], list)
            if a == False:
                return {'isjson': True, 'error': True, 'info': "Issue with skills->keywords object!"}

    except:
            rc = {'isjson': True, 'error': True, 'info': "Issue with skills object in json. Please look at Json file"}
            return rc
        
    rc = {'isjson': True, 'error': False, 'info': None}
    return rc

# Following fuction will save uploaded resume to mongodb.
def save_to_db(file):
    cmd = subprocess.Popen(["mongoimport", "-h", _MONGODB_HOST, "-p", _MONGODB_PASSWD, "-d",
                            _MONGODB_NAME, "-c", _MONGODB_COLLECTION, file], stdout=subprocess.PIPE)
    (cmd_out, cmd_err) = cmd.communicate()
    cmd_err = cmd.wait()
    if cmd_err == 0:
        return True
    else:
        return False


