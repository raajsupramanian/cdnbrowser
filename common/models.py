"""Models for common modules"""
import django
from django.db import models

now = django.utils.timezone.now()


class Environment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    default = models.BooleanField(default=False)

    class Meta:
        db_table = "environment"

    def get_default(self):
        return Environment.objects.filter(default=True)[0]

    def __unicode__(self):
        return self.name


class AccessCredentials(models.Model):
    name = models.CharField(max_length=100)
    access_key = models.CharField(max_length=200)
    secret = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=None, blank=True)
    updated_date = models.DateTimeField(default=None, blank=True)
    env = models.ForeignKey(Environment, default=None, blank=True, null=True, verbose_name="Environment")

    class Meta:
        db_table = "access_details"
        verbose_name_plural = "Access Details"

    def save(self, *args, **kw):
        self.updated_date = now
        if self.pk is None:
            self.created_date = now
        super(AccessCredentials, self).save(*args, **kw)

    def __unicode__(self):
        return self.name

    def get_env(self):
        return self.env
