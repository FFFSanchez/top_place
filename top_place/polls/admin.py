from django.contrib import admin

from .models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'title', 'pub_date')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('title',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_value', 'voices')
    search_fields = ('choice_value',)


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
