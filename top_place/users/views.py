from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.shortcuts import redirect

# Импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.

    # 'users:login'
    success_url = reverse_lazy('blog:index', args=[0])
    template_name = 'users/signup.html'

    def form_valid(self, form):
        """If the form is valid,
        save the associated model and log the user in."""

        user = form.save()
        login(self.request, user)

        return redirect(self.success_url)
