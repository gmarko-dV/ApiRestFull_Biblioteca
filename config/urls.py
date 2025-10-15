from django.contrib import admin
from django.urls import path,include
from biblioteca.views import welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('biblioteca.urls')),
    path('',welcome),
]
