from django.db import models
from django.contrib.auth.models import AbstractUser


class Company(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'company'

    def __str__(self) -> str:
        return self.name


class Users(AbstractUser):
    
    company = models.ForeignKey(Company, on_delete = models.CASCADE, null=True, default=None)

    class Meta:
        db_table = 'users'
