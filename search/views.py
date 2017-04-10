from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .models import *
import json
import requests
from mongoengine import *





def index(request):
    query = request.GET.get("find")
    if query:
        query_resumes = resumes.objects.search_text(query)
        query_resumes_count = resumes.objects.search_text(query).count()
        if (len(query_resumes) > 0):
            context = {'query_resumes': query_resumes, 'query_resumes_count': query_resumes_count}
            #context = {'all_resumes': query_resumes, 'all_resumes_count': query_resumes_count}
            return render(request, 'search/search.html', context)
        else:
            raise Http404("Non of the resumes contain: %s" % (query))
            #return HttpResponse(query)
    else:
        all_resumes = resumes.objects.all()
        all_resumes_count = resumes.objects.all().count()
        context = {'all_resumes': all_resumes, 'all_resumes_count': all_resumes_count}
        return render(request, 'search/index.html', context)
        #return HttpResponse(template.render(context, request))


def detail(request, resumes_id):
    resume = resumes.objects(id=resumes_id)

    try:
        resume_str = resume.to_json()
        resume_list = json.loads(resume_str)

        if (len(resume) > 0):
            return render(request, 'search/detail.html', {'resume': resume_list[0]})
        else:
            raise Http404("Resume does not exist")
    except:
        raise Http404("Resume does not exist")








