from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class EmployerManager(BaseUserManager):
    def create_user(self, email_employer, password=None, **extra_fields):
        if not email_employer:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email_employer)
        user = self.model(email_employer=email, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user


class Employer(AbstractBaseUser):
    company_name = models.CharField(max_length=255)
    email_employer = models.EmailField(max_length=200)
    password = models.CharField(max_length=255)

    objects = EmployerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['company_name']

    def get_my_model_name(self):
        return self._meta.model_name
    def __str__(self):
        return self.company_name