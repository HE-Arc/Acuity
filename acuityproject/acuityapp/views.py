from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse
from .serializers import AssessSerializer, UserSerializer
from .models import Assess, User

from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.response import Response 
from django.conf import settings
from .permissions import UserPermission


from django.utils.decorators import method_decorator
from rest_framework import viewsets, status

class AssessViewSet(viewsets.ModelViewSet):
    queryset = Assess.objects.all()
    serializer_class = AssessSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, validated_data):     
        user = validated_data.user
        
        try:
            to_user = User.objects.get(pk=validated_data.data['to_user'])        
            score = validated_data.data['score']  
            comment = validated_data.data['comment']
        except KeyError:
            return Response({'status': status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
        
        
         
        if user == to_user:
            return Response({'status': status.HTTP_401_UNAUTHORIZED}, status=status.HTTP_401_UNAUTHORIZED)
        
        # delete every other entries
        for a in Assess.objects.filter(to_user=validated_data.data['to_user']).filter(from_user=validated_data.user):
            a.delete()
        
        Assess.objects.create(from_user=user, to_user=to_user, score=score, comment=comment).save()
        
        to_user.update_mean()
        
        return Response({'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
    def myAssessOf(self, request, pk):
        to_user_pk = pk
        print(pk)
        
        from_user = request.user
        existing = Assess.objects.filter(to_user=to_user_pk).filter(from_user=from_user)
        print(Assess.objects.filter(from_user=request.user))
        try:
            existing = existing.get()
        except Assess.MultipleObjectsReturned: 
            #in case there is already mutliples comments => keep one
            existing = existing[len(existing)-1]    # keep the last
            
            User.objects.get(pk=to_user_pk).update_mean()     # update user's mean
        except Assess.DoesNotExist:
            return Response({'status': status.HTTP_204_NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)
            
            
        serializer = AssessSerializer(existing, context={'request':request}, many=False)
        
        return JsonResponse(serializer.data, safe=False)
        
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]
    
    @action(detail=True, methods=['get'])
    def assess(self, request, pk):
        to_user = User.objects.get(pk=pk)
        assess = Assess.objects.filter(to_user=to_user)
        
        serializer = AssessSerializer(assess, context={'request':request}, many=True)
        return JsonResponse(serializer.data, safe=False)

    @action(detail=False, methods=['get'])
    def myuser(self, request):
        user = request.user
        serializer = UserSerializer(user)
        
        return JsonResponse(serializer.data, safe=False)
        
    @action(detail=False, methods=['get'])
    def best_users(self, request):
        users = User.objects.all().order_by('-score_mean')[:10]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def worst_users(self, request):
        
        users = User.objects.all().order_by('score_mean')[:10]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def create(self, validated_data):   
        validated_data = validated_data.data
        User.objects.create_user(validated_data['first_name'],
                    validated_data['last_name'], 
                    validated_data['email'], 
                    validated_data['password'])
        
        
        
        return Response({'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)
        
        