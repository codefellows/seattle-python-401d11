from django.shortcuts import render


def home_view(request):
    return render(request, 'generic/home.html', {'message': 'Hello World'})
