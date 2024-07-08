from django.contrib import admin
from users.models import UserBalance
# Register your models here.

@admin.register(UserBalance)
class UserbalanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']