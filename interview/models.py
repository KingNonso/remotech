from django.db import models

# Create your models here.
class Order(models.Model):
    side = models.CharField(max_length=50)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.side


