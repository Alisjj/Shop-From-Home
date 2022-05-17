from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

