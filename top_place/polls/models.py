from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Poll(models.Model):
    title = models.TextField(
        'Название опроса',
        help_text='Введите название опроса'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    choices = models.ManyToManyField(
        'Choice',
        blank=False,
        related_name='polls'
    )

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        ordering = ('-pub_date',)  # критерии сортировки

    def __str__(self):
        # выводим текст поста
        return self.title[:15]


class Choice(models.Model):
    # poll = models.ForeignKey(
    #     Poll,
    #     on_delete=models.CASCADE,
    #     related_name='choices',
    #     verbose_name='Опрос'
    # )
    choice_value = models.TextField(
        'Вариант ответа',
        help_text='Введите вариант ответа'
    )
    voices = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.choice_value


class UserPolls(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Юзер',
        related_name='voted_user',
        on_delete=models.CASCADE)
    poll = models.ForeignKey(
        Poll,
        verbose_name='Опрос',
        related_name='poll_voted_by_user',
        on_delete=models.CASCADE
    )
    choice = models.ForeignKey(
        Choice,
        null=True,
        verbose_name='Выбор',
        related_name='poll_choice_by_user',
        on_delete=models.SET_NULL
    )
