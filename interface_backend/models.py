from django.db import models

# Create your models here.
class Faq(models.Model):
    question = models.TextField(blank=False)
    answer = models.TextField(blank=False)
    helpful = models.BooleanField(blank=True)

    def __str__(self) -> str:
        return self.question