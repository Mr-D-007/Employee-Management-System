from django.db import models

# Create your models here.


class Position(models.Model):
    code = models.CharField(max_length=5)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.code


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
