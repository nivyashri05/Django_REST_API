from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from simpleapp.serializer import UserSerializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class GetAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response=super(GetAuthToken,self).post(request,*args,**kwargs)
        token=Token.objects.get(key=response.data['token'])
        user=User.objects.get(id=token.user_id)
        user_serializer=UserSerializers(user,many=False)
        return Response({'token':token.key,'user':user_serializer.data})