from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

from accounts_api import models

admin.site.register(models.UserProfile)


# class AccountAdmin(UserAdmin):
#     list_display = ("email", "name", "is_staff")
#     # fields = ("first_name", "plan", "email")
#     ordering = ('email',)
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()
#
#
# admin.site.register(models.UserProfile, AccountAdmin)
