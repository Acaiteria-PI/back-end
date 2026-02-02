from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.number}, {self.city}, {self.state}, {self.zip_code}"