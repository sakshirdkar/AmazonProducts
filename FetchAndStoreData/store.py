from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=40)


book = Books.objects.create(
    name="A Thousand Splendid Suns",
    author="Khalid Houssini"
)
