from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Profile)
admin.site.register(models.MemberFamily)
admin.site.register(models.Contribution)
admin.site.register(models.Notification)
admin.site.register(models.Address)
