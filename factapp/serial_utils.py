# Django Imports
from django.contrib.auth.models import User
# DRF Imports
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# FactApp Imports
from factapp.models import *


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)
    first_name = serializers.CharField(
        required=True
    )
    last_name = serializers.CharField(
        required=True
    )

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        seller = Seller.objects.create(**validated_data)
        Token.objects.create(user=seller.user)
        return seller

    class Meta:
        model = Seller
        fields = '__all__'


class TypeProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        max_length=20
    )
    description = serializers.CharField(
        max_length=150,
        required=False
    )

    class Meta:
        model = TypeProduct
        fields = ('name', 'description')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'code', 'unit_price', 'type_product', 'quantity')


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('seller', 'client')


class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ('invoice', 'product', 'quantity')
