from django.db import models


class Tester(models.Model):
    username = models.CharField('username', max_length=20, unique=True)
    password = models.CharField('password', max_length=128)
