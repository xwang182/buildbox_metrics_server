from django.conf.urls import url
from buildbox_metrics import views

urlpatterns = [
    url(r'^trains/$', views.BuildTrainList.as_view()),
    url(r'^trains/(?P<pk>[0-9]+)$', views.BuildTrainDetail.as_view()),
    url(r'^builds/$', views.BuildList.as_view()),
    url(r'^builds/(?P<pk>[0-9]+)$', views.BuildDetail.as_view()),
    url(r'^deliverables/$', views.DeliverableList.as_view()),
    url(r'^deliverables/(?P<pk>[0-9]+)$', views.DeliverableDetail.as_view()),
]
