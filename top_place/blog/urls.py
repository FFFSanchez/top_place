from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('articles/', views.articles, name='articles'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('project/', views.project, name='project'),
    path('contact_email/', views.contact_email, name='contact_email')
]
