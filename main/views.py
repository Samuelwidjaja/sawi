# views.py in the 'main' app
from django.shortcuts import render
from .models import Item

def show_main(request):
    context = {
        'name': 'Pak Bepe',
        'type': "Monster Cards",
        'description': "Monster Cards represent monsters that players battle against each other or directly against either player during the Battle Phase. Monsters are the main focus of Yu-Gi-Oh!.",
        'items': Item.objects.all()  # Retrieve all items from the Item model
    }

    return render(request, "main.html", context)
