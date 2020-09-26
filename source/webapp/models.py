from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

CATEGORY_CHOICES = [
    ('others', 'прочее'),
    ('toys', 'Игрушки'),
    ('spare_parts', 'запчасти'),
    ('food', 'Продукты')
]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='others', verbose_name='Категория')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(null=True, blank=True, upload_to='uploads', verbose_name='Картинка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return "{}. {}".format(self.name, self.image)

    class Meta:
        verbose_name = 'Название'
        verbose_name_plural = 'Список'


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1,
                               related_name='articles', verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', related_name='reviews', on_delete=models.CASCADE, verbose_name='Товар')
    text = models.TextField(max_length=3000, verbose_name='Текст отзыва')
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return "{}. {}".format(self.text[:20], self.rating)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


