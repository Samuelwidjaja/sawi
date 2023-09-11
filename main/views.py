from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Pak Bepe',
        'type': "Monster Cards",
    }

    return render(request, "main.html", context)