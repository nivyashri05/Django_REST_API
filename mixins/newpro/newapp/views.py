from newapp.models import Employee
from newapp.serializer import EmployeeSerializer
from rest_framework import generics
from rest_framework import mixins

class Newapi(generics.GenericAPIView, mixins.ListModelMixin,
             mixins.CreateModelMixin,mixins.UpdateModelMixin,
             mixins.RetrieveModelMixin,mixins.DestroyModelMixin):

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    lookup_field = 'id'


    def get(self,request,id=None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request,id=None):
        return self.destroy(request,id)

newapi=Newapi.as_view()