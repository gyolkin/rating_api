from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .core import CategoryGenreModel, ReviewCommentModel
from .validators import year_validator


class Category(CategoryGenreModel):
    pass


class Genre(CategoryGenreModel):
    pass


class Title(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название',
        help_text='Укажите название'
    )
    year = models.PositiveSmallIntegerField(
        validators=(year_validator,),
        verbose_name='Год',
        help_text='Укажите год'
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Категория',
        help_text='Выберите категорию'
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='Жанр',
        help_text='Выберите жанр'
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание',
        help_text='Добавьте описание'
    )

    def __str__(self):
        return self.name


class Review(ReviewCommentModel):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
        help_text='Выберите произведение'
    )
    score = models.PositiveSmallIntegerField(
        validators=(
            MaxValueValidator(10),
            MinValueValidator(1)
        ),
        verbose_name='Оценка',
        help_text='Укажите оценку'
    )

    class Meta(ReviewCommentModel.Meta):
        default_related_name = 'reviews'
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_author_title'
            )
        ]


class Comment(ReviewCommentModel):
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,)

    class Meta(ReviewCommentModel.Meta):
        default_related_name = 'comments'
