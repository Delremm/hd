# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table('hd_app_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(null=True, max_length=1000, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(null=True, max_length=1000, blank=True)),
            ('al_url', self.gf('django.db.models.fields.CharField')(null=True, max_length=1000, blank=True)),
        ))
        db.send_create_signal('hd_app', ['Tag'])

        # Adding model 'Startup'
        db.create_table('hd_app_startup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(null=True, max_length=1000, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(null=True, max_length=1000, blank=True)),
            ('al_url', self.gf('django.db.models.fields.CharField')(null=True, max_length=1000, blank=True)),
            ('hidden', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('follower_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('product_desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('quality', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('twitter_url', self.gf('django.db.models.fields.CharField')(null=True, max_length=1000, blank=True)),
            ('company_url', self.gf('django.db.models.fields.CharField')(null=True, max_length=1000, blank=True)),
            ('created_at', self.gf('django.db.models.fields.CharField')(null=True, max_length=255, blank=True)),
            ('fundraising', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('hd_app', ['Startup'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table('hd_app_tag')

        # Deleting model 'Startup'
        db.delete_table('hd_app_startup')


    models = {
        'hd_app.startup': {
            'Meta': {'object_name': 'Startup'},
            'al_url': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1000', 'blank': 'True'}),
            'company_url': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1000', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'follower_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fundraising': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1000', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1000', 'blank': 'True'}),
            'product_desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quality': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'row_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'twitter_url': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1000', 'blank': 'True'})
        },
        'hd_app.tag': {
            'Meta': {'object_name': 'Tag'},
            'al_url': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1000', 'blank': 'True'}),
            'row_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1000', 'blank': 'True'})
        }
    }

    complete_apps = ['hd_app']