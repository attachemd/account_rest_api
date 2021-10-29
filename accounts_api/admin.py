from django.contrib import admin

from accounts_api import models

admin.site.register(models.UserProfile)
