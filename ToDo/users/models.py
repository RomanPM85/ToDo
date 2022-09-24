from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class User(AbstractUser):
    user_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(_('email address'), unique=True)

