from django.shortcuts import render


def index(request):
    template = 'blog/index.html'
    context = {
        'text': 'Кружочки'
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
    template = 'blog/articles.html'
    context = {
        'text': 'Кружочки'
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
