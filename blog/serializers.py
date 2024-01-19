from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from .models import Blog, Category
from rest_framework.authtoken.models import Token
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    #password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed({"message": "The selected email is invalid.",
                            "errors": { "email": ["The selected email is invalid."]}})
        data['user'] = user
        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'text_color', 'background_color']

class BlogSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'image', 'publish_date', 'categories', 'author']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {'data': [data]}