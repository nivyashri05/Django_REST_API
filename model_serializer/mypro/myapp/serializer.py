from rest_framework import serializers
from myapp.models import Contactus


# ModelSerializer

class ContactusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contactus
        fields = ('id','name1', 'phoneno','place','email')
