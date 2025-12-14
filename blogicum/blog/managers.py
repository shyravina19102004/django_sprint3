from django.db import models
from django.utils import timezone

class PostManager(models.Manager):
    """Кастомный менеджер для модели Post."""

    def get_published_posts(self):
        """
        Возвращает опубликованные посты.
        Использует select_related для оптимизации запросов к БД.
        """
        return self.filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True
        ).select_related('author', 'category', 'location')