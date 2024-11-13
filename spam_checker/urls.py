from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
