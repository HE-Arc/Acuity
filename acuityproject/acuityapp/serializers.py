from rest_framework import routers,serializers,viewsets
from .models import Task, Assess, User
from djoser.serializers import UserSerializer

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'score_mean', 'first_name', 'last_name']
        
class AssessSerializer(serializers.HyperlinkedModelSerializer):
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)
    class Meta:
        model = Assess
        fields = ['url', 'score', 'from_user', 'to_user', 'comment']
