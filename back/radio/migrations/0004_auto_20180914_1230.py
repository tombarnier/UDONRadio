# Generated by Django 2.1.1 on 2018-09-14 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0003_livestream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livestream',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
