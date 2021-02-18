from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('registration/',views.registration),
    path('registration/showStudents/',views.showStudents),
]