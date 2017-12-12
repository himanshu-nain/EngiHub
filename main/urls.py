from django.conf.urls import url
import main.views as view
from django.contrib.auth import views as auth_views

app_name = 'main'

urlpatterns = [
    url(r'^$', view.intro, name = 'intro'),
    url(r'^login/$', view._login_, name='login'),
    url(r'^dashboard/$', view._dash_, name='dashboard'),
    url(r'^logout/$', view._logout_,name='logout'),
    url(r'^register/$',view._register_, name='register'),
    url(r'^upload/$',view.upload_file, name='file_upload'),
    url(r'^download/(?P<path>.*)$', view.download_file, name='file_download'),
    url(r'^delete/(?P<id>\d+)$', view.delete_file, name='file_delete'),

]