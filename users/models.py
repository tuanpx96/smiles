from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    facebook_id = models.CharField(_('first name'), max_length=158, blank=True, null=True, unique=True)

    class Meta:
        db_table = 'user'


