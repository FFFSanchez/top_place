from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = form.send()
            if mail:  # send_mail возвращает кол-во отправок 0 или другое число
                messages.success(request, 'Письмо отправлено')
                return redirect('contact')
            else:
                messages.error(request, 'Ошибка отправки - fail_silently=True')
        else:
            messages.error(request, 'Ошибка валидации')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
