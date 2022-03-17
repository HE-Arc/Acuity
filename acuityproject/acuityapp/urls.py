from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'assess', views.AssessViewSet)

# define the urls
urlpatterns = [
    path('tasks/', views.tasks),
    path('tasks/<int:pk>/', views.task_detail),
    # path('assess/', views.AssessCreateView.as_view())
    path('', include(router.urls))
]