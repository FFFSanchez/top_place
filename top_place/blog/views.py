from django.shortcuts import render
from .models import Group, Article
from polls.models import Poll, Choice
from django.shortcuts import get_object_or_404
from .utils import pag


def index(request):
    articles = Article.objects.all()
    # if poll_id == -1:
    poll = Poll.objects.order_by('?').first()
    # else:
    #     poll = Poll.objects.get(pk=poll_id)
    template = 'blog/index.html'
    # post_list = Post.objects.filter(author__following__user=request.user)
    choice_list = Choice.objects.filter(polls__id=poll.id)
    # print(list(choice_list))
    # print(choice_list)
    # print(type(list(choice_list)))
    # print(dir(choice_list))
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
    groups = Group.objects.all()
    template = 'blog/articles.html'
    context = {
        'page_obj': pag(request, articles),
        'groups': groups
    }
    return render(request, template, context)


def articles_on_group(request, slug):
    group = get_object_or_404(Group, slug=slug)
    articles_on_group_list = Article.objects.filter(group=group)
    groups = Group.objects.all()
    template = 'blog/articles.html'
    context = {
        'page_obj': pag(request, articles_on_group_list),
        'groups': groups
    }
    return render(request, template, context)


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    template = 'blog/article_detail.html'
    context = {
        'article': article,
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
