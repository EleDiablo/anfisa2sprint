from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title: models.CharField = models.CharField(max_length=256,
                                               verbose_name='Название')
    slug: models.SlugField = models.SlugField(max_length=64,
                                              unique=True,
                                              verbose_name='Слаг')
    output_order: models.PositiveSmallIntegerField = (
        models.PositiveSmallIntegerField(default=100,
                                         verbose_name='Порядок отображения'))

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Topping(PublishedModel):
    title: models.CharField = models.CharField(max_length=256,
                                               verbose_name='Название')
    slug: models.SlugField = models.SlugField(max_length=64,
                                              unique=True,
                                              verbose_name='Слаг')

    class Meta:
        verbose_name = 'Топинг'
        verbose_name_plural = 'Топинги'

    def __str__(self):
        return self.title


class Wrapper(PublishedModel):
    title: models.CharField = models.CharField(max_length=256,
                                               verbose_name='Название',
                                               help_text='Уникальное название'
                                               'обёртки, не более 256 символов'
                                               )

    class Meta:
        verbose_name = 'Обертка'
        verbose_name_plural = 'Обертки'

    def __str__(self):
        return self.title


class IceCream(PublishedModel):
    title: models.CharField = models.CharField(max_length=256,
                                               verbose_name='Название')
    description: models.TextField = models.TextField(verbose_name='Описание')
    wrapper: models.OneToOneField = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name='Обертка'
    )
    category: models.ForeignKey = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    toppings: models.ManyToManyField = models.ManyToManyField(
                                        Topping, verbose_name='Топинги')
    output_order: models.PositiveSmallIntegerField = (
        models.PositiveSmallIntegerField(default=100,
                                         verbose_name='Порядок отображения'))
    price: models.DecimalField = models.DecimalField(max_digits=10,
                                                     decimal_places=2)
    is_on_main: models.BooleanField = models.BooleanField(
                                        default=False,
                                        verbose_name='На главную')

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженое'
        ordering = ('output_order', 'title')

    def __str__(self):
        return self.title
