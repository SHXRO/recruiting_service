from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('careers/', views.VacancyView.as_view(), name='vacancy'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='job_detail'),
    path('review/<int:pk>/', views.JobApplication.as_view(), name="job_application"),
    path('success/', views.Success.as_view(), name='success'),
    path('fail/', views.Fail.as_view(), name='fail'),
    path('<slug:url>/', views.VacancyView.post_category, name='post_category')

]
