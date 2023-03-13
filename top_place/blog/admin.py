from django.contrib import admin

from .models import Article, Group, Comment


class ArticleAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = (
        'pk', 'title', 'text', 'pub_date', 'author', 'group', 'image'
        )
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
    list_editable = ('group',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'text', 'created')
    search_fields = ('article',)
    list_filter = ('author',)


# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Group)
