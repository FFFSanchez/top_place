from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('choice/vote/<int:choice_id>/<int:poll_id>/', views.vote, name='vote'),
]
