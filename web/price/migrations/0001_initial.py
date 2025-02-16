# Generated by Django 4.2.18 on 2025-02-14 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.CharField(blank=True, max_length=255, null=True)),
                ('origin_price', models.CharField(blank=True, max_length=255, null=True)),
                ('discount_price', models.CharField(blank=True, max_length=255, null=True)),
                ('collect_ts', models.DateTimeField()),
            ],
            options={
                'db_table': 'price_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('url_link', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'url',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('createts', models.DateTimeField()),
                ('user_pw', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserUrl',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='price.user')),
            ],
            options={
                'db_table': 'user_url',
                'managed': False,
            },
        ),
    ]
