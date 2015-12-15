from django.contrib import admin
from .models import Environment, AccessCredentials


@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    pass


@admin.register(AccessCredentials)
class AccessCredentialsAdmin(admin.ModelAdmin):
    pass
