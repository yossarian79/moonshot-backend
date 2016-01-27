from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.QuestionList.as_view(),name='question_list'),
   url(r'^(?P<pk>[0-9]+)/', views.QuestionDetail.as_view(),name='question_detail'),
   # url(r'^$',views.QuestionList.as_view(),name='question_list'),
   # url(r'^(?P<pk>[0-9]+)/$',views.QuestionDetail.as_view(),name='question_detail'),
   #  url(r'^create/$',views.QuestionCreate.as_view(),name='question_create'),
   # url(r'^(?P<pk>[0-9]+)/update/$',views.QuestionUpdate.as_view(),name='question_edit'),
   # url(r'^(?P<pk>[0-9]+)/delete/$',views.QuestionDelete.as_view(),name='question_delete'),
]