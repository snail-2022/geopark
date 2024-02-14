# Generated by Django 5.0.1 on 2024-02-08 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_delete_worldgeopark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worldgeopark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_description_path', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'worldgeopark',
                'managed': False,
            },
        ),
    ]