from django.urls import path
from .views import home, student_api

urlpatterns = [
    path('', home),
    path('student/', student_api),

]
