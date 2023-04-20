from rest_framework.routers import DefaultRouter

from lessons import views

app_name = 'lessons'


router = DefaultRouter()
router.register(r'subjects', views.SubjectViewSet)
router.register(r'lecturers', views.LecturerViewSet)
router.register(r'students', views.StudentViewSet)

urlpatterns = router.urls
