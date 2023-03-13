from django.shortcuts import render, redirect
from .models import Group, Article, Comment
from .forms import CommentForm
from polls.models import Poll, Choice, UserPolls
from django.shortcuts import get_object_or_404
from .utils import pag
from django.contrib.auth.decorators import login_required


def index(request, poll_id=0):
    """Если 0 то будет рандомный опрос,
    если не 0, то будет тот же опрос,
    опрос выбирается исключая уже пройденные"""

    voices_vision = False
    if poll_id == 0:
        if request.user.is_authenticated:
            # Исключает объекты Поллов которые уже были ассоцированы с юзером
            poll = Poll.objects.exclude(
                poll_voted_by_user__user=request.user
                ).order_by('?').first()
        else:
            poll = Poll.objects.order_by('?').first()
    else:
        poll = Poll.objects.get(pk=poll_id)
        voices_vision = True
    already_voted = False
    if request.user.is_authenticated and poll:
        if UserPolls.objects.filter(
                user=request.user
                ).filter(
                poll=get_object_or_404(Poll, id=poll.id)).exists():
            already_voted = True
    template = 'blog/index.html'
    if poll:
        choice_list = Choice.objects.filter(polls__id=poll.id)
    else:
        choice_list = None

    polls = Poll.objects.all()

    context = {
        'text': 'Социальные Статистические Кружочки',
        'poll': poll,
        'polls': polls,
        'choice_list': choice_list,
        'already_voted': already_voted,
        'voices_vision': voices_vision
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
    form = CommentForm(request.POST or None)
    comments = Comment.objects.filter(article_id=article_id)
    template = 'blog/article_detail.html'
    context = {
        'article': article,
        'form': form,
        'comments': comments
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


@login_required
def add_comment(request, article_id):
    article = Article.objects.get(id=article_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.article = article
        comment.save()
    return redirect('blog:article_detail', article_id=article_id)
