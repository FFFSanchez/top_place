from django.contrib import admin

from .models import Article, Group, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'text', 'pub_date', 'author', 'group', 'image'
        )
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
    list_editable = ('group',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'text', 'created')
    search_fields = ('article',)
    list_filter = ('author',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Group)
