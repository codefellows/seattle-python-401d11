from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note


@login_required
def note_list_view(request):
    notes = get_list_or_404(Note, user=request.user.id)
    context = {
        'notes': notes,
    }

    return render(request, 'notes/note_list.html', context)


@login_required
def note_detail_view(request, pk=None):
    note = get_object_or_404(Note, id=pk, user=request.user.id)
    context = {
        'note': note,
    }

    return render(request, 'notes/note_detail.html', context)
