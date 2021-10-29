# from MySQLdb.constants.ER import USERNAME
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, \
    PermissionManager, BaseUserManager


class UserProfileManager(BaseUserManager):
    """
    Manager for user profiles.
    """

    def create_user(self, email, name, password=None):
        """
        Create a new user profile.
        """
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """
        Create a new superuser with the given details.
        """
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_stuff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionManager):
    """
    Database model for users in the system.
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Retrieve full name fro user
        """
        return self.name

    def get_short_name(self):
        """
        Retrieve short name fro user
        """
        return self.name

    def __str__(self):
        """
        returns a string representation of user
        """
        return self.email
