from django.shortcuts import render, redirect
from .models import Choice, Poll, UserPolls
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def vote(request, choice_id, poll_id):
    choice = get_object_or_404(Choice, id=choice_id)
    choice.voices += 1
    choice.save()

    UserPolls.objects.create(
        user=request.user,
        poll=get_object_or_404(Poll, id=poll_id),
        choice=choice
    )
    # print(poll_id)
    return redirect('blog:index', poll_id)
