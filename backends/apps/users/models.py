import uuid

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(email=email,
                          is_staff=is_staff,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def get_by_natural_key(self, email_):
        return self.get(email=email_)

    def create_user(self, email, password=None):
        return self._create_user(email, password, False, False, is_active=False)

    def create_superuser(self, email, password):
        return self._create_user(email, password, True, True, is_active=True)


# Django expects your custom user model to meet some minimum requirements. usernamefiled 정의해야함.
# 이메일 인증을 하려면 abstractbaseuser여야함.
# permission mixin은 permission 관련 method를 자동으로 추가해줌.
class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    email = models.EmailField(blank=True, unique=True)
    nickName = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    joined_date = models.DateField(auto_now_add=True)
