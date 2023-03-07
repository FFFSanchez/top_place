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
