from django.urls import path
from . import views

urlpatterns = [
    path('daftar-kartu/', views.daftar_kartu, name='daftar_kartu'),
    # Tambahkan path lainnya sesuai kebutuhan
]
