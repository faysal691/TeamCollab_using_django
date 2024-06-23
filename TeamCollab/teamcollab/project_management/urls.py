# project_management/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewSet, ProjectViewSet, ProjectMemberViewSet, TaskViewSet, CommentViewSet
from rest_framework.schemas import get_schema_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'project-members', ProjectMemberViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="TeamCollab API",
        default_version='v1',
        description="API documentation for the TeamCollab project management tool",
    ),
    public=True,
)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
]

