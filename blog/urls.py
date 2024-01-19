from django.urls import path, include
from .views import LoginViewSet, BlogViewSet, CategoryViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .auth import UsernameOnlyAuthentication
# Schema view for Swagger documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    #authentication_classes=[UsernameOnlyAuthentication],
)

urlpatterns = [  
    path('blogs/', BlogViewSet.as_view({'get': 'list', 'post': 'create'}), name='blog-list'),
    path('blogs/<int:id>', BlogViewSet.as_view({'get':'list'}), name = 'blog-list'),
    path('categories/', CategoryViewSet.as_view({'get':'list'}), name = "blog-list"),
    path('login/', LoginViewSet.as_view({ 'post': 'login'}), name='blog-list'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

