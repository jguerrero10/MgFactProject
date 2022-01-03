from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from factapp.serial_utils import *
from django.contrib.auth.models import User
from factapp.models import *


class UserView(viewsets.ModelViewSet):
    """
    This class creates a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class TypeProductView(viewsets.ModelViewSet):
    queryset = TypeProduct.objects.all()
    serializer_class = TypeProductSerializer
