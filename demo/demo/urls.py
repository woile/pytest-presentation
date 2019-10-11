from django.contrib import admin
from django.urls import path
from rest_framework import routers
from customers.viewsets import CustomerViewSet
from customers.views import (
    CustomerListCreateApiView,
    CustomerRetrieveUpdateApiView,
    CustomerListOutputApiView,
)
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


router = routers.SimpleRouter()
router.register(r"customers", CustomerViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("clients/", CustomerListCreateApiView.as_view()),
    path("clients/<int:pk>/", CustomerRetrieveUpdateApiView.as_view()),
    path("clients-output/", CustomerListOutputApiView.as_view()),

    path(
        "openapi",
        get_schema_view(
            title="Customers", description="API for customers", version="0.1.0"
        ),
        name="openapi-schema",
    ),
    path(
        "docs/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
] + router.urls
