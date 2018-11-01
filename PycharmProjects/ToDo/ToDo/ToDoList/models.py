from django.db import models


from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import UserManager

# Create your models here.
class Company(models.Model):
    name = models.CharField(verbose_name="company name", unique=True, max_length=64)
    def __str__(self):
       return self.name

#Создание модели списков
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.ForeignKey(Company, null = False)

    def __str__(self):
        return self.title


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    company = models.ManyToManyField(Company)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
