# Generated by Django 2.2 on 2020-09-12 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='slug',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
