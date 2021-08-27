from django.db import models

# Create your models here.
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models

class userManager(BaseUserManager):
    
    def create_user(self, username, email, password=None):
        print("create user")