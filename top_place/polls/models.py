from django.db import models


class Poll(models.Model):
    title = models.TextField(
        'Название опроса',
        help_text='Введите название опроса'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    choices = models.ManyToManyField('Choice', blank=False, related_name='polls')

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
