from django.shortcuts import render
from .models import Group, Article
from django.core.mail import send_mail


def index(request):
    articles = Article.objects.all()
    template = 'blog/index.html'
    context = {
        'text': 'Кружочки',
        'articles': articles
    }
    return render(request, template, context)


def contact(request):
    template = 'blog/contact.html'
    context = {
        'text': 'Кружочки'
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


def contact_email(form):
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']

    body = f"{name} {message}"
    send_mail(
        subject, body, email, ["lordsanchez@yandex.ru", ],
    )
