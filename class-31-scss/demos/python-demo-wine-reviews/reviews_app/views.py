from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Review


def review_list_view(request):
    reviews = get_list_or_404(Review)

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/review_list.html', context)


def review_detail_view(request, pk):
    context = {
        'review': get_object_or_404(Review, pk=pk),
    }

    return render(request, 'reviews/review_detail.html', context)
