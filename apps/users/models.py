import binascii
import os

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from app_smiles.app_smiles import settings

TOKEN_LENGTH = 64


class User(AbstractUser):
    facebook_id = models.CharField(_('facebook id'), max_length=158, blank=True, null=True, unique=True)
    avatar = models.CharField(_('avatar'), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
        ordering = ['-created_at']

    def __str__(self):
        return 'Users: {}'.format(self.username)


class Token(models.Model):
    key = models.CharField(_("Key"), max_length=TOKEN_LENGTH, primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='tokens',
        on_delete=models.CASCADE, verbose_name=_('User')
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        db_table = 'token'

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()

        return super(Token, self).save(*args, **kwargs)

    @staticmethod
    def generate_key():
        num_bytes = TOKEN_LENGTH // 2
        return binascii.hexlify(os.urandom(num_bytes)).decode()

    def __str__(self):
        return 'Token (user {}): {}'.format(self.user_id, self.key)
