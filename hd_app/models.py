from django.db import models

# Create your models here.

class Tag(models.Model):
    row_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True)
    title = models.CharField(max_length=1000, null=True, blank=True)
    al_url = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title


class Startup(models.Model):
    row_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    location = models.CharField(max_length=1000, blank=True, null=True)
    al_url = models.CharField(max_length=1000, null=True, blank=True)
    hidden = models.BooleanField(default=False)
    follower_count = models.IntegerField(null=True, blank=True)
    product_desc = models.TextField(null=True, blank=True)
    quality = models.IntegerField(blank=True, null=True)
    twitter_url = models.CharField(max_length=1000, null=True, blank=True)
    company_url = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.CharField(max_length=255, null=True, blank=True)
    fundraising = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        if self.name:
            return '%s' % self.name
        else:
            return str(self.id)

from django.contrib import admin
admin.site.register(Tag)
admin.site.register(Startup)
