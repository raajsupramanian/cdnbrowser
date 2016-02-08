from django.db import models

from common.models import AccessCredentials, Environment


class Bucket(models.Model):
    access = models.ForeignKey(AccessCredentials)
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=None)
    env = models.ForeignKey(Environment, verbose_name="Environment", null=True, blank=True, default=None)

    def save(self, *args, **kw):
        print "test" + str(self.env)
        if self.env is None:
            print "hi"
            self.env = self.access.get_env()
        super(Bucket, self).save(*args, **kw)

    class Meta:
        db_table = "bucket"

    def __unicode__(self):
        return self.name
