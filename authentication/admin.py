from django.contrib import admin
from news.admin import myems_admin_site
# Register your models here.
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'auth_provider', 'created_at']


myems_admin_site.register(User, UserAdmin)
