from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'assess', views.AssessViewSet)
router.register(r'users', views.UsersViewSet)

# define the urls
urlpatterns = [
    path('', include(router.urls))
]