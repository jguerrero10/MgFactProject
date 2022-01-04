# Django imports
from django.shortcuts import get_object_or_404
# DRF Imports
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework import permissions
# FactApp Imports
from factapp.serial_utils import *
from factapp.models import *


class UserView(viewsets.ModelViewSet):
    """
    This class is a View user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientView(viewsets.ModelViewSet):
    """
    This Class is a View Client
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


class SellerView(viewsets.ModelViewSet):
    """
        This Class is a View Seller
    """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['GET'], name='token-Seller')
    def token_seller(self, request, pk=None):
        seller = get_object_or_404(self.queryset, pk=pk)
        token = Token.objects.get(user=seller.user)
        return Response({
            'Seller': seller.user.username,
            'Token': token.key
        })


class TypeProductView(viewsets.ModelViewSet):
    """
        This Class is a View Type Product
    """
    queryset = TypeProduct.objects.all()
    serializer_class = TypeProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductView(viewsets.ModelViewSet):
    """
        This Class is a View Product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class InvoiceView(viewsets.ModelViewSet):
    """
        This Class is a View Invoice
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class InvoiceDetailView(viewsets.ModelViewSet):
    """
        This Class is a View Invoice Detail
    """
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['GET'], name='calculate invoice')
    def calc_amount(self, request, pk=None):
        invoice_detail = get_object_or_404(self.queryset, pk=pk)
        invoice_detail.total_amount = invoice_detail.product.unit_price * invoice_detail.quantity
        invoice_detail.save()
        serializers = InvoiceDetailSerializer(invoice_detail)
        return Response(serializers.data)

