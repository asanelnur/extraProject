from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blogs import views

app_name = 'blogs1'

router = DefaultRouter()
router.register(r'blogs', views.BlogViewSet, basename='blogs')

urlpatterns = [
    path('', include(router.urls)),
    # path('<int:id>/', views.get_blog),
    # path('create/', views.create_blog),
    # path('', views.get_blogs),
    # path('v2/', views.BlogView.as_view({'get': 'list'})),
    # path('v2/<int:pk>/', views.BlogView.as_view({'get': 'retrieve'})),
    # path('<int:blog_id>/', views.index, name="blog"),
]
