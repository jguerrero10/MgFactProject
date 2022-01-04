# Django Imports
from django.urls import path, include
# DRF Imports
from rest_framework.routers import DefaultRouter
# FactApp Imports
from factapp import views

# Routers
router = DefaultRouter()
router.register('user', views.UserView, basename='user')
router.register('client', views.ClientView, basename='client')
router.register('seller', views.SellerView, basename='seller')
router.register('type-product', views.TypeProductView, basename='type-products')
router.register('product', views.ProductView, basename='product')
router.register('inovice', views.InvoiceView, basename='invoice')
router.register('invoice-detail', views.InvoiceDetailView, basename='invoice-detail')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls'))
]
