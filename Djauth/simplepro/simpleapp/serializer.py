from rest_framework import serializers
from django.contrib.auth.models import User
from simpleapp.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=('age','bio')


class UserSerializers(serializers.ModelSerializer):
    person=PersonSerializer()

    class Meta:
        model=User
        fields=('id','username','password','person')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self,validate_data):
        print(validate_data)
        person_data=validate_data.pop('person')
        user=User.objects.create(**validate_data)
        user.person=Person.objects.create(user=user,**person_data)
        user.save()
        return user
