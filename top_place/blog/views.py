from django.shortcuts import render
from .models import Group, Article
from polls.models import Poll, Choice


def index(request):
    articles = Article.objects.all()
    # if poll_id == -1:
    poll = Poll.objects.order_by('?').first()
    # else:
    #     poll = Poll.objects.get(pk=poll_id)
    template = 'blog/index.html'
    # post_list = Post.objects.filter(author__following__user=request.user)
    choice_list = Choice.objects.filter(polls__id=poll.id)
    print(list(choice_list))
    print(choice_list)
    print(type(list(choice_list)))
    print(dir(choice_list))
    context = {
        'text': 'Социальные Статистические Кружочки',
        'articles': articles,
        'poll': poll,
        'choice_list': choice_list
    }
    return render(request, template, context)


def services(request):
    template = 'blog/services.html'
    context = {
        'text': 'Кружочки'
    }
    return render(request, template, context)


def articles(request):
    articles = Article.objects.all()
    template = 'blog/articles.html'
    context = {
        'articles': articles
    }
    return render(request, template, context)


def portfolio(request):
    template = 'blog/portfolio.html'
    context = {
        'text': 'Кружочки'
    }
    return render(request, template, context)


def project(request):
    template = 'blog/project.html'
    context = {
        'text': 'Кружочки'
    }
    return render(request, template, context)
