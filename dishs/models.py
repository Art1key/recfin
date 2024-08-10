from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class AdminPermission(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
