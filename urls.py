from django.contrib import admin
from django.urls import path, include
from service_requests.views import homepage  # Import the homepage view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('requests/', include('service_requests.urls')),
     path('', homepage, name='homepage'),  # Redirect homepage to the request submission page
]

