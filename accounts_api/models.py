# from MySQLdb.constants.ER import USERNAME
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, \
    PermissionManager, BaseUserManager


class UserProfileManager(BaseUserManager):
    """
    Manager for user profiles.
    """

    def create_user(self, email, field_name, test, password):
        """
        Create a new user profile.
        """
        if not email:
            raise ValueError("Users must have an email address")

        if not field_name:
            raise ValueError("Users must have a field_name")

        email = self.normalize_email(email)
        user = self.model(email=email)

        user.field_name = field_name
        user.test = test

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, field_name, test, password):
        """
        Create a new superuser with the given details.
        """

        user = self.create_user(
            email=email,
            field_name=field_name,
            test=test,
            password=password
        )

        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionManager):
    """
    Database model for users in the system.
    """
    id = models.AutoField(primary_key=True)
    email = models.EmailField("email", max_length=255, unique=True)
    # field_name = models.CharField(max_length=255, blank=False, null=False)
    # username = None
    # username = models.CharField(max_length=255)
    field_name = models.CharField("field_name", max_length=255, default='NAME STRING')
    test = models.CharField("test", max_length=255, default='SOME STRING')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['field_name', 'test']

    def get_full_name(self):
        """
        Retrieve full name for user
        """
        return self.field_name

    def get_short_name(self):
        """
        Retrieve short name for user
        """
        return self.field_name

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        """
        returns a string representation of user
        """
        return self.email
