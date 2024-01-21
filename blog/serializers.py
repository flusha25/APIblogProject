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
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {'data': data}        
class CategorySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'text_color', 'background_color']

class BlogSerializer(serializers.ModelSerializer):
    categories = CategorySerializer2(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'description', 'image', 'publish_date', 'categories', 'author')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        blog_data = {
            "id": data['id'],
            "title": data['title'],
            "description": data['description'],
            "image": data['image'],
            "publish_date": data['publish_date'],
            "categories": data['categories'],
            "author": data['author']
        }
        return {'data': [blog_data]}

    def update_categories_representation(self, data):
        categories_data = data.get('categories', [])
        updated_categories = []
        for category_data in categories_data:
            category = {
                "id": category_data['id'],
                "name": category_data['title'],
                "text_color": category_data['text_color'],
                "background_color": category_data['background_color']
            }
            updated_categories.append(category)
        data['categories'] = updated_categories
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        updated_data = self.update_categories_representation(data)
        return {'data': [updated_data]}
