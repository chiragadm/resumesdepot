
from django.shortcuts import render
# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from resumesdepot.settings import BASE_DIR
#from .handle_uploaded_file import handle_uploaded_file
from .handle_uploaded_file import verify, save_to_db



def index(request):
    if request.method == 'POST' and request.FILES['upload_file']:
        myfile = request.FILES['upload_file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        file_path = BASE_DIR + uploaded_file_url
        verify_info = verify(file_path)
        if verify_info["isjson"] == True and verify_info["error"] == False:
            save_check = save_to_db(file_path)
            if save_check == True:
                context = {'upload_info': "Congratulations: Resume uploaded into database!"}
                return render(request, 'upload/index.html', context)
            else:
                context = {'upload_info': "There was issue saving resume to database. :( Please try again!"}
                return render(request, 'upload/index.html', context)
        elif verify_info["isjson"] == True and verify_info["error"] == True:
            e_info = ("We encounter issue with your resume file. Please look at following error:\n%s" % verify_info['info'])
            context = {'upload_info': e_info}
            return render(request, 'upload/index.html', context)
        else:
            context = {'upload_info': "Uploaded file is not in JSON format. Please upload JSON format file!"}
            return render(request, 'upload/index.html', context)

    else:
        return render(request, 'upload/index.html')




