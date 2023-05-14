from rest_framework.routers import DefaultRouter
from django.urls import path

from logistic.views import ProductViewSet, StockViewSet, test_change

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)


urlpatterns = router.urls, path('api/v1/test/', test_change)
