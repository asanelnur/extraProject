from rest_framework.routers import DefaultRouter

from accounts import views

app_name = 'accounts1'

router = DefaultRouter()
router.register(r'accounts', views.AccountViewSet)
router.register(r'wallets', views.WalletViewSet)

urlpatterns = router.urls
