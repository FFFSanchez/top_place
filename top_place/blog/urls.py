from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('<int:poll_id>/', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('articles/', views.articles, name='articles'),
    path(
        'articles_on_group/<slug:slug>/',
        views.articles_on_group,
        name='articles_on_group'
    ),
    path(
        'articles/<int:article_id>/',
        views.article_detail,
        name='article_detail'
    ),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('project/', views.project, name='project'),
    path(
        'articles/<int:article_id>/comment/',
        views.add_comment,
        name='add_comment'
    ),
]
