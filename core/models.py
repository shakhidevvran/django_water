from django.db import models

class Bootle(models.Model):
    address = models.CharField(max_length=255)
    volume = models.IntegerField(default=10)
    maker = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    expired = models.BooleanField(default=False)

class Order(models.Model):
    created_at= models.DateTimeField(
        verbose_name="Дата и время заказа",
        auto_now_add=True,
    )
    update_at = models.DateTimeField(
        verbose_name="Дата и время изменения заказа",
        auto_now_add=True,
    )

