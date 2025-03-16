from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    slug = models.SlugField('Слаг', max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(
        'Порядок отображения', default=100
        )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Topping(PublishedModel):
    slug = models.SlugField('Слаг', max_length=64, unique=True)

    class Meta:
        verbose_name = 'топпинг'
        verbose_name_plural = 'Топпинги'

    def __str__(self):
        return self.title


class Wrapper(PublishedModel):

    class Meta:
        verbose_name = 'обёртка'
        verbose_name_plural = 'Обёртки'

    def __str__(self):
        return self.title


class IceCream(PublishedModel):
    description = models.TextField('Описание')
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name='Обёртка'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    toppings = models.ManyToManyField(Topping, verbose_name='Топпинг')
    is_on_main = models.BooleanField('На главную', default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    output_order = models.PositiveSmallIntegerField(
        'Порядок отображения', default=100
        )

    class Meta:
        verbose_name = 'мороженое'
        verbose_name_plural = 'Мороженое'
        ordering = ('output_order', 'title')

    def __str__(self):
        return self.title
