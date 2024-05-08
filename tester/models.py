from django.db import models
from django.utils import timezone


class Tester(models.Model):
    username = models.CharField('username', max_length=20, unique=True)
    password = models.CharField('password', max_length=128)


class Access(models.Model):
    tester = models.ForeignKey('Tester', on_delete=models.CASCADE, db_index=True)
    created = models.DateTimeField('created', default=timezone.now())
