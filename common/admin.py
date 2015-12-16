from django.contrib import admin
from .models import Environment, AccessCredentials
from .forms import AccessForm
from s3.admin import BucketInlineAdmin
from s3.utils import S3Connect


@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    pass

@admin.register(AccessCredentials)
class AccessCredentialsAdmin(admin.ModelAdmin):
    form = AccessForm
    fieldsets = (
        ('Access Details', {
            'fields': (('name', 'access_key', 'secret', 'env', 'updated_date', 'created_date'),)
        }),
        # ('Details', {
        #     'fields': (('updated_date', 'created_date'),)
        # }),
    )
    readonly_fields = ('updated_date', 'created_date')
    inlines = (BucketInlineAdmin,)

    def make_published(modeladmin, request, queryset):
        for one in queryset.all():
            S3Connect(one.access_key, one.secret).update_create_bucket(one)

    make_published.short_description = "Mark selected stories as published"

    actions = (make_published,)
