from rest_framework import routers,serializers,viewsets
from .models import Task, Assess, User
from djoser.serializers import UserSerializer

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at']
        
class AssessSerializer(serializers.HyperlinkedModelSerializer):
    fromUser = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())
    toUser = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())
    class Meta:
        model = Assess
        fields = ['url', 'score', 'fromUser', 'toUser']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['score_mean', 'first_name', 'last_name']