from django.urls import path, include
from rest_framework.routers import DefaultRouter
from factapp import views

router = DefaultRouter()
router.register('user', views.UserView, basename='user')
router.register('client', views.ClientView, basename='client')
router.register('type-product', views.TypeProductView, basename='type-products')
urlpatterns = [
    path('', include(router.urls))
]
