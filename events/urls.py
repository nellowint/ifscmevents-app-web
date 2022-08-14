from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^pendency/$', views.pendencyList, name="pendencyList"),
    url(r'^event/$', views.eventList, name="eventList"),
    url(r'^event/(?P<pk>\d+)/$', views.eventDetail, name="eventDetail"),
    url(r'^event/new/$', views.eventNew, name="eventNew"),
    url(r'^event/(?P<pk>\d+)/edit/$', views.eventEdit, name="eventEdit"),
    url(r'^event/(?P<pk>\d+)/remove/$', views.eventRemove, name="eventRemove"),
    url(r'^speaker/$', views.speakerList, name="speakerList"),
    url(r'^speaker/(?P<pk>\d+)/$', views.speakerDetail, name="speakerDetail"),
    url(r'^speaker/(?P<pk>\d+)/edit/$', views.speakerEdit, name="speakerEdit"),
    url(r'^speaker/(?P<pk>\d+)/remove/$', views.speakerRemove, name="speakerRemove"),
    url(r'^speaker/(?P<pk>\d+)/approve/$', views.speakerApprove, name="speakerApprove"),
    url(r'^talk/(?P<pk>\d+)/$', views.talkDetail, name="talkDetail"),
    url(r'^talk/new/$', views.talkNew, name="talkNew"),
    url(r'^talk/(?P<pk>\d+)/edit/$', views.talkEdit, name="talkEdit"),
    url(r'^talk/(?P<pk>\d+)/remove/$', views.talkRemove, name="talkRemove"),
    url(r'^talk/(?P<pk>\d+)/approve/$', views.talkApprove, name="talkApprove"),
    url(r'^get/event/$', views.eventListJson, name="eventListJson"),
    url(r'^get/event/next/$', views.nextEventListJson, name="nextEventListJson"),
    url(r'^get/event/now/$', views.nowEventListJson, name="nowEventListJson"),
    url(r'^get/event/(?P<pk>\d+)/$', views.eventDetailJson, name="eventDetailJson"),
    url(r'^get/event/(?P<pk>\d+)/talk/$', views.eventTalkListJson, name="eventTalkListJson"),
    url(r'^get/speaker/$', views.speakerListJson, name="speakerListJson"),
    url(r'^get/speaker/(?P<pk>\d+)/$', views.speakerDetailJson, name="speakerDetailJson"),
    url(r'^get/speaker/(?P<pk>\d+)/talk/$', views.speakerTalkJson, name="speakerTalkJson"),
    url(r'^get/talk/$', views.talkListJson, name="talkListJson"),
    url(r'^get/talk/(?P<pk>\d+)/$', views.talkDetailJson, name="talkDetailJson"),
    url(r'^get/talk/(?P<pk>\d+)/speaker/$', views.talkSpeakerJson, name="talkSpeakerJson"),
    url(r'^get/pendency/$', views.pendencyCountJson, name="pendencyCountJson"),
    url(r'^get/object/$', views.objectListJson, name="objectListJson"),
]