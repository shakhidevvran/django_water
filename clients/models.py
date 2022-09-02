from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    active = models.BooleanField(default=True, verbose_name='является активным покупателем')
    bottle_ordered = models.IntegerField(default=1)
    photo = models.ImageField(verbose_name='Фото',
                              upload_to='photos',
                              null=True,
                              blank=True
                              )

class Order(models.Model):
    created_at = models.DateTimeField(verbose_name='дата и время создания заказа',
                                      auto_now_add=True)
    update_at = models.DateTimeField(
        verbose_name='дата и время изменения заказа',
        auto_now=True
    )
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.name} - {self.contacts}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
