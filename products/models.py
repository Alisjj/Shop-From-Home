import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()



class Item(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)
    item_images = models.ImageField(upload_to='product_images/', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_details', args=[str(self.id)])

class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="reviews")
    review = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.review
