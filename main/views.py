# views.py in the 'main' app
from django.shortcuts import render
def show_main(request):
    context = {
        'name': 'James Samuel Widjaja',
        'class': "PBP A",
        'title': "Sawi Trading Card"
    }

    return render(request, "main.html", context)
