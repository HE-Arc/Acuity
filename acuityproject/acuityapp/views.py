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
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, validated_data):     
        user = validated_data.user
        toUser = User.objects.get(pk=validated_data.data['toUser'])        
        score = validated_data.data['score']  
        comment = validated_data.data['comment']
         
        if user == toUser:
            return Response({'status': status.HTTP_401_UNAUTHORIZED}, status=status.HTTP_401_UNAUTHORIZED)
        
        # delete every other entries
        for a in Assess.objects.filter(toUser=validated_data.data['toUser']).filter(fromUser=validated_data.user):
            a.delete()
        
        Assess.objects.create(fromUser=user, toUser=toUser, score=score, comment=comment).save()
        
        toUser.update_mean()
        
        return Response({'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
    def myAssessOf(self, request, pk):
        toUserPk = pk
        
        fromUser = request.user
        existing = Assess.objects.filter(toUser=toUserPk).filter(fromUser=fromUser)
        
        try:
            existing = existing.get()
        except Assess.MultipleObjectsReturned: 
            #in case there is already mutliples comments => keep one
            existing = existing[len(existing)-1]    # keep the last
            
            User.objects.get(pk=toUserPk).update_mean()     # update user's mean
        except Assess.DoesNotExist:
            return Response({'status': status.HTTP_204_NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)
            
            
        serializer = AssessSerializer(existing, context={'request':request}, many=False)
        
        return JsonResponse(serializer.data, safe=False)
        
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
    @action(detail=True, methods=['get'])
    def assess(self, request, pk):
        toUser = User.objects.get(pk=pk)
        assess = Assess.objects.filter(toUser=toUser)
        
        serializer = AssessSerializer(assess, context={'request':request}, many=True)
        return JsonResponse(serializer.data, safe=False)

    @action(detail=False, methods=['get'])
    def get_asc(self, request):
        users = User.objects.all().order_by('score_mean')
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)
    
    def create(self, validated_data):   
        validated_data = validated_data.data
        User.objects.create_user(validated_data['first_name'],
                    validated_data['last_name'], 
                    validated_data['email'], 
                    validated_data['password'])
        
        
        
        return Response({'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)
        
        
    
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
        