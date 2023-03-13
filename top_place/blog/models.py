from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Article(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,)
    text = models.TextField(
        'Текст статьи',
        help_text='Введите текст статьи'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='articles',
        verbose_name='Группа',
        help_text='Группа, к которой будет относиться статья'
    )
    # Поле для картинки (необязательное)
    # image = models.ImageField(
    #     'Картинка',
    #     upload_to='posts/',
    #     blank=True,
    #     null=True,
    # )
    # Аргумент upload_to указывает директорию,
    # в которую будут загружаться пользовательские файлы.

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-pub_date',)  # критерии сортировки

    def __str__(self):
        # выводим текст поста
        return self.text[:25]


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Статья'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    text = models.TextField(
        'Текст комментария',
        help_text='Введите комментарий'
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-created',)

    def __str__(self):
        return self.text[:10]
