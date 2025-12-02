from django.db import models
from django.contrib.auth.models import AbstractUser

from core.establishment.models import Establishment
from django.utils.translation import gettext_lazy as _

from core.users.managers import CustomUserManager  # Assuming you have a custom user manager

# Create your models here.
class User(AbstractUser):
    username = None  # Remove the username field
    email = models.EmailField(_("e-mail address"), unique=True)
    registration = models.IntegerField(null=True, unique=True)
    name = models.CharField(max_length=255, null=True)
    establishment = models.ForeignKey(
        Establishment,
        on_delete=models.CASCADE,
        related_name="worker",
        null=True,
        blank=True
    )
    is_management = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']
    EMAIL_FIELD = "email"

    def __str__(self):
        return self.email + " - " + (self.name or "No Name")
    
    objects = CustomUserManager()  # Assuming you have a custom user manager

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]
