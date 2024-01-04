from django.db import models

# Create your models here.
class Faq(models.Model):
    question = models.TextField(blank=False)
    answer = models.TextField(blank=False)
    helpful = models.CharField(max_length=1, default="N") # N=not specified, T=true, F=false

    def __str__(self) -> str:
        return self.question
    
class TestConnection(models.Model):
    name=models.CharField(max_length=10)
    image = models.ImageField(blank=False)

    def __str__(self) -> str:
        return self.name