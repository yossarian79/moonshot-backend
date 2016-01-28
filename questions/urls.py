from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.QuestionList.as_view(),name='question_list'),
   url(r'^(?P<pk>[0-9]+)/', views.QuestionDetail.as_view(),name='question_detail'),
  
]