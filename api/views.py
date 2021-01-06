from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import TaskSerializer
from .models import Task
from .utils import authenticate, CsrfExemptSessionAuthentication


class TaskViewSet(viewsets.ModelViewSet):
    """Class create API for ToDoApp
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (CsrfExemptSessionAuthentication, )

    def list(self, request, **kwargs) -> Response:
        """Method for get all task list

        Args:
            request: Request data

        Returns:
            Response

        """
        employees = request.user.user
        queryset = Task.objects.filter(organization=employees.login)
        serializer = TaskSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs) -> Response:
        """Method for get task on id

        Args:
            request: Request data
            pk: id task
            **kwargs:

        Returns:
            Response

        """
        employees = request.user.user
        queryset = Task.objects.filter(organization=employees.login)
        task = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(task)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs) -> Response:
        """Method for delete task id

        Args:
            request: Request data
            *args:
            **kwargs:

        Returns:
            Response

        """
        employees = request.user.user
        login = employees.login
        instance = self.get_object()

        if instance.organization != login:
            return Http404
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def signin(request):
    """"""
    email = request.data.get('email')
    organization = request.data.get('organization')
    password = request.data.get('password')

    user = authenticate(email=email, organization=organization, password=password)

    if user is not None:
        login(request, user)
        return Response(status=200)
    else:
        return Response(status=401)


@api_view(['GET'])
def signout(request):
    logout(request)
    return Response(status=200)
