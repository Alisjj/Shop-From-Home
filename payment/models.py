from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    transaction_ref = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=50)
    email = models.EmailField()
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.transaction_ref