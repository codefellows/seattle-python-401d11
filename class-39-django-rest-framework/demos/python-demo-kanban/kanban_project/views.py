from django.shortcuts import render


def home_view(request):
    context = {
        'message': 'Hello world.'
    }
    return render(request, 'generic/home.html', context)
