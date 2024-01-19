from django_filters import rest_framework as filters
from .models import Blog
import django_filters


class BlogFilter(django_filters.FilterSet):
    categories = django_filters.CharFilter(
        field_name='category__title',
        lookup_expr='icontains',  
        label='category Name'
    )
    def filter_category_name(self, queryset, name, value):
        categories = value.split(',')
        return queryset.filter(categories__title__in=categories)
 
    class Meta:
        model = Blog
        fields = ['categories']