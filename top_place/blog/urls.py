from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('articles/', views.articles, name='articles'),
    path(
        'articles_on_group/<slug:slug>/',
        views.articles_on_group,
        name='articles_on_group'
    ),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('project/', views.project, name='project'),
]
