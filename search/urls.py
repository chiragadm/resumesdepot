from django.conf.urls import url
from . import views

app_name = 'search'

urlpatterns = [
    # /search/
    url(r'^$', views.index, name='index'),

    # /search/id/
    url(r'^(?P<resumes_id>[a-zA-Z0-9]{24,24})/$', views.detail, name='detail'),
    #url(r'^(?P<resumes_id>[a-zA-Z0-9]+)/$', views.detail, name='detail'),

    # /search/?find/
    #url(r'^(?P<find_req>/find/[?]find=[a-zA-Z0-9]+)/$', views.find, name='find'),

]
