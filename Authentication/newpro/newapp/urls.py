from django.urls import path,include
from newapp.views import newapi
urlpatterns = [
    path('new/', view=newapi,name='newapi'),
    path('new/<int:id>/', view=newapi,name='newapi')
]
