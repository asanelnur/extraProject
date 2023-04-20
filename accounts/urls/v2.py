from rest_framework.routers import DefaultRouter

from accounts import views

app_name = 'accounts2'

router = DefaultRouter()
router.register(r'accounts', views.AccountViewSetV2)
router.register(r'wallets', views.WalletViewSet)

urlpatterns = router.urls
