from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class UserAccountManager(BaseUserManager):
   def create_user(self, email, name, password=None):
      if not email:
         raise ValueError('users must have an email address')

      email = self.normalize_email(email)
      email = email.lower()   


      user = self.model(
         email=email,
         name=name
      )

      user.set_password(password)
      user.save(using=self._db)

      return user

   def create_admin(self, email, name, password=None):
      user = self.create_user(self, email, name, password)

    

      user.is_admin = True
      user.save(using=self._db)

      return user
   
   def create_superuser(self, email, name, password):
      user = self.create_user(self, email, name, password)

      user.is_superuser = True
      user.is_staff = True

      user.save(using=self._db)

      return user


      

class UserAccount(AbstractBaseUser, PermissionsMixin):
   email = models.EmailField(max_length=255, unique=True)
   name = models.CharField(max_length=255)
   is_active = models.BooleanField(default=True)
   is_Staff = models.BooleanField(default=False)

   is_admin = models.BooleanField(default=False)

   objects = UserAccountManager()

   USERNAME_FIELD = 'email'

   def __str__(self):
      return self.email
