from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class TODO(models.Model):
    Status_Choices = [
        ('C', 'Completed'),
        ('P', 'Pending'),

    ]
    priority_Choices = [

        ('1', ' 1️⃣'),
        ('2', '2️⃣'),
        ('3', '3️⃣'),
        ('4', '4️⃣'),
        ('5', '5️⃣'),
        ('6', '6️⃣'),
        ('7', '7️⃣'),
        ('8', '8️⃣'),
        ('9', '9️⃣'),
        ('10', '🔟'), ]

    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=Status_Choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2, choices=priority_Choices)
