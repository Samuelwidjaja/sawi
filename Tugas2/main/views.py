from django.shortcuts import render
from .models import Kartu

def daftar_kartu(request):
    kartus = Kartu.objects.all()
    return render(request, 'nama_aplikasi/daftar_kartu.html', {'kartus': kartus})
