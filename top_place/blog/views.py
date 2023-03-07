from django.shortcuts import render


def index(request):
    template = 'blog/index.html'
    return render(request, template)
