from django.urls import path
from . import views

app_name = 'sales'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('form/', views.form, name='form'),
    path('submission/', views.submission, name='submission'),
    path('report/', views.report, name='report'),
]
