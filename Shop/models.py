from django.db import models
from django.contrib.auth.models import User

class DoorModel(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField(max_length=255)
    image = models.ImageField(upload_to='model_images')
    price = models.CharField(max_length=20)

    def __str__(self):
        return f'Модель {self.name}'

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Моделі'

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментрі'

    def __str__(self):
        return f'Коментар {self.author}'