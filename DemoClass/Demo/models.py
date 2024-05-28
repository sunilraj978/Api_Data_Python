from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
# class User(models.Model):
#     Name = models.CharField(max_length=20)
#     username = models.CharField(max_length=20)
#     email = models.CharField(max_length=30)
#     street = models.CharField(max_length=10)
#     zipcode = models.CharField(max_length=10)
#     phone = models.CharField(max_length=10)
#     website = models.CharField(max_length=10)


class Poll(models.Model):
    image = models.CharField(max_length=30)
    occupation = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    nickname = models.CharField(max_length=10)
    portrayed = models.CharField(max_length=10)

    def __str__(self):
        return self.nickname
