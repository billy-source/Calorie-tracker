from django.db import models
from django.utils import timezone

# Create your models here.

class FoodItem(models.Model):
    name = models.CharField(max_length=20)
    calories = models.IntegerField()
    entry_date = models.DateTimeField(default=timezone.now)

    def _str_ (self):
        return f"{self.name} has {self.calories}"
