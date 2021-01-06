from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from rest_framework import routers

from . import views
from .views import signin, signout

router = routers.DefaultRouter()
router.register('todolist', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signin/', csrf_exempt(signin), name='signin'),
    path('signout/', signout, name='signout'),
]