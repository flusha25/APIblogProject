from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .serializers import LoginSerializer, BlogSerializer,  CategorySerializer
from . models import Blog, Category
from rest_framework.authtoken.models import Token
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .filters import BlogFilter
from .permissions import CustomTokenPermission
from drf_yasg.utils import swagger_auto_schema

class LoginViewSet(viewsets.ViewSet):  # Change inheritance to viewsets.ViewSet
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    last_token = None
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']  # Use validated_data instead of validate
            token, created = Token.objects.get_or_create(user=user)
            self.last_token = token.key
            print(self.last_token)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
    

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogFilter

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    