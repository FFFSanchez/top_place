from django.contrib import admin

from .models import Poll, Choice, UserPolls


class PollAdmin(admin.ModelAdmin):
    save_on_top = True
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'title', 'pub_date')
    list_display_links = ('pk', 'title')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('title',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_value', 'voices')
    list_display_links = ('choice_value',)
    search_fields = ('choice_value',)


class UserPollsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'poll', 'choice')
    list_display_links = ('user',)
    search_fields = ('poll',)


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(UserPolls, UserPollsAdmin)
