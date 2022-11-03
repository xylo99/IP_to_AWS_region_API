from django.urls import path
from .views import (
    IP_to_AWS_region_APIView,
)

urlpatterns = [
    path('api', IP_to_AWS_region_APIView.as_view()),
]