
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username,  first_name, last_name, middle_name, password=None, is_active=True, is_staff=False, is_admin=False):
        if not username:
            raise ValueError("User must have an username ")
        if not password:
            raise ValueError("User must have a password")
        user = self.model(
            username=username,

            password=password,
            middle_name=middle_name,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.set_password(password)
        user.save(using=self._db)
        return user

        def create_staffuser(self, username, password=None):
            user = self.create_user(

                username=username,
                password=password,
                is_staff=True,
            )
        user.save(using=self._db)
        return user

    def create_superuser(self, username,  first_name, middle_name, last_name, password=None,):
        user = self.create_user(

            username=username,

            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True)
   # email = models.EmailField(max_length=50, unique=True, null=True)
    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['first_name', 'middle_name', 'last_name']
    objects = UserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.first_name + " " + self.middle_name

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
