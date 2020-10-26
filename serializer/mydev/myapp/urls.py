from django.urls import path,include
from myapp.views import College_details

urlpatterns = [

    path('dev', College_details),
]
