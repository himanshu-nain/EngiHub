from django.conf.urls import url
import main.views as view

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
    url(r'^myuploads/$', view._my_uploads_, name='my_uploads'),
    url(r'^detail/(?P<id>\d+)$', view.file_details, name='file_detail'),
    url(r'^like/(?P<id>\d+)$', view.like, name='like'),
    url(r'^dislike/(?P<id>\d+)$', view.dislike, name='dislike'),
    url(r'^account/$', view.my_account, name='my_account'),
    url(r'^password/$', view.change_password, name='change_password'),
    url(r'^email/$', view.change_email, name='change_email'),
    url(r'^deleteAccount/$', view.delete_account, name='delete_account'),

]