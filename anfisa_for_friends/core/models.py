from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет флаг is_published."""
    is_published = models.BooleanField('Опубликовано', default=True)
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Уникальное название, не более 256 символов'
        )

    class Meta:
        abstract = True
