from django.shortcuts import render, redirect
from .models import Poll, Choice
from django.shortcuts import get_object_or_404


def vote(request, choice_id, poll_id):
    choice = get_object_or_404(Choice, id=choice_id)
    choice.voices += 1
    choice.save()
    # print(poll_id)
    return redirect('blog:index')
