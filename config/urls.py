"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core.establishment.views import EstablishmentViewSet, IngredientViewSet, RecipientViewSet, FinalCupViewSet, ComboViewSet, StockViewSet, CustomCupViewSet, DailyRevenueViewSet
from core.orders.views import OrderViewSet, OrderItemViewSet
from core.users.views import UserViewSet
from core.adress.views import AddressViewSet
from core.supplier.views import SupplierViewSet, ContactViewSet

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


router = DefaultRouter()
router.register(r'establishments', EstablishmentViewSet, basename='establishments')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')
router.register(r'recipients', RecipientViewSet, basename='recipients')
router.register(r'final-cups', FinalCupViewSet, basename='final-cups')
router.register(r'users', UserViewSet, basename='users')
router.register(r'combos', ComboViewSet, basename='combos')
router.register(r'stock', StockViewSet, basename='stock')
router.register(r'custom-cups', CustomCupViewSet, basename='custom-cups')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'order-items', OrderItemViewSet, basename='order-items')
router.register(r'addresses', AddressViewSet, basename='addresses')
router.register(r'suppliers', SupplierViewSet, basename='suppliers')
router.register(r'contacts', ContactViewSet, basename='contacts')
router.register(r'daily-revenues', DailyRevenueViewSet, basename='daily-revenues')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'api'), namespace='api')),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]