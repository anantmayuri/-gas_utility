from django.urls import path
from .views import service_request_list, service_request_create

urlpatterns = [
    path('', service_request_list, name='service_requests_list'),
    path('new/', service_request_create, name='service_request_create'),  # New URL for form
]
