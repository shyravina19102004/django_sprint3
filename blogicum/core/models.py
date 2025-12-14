from django.db import models


class PublishedModel(models.Model):
    """
    Абстрактная модель. Добавляет флаг is_published.

    Attributes:
        is_published (BooleanField): Флаг публикации
        created_at (DateTimeField): Дата и время создания
    """

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        abstract = True