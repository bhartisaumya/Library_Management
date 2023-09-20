from django.db import models


# Create your models here.
class UserModel(models.Model):
    name = models.CharField(null=False, blank=False, max_length=200, help_text="Name of the user")
    email = models.CharField(null=False, blank=False, max_length=50, help_text="Email of the user")
    address = models.TextField(null=True, blank=True, help_text="Address of the user")

    def __str__(self):
        return self.name
