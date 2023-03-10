from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=100, blank=False, null=False)
    country = models.CharField(max_length=100, default='kenya')
    city = models.CharField(max_length=100, default='nairobi')
    amount = models.IntegerField(default=1)
    phone_number = models.IntegerField(default=1)


def __str__(self):
    return self.name
