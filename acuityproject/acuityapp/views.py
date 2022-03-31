# from crypt import methods
from django.shortcuts import render
# from html5lib import serialize
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for task
from .serializers import TaskSerializer, AssessSerializer, UserSerializer
# Task model
from .models import Task, Assess, User

from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.response import Response 
from django.conf import settings

# Create your views here.

from django.utils.decorators import method_decorator
from rest_framework import viewsets, status

class AssessViewSet(viewsets.ModelViewSet):
    queryset = Assess.objects.all()
    serializer_class = AssessSerializer
    #permission_classes = [permissions.IsAuthenticated]
    
    def create(self, validated_data):
        user = validated_data.user
        toUser = User.objects.get(pk=validated_data.data['toUser'])
        score = validated_data.data['score']  
        comment = validated_data.data['comment']
        Assess.objects.create(fromUser=user, toUser=toUser, score=score, comment=comment).save()
        
        toUser.update_mean()
        
        return Response({'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def get_asc(self, request):
        user = User.objects.all().order_by('score_mean')

        return Response(UserSerializer.data)

        

@csrf_exempt
def tasks(request):
    if(request.method == 'GET'):
        # get all the tasks
        tasks = Task.objects.all()
        # serialize the task data
        serializer = TaskSerializer(tasks, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = TaskSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def task_detail(request, pk):
    print(pk)
    try:
        # obtain the task with the passed id.
        task = Task.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)  
    if(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = TaskSerializer(task, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # if okay, save it on the database
            serializer.save() 
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the task
        task.delete() 
        # return a no content response.
        return HttpResponse(status=204) 
    elif(request.method == 'GET'):
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data)
        