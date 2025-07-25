from django.db import models

class Contribution(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount} TZS"
