from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapp.models import Contactus
from myapp.serializer import ContactusSerializer


@csrf_exempt
def Contact_list(request):

    if request.method=='GET':
        contacts=Contactus.objects.all()
        serializer=ContactusSerializer(contacts, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=ContactusSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.data,status=400)


@csrf_exempt
def Contact_details(request, pk):

    # Retrieve, update or delete

    try:
        contacts = Contactus.objects.get(pk=pk)
    except Contactus.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ContactusSerializer(contacts)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ContactusSerializer(contacts, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.data, status=400)

    elif request.method == 'DELETE':
        contacts.delete()
        return HttpResponse(status=204)

