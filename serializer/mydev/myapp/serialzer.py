from rest_framework import serializers
from myapp.models import Collegetb

class CollegetbSerializer(serializers.Serializer):
    deptid=serializers.IntegerField()
    deptname = serializers.CharField(max_length=256)
    depthod = serializers.CharField(max_length=256)
    location = serializers.CharField(max_length=256)

    def create(self,validated_data):
        return Collegetb.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.deptid=validated_data.get('deptid',instance.deptid)
        instance.deptname=validated_data.get('deptname',instance.deptname)
        instance.depthod=validated_data.get('depthod',instance.depthod)
        instance.location=validated_data.get('location',instance.location)
        instance.save()
        return instance



