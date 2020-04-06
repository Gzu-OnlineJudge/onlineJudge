from django.urls import path, re_path
from Api import views

urlpatterns_Contest = [
    path('contest/', views.ContestApi.GetContestPage.as_view(), name='contests'),
    path('contest/<match_id>/', views.ContestShowContent.as_view(), name='contestContent'),
    path('contest/<int:match_id>/status/', views.ContestGetStatus.as_view(), name='contestContentStatus'),
    # re_path(r'^contest/problems/(?P<match_id>\d+)/$', views.ContestShowContent.as_view(), name='contest_pro'),
    path('test/', views.UserApi.Test.as_view(), name ='test'),
]