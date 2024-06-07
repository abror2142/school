from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import SubjectAPIView, TeacherAPIView, TeacherSubjectAPIView, ClassAPIView, StudentAPIView


router = routers.SimpleRouter()
router.register('subject', SubjectAPIView)
router.register('teacher', TeacherAPIView)
router.register('teacher-subject', TeacherSubjectAPIView)
router.register('class', ClassAPIView)
router.register('student', StudentAPIView)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
