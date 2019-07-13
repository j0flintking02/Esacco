from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class EsaccoAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'status')


admin.site.register(User, EsaccoAdmin)
admin.site.register(Profile)
