# Generated by Django 2.1.1 on 2018-09-18 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0004_auto_20180914_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='livestream',
            name='password',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
