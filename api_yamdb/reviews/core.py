from django.db import models

from users.models import User


class CategoryGenreModel(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название',
        help_text='Укажите название'
    )
    slug = models.SlugField(
        unique=True,
        max_length=50,
        verbose_name='Короткое имя',
        help_text='Укажите короткое имя'
    )

    class Meta:
        abstract = True
        ordering = ('name',)

    def __str__(self):
        return self.name


class ReviewCommentModel(models.Model):
    text = models.TextField(
        verbose_name='Отзыв',
        help_text='Напишите отзыв'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата',
        help_text='Укажите дату'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        help_text='Выберите автора'
    )

    class Meta:
        abstract = True
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:20]
