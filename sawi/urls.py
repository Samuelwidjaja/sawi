from django.urls import path
from django.contrib import admin
from django.urls import path, include

app_name = 'main'

urlpatterns = [
    path('admins/', admin.site.urls),
    path('main/', include('main.urls')),
]