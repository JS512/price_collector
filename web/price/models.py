# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class PriceData(models.Model):
    discount = models.CharField(max_length=255, blank=True, null=True)
    origin_price = models.CharField(max_length=255, blank=True, null=True)
    discount_price = models.CharField(max_length=255, blank=True, null=True)
    collect_ts = models.DateTimeField()
    url = models.ForeignKey('Url', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'price_data'


class Url(models.Model):
    id = models.IntegerField(primary_key=True)
    url_link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'url'


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=255)
    createts = models.DateTimeField()
    user_pw = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'user'


class UserUrl(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, url_id) found, that is not supported. The first column is selected.
    url = models.ForeignKey(Url, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_url'
        unique_together = (('user', 'url'),)
