from django_filters import rest_framework as filters
from django.contrib.auth.models import User


class CustomerFilter(filters.FilterSet):
    email__contains = filters.CharFilter(field_name="email", lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'email__contains']
