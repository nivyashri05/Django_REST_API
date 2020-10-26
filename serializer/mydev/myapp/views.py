from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapp.models import Collegetb
from myapp.serialzer import CollegetbSerializer


@csrf_exempt
def College_details(request):
    if request.method=='GET':
        contacts=Collegetb.objects.all()
        serializer=CollegetbSerializer(contacts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=CollegetbSerializer(data=data)
        print(data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.data,status=400)

