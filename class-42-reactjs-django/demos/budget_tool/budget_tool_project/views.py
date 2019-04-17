from django.shortcuts import render


def home_view(req):
    return render(req, 'generic/home.html')
