from django.contrib import admin

from .models import Bucket


class BucketInlineAdmin(admin.TabularInline):
    model = Bucket
    extras = 0
    max_num = 0
    fields = ('name', 'creation_date', 'env')
    all_fields = Bucket._meta.get_all_field_names()
    all_fields.remove('env')
    readonly_fields = all_fields

    class Media:
        css = {"all": ("css/hide_admin_original.css",)}
