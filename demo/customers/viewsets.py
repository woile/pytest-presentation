from django.contrib.auth.models import User
from rest_framework import viewsets, pagination
from .serializers import CustomerSerializer
from .filters import CustomerFilter


class CustomerViewSet(viewsets.ModelViewSet):
    """
    Contains:
     - queryset
     - filter queryset
     - serializer_class (and validations)
     - pagination (use offset)
     - create/edit implementation
    """

    # Required
    queryset = User.objects.all()
    serializer_class = CustomerSerializer

    # Optionals
    filterset_class = CustomerFilter
    pagination_class = pagination.LimitOffsetPagination

    # -> can be customized containing only business logic, no API noise
    # def perform_create(validated_data):

    # def perform_update()
