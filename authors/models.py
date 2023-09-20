from django.db import models

from users.models import UserModel


class Author(UserModel):
    description = models.CharField(max_length=450)

    def __str__(self):
        return self.name
