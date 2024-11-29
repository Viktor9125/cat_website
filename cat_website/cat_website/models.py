from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    pass

class Cat(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


# class CustomCake(models.Model):
#     # image = models.ImageField(upload_to='images/')
#     image = models.ImageField('Изображение', upload_to='images/',
#                               blank=True, null=True, default='images/default.jpg')
#     name = models.CharField(_('Название'), max_length=100)
#     # weight = models.FloatField()
#     # calories = models.IntegerField()
#     price = models.DecimalField(_('Цена'), max_digits=8, decimal_places=2)
#     quantity_in_stock = models.IntegerField(_('Количество на складе'))
#
#     def __str__(self):
#         return f'{self.name} - {self.price} рублей'
#
#     class Meta:
#         verbose_name = _('Торт')
#         verbose_name_plural = _('Торты')

# class ShoppingCartItem(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
#     item = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
#     quantity = models.PositiveIntegerField(default=1)


# class ShoppingCart(models.Model):
#     pass
