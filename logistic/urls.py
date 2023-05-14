from rest_framework.routers import DefaultRouter

from logistic.views import ProductViewSet, StockViewSet, test_change

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)
router.register('test', test_change)


urlpatterns = router.urls
