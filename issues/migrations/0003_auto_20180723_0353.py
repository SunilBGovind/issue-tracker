# Generated by Django 2.0.7 on 2018-07-23 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_auto_20180723_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='is_resolved',
            field=models.BooleanField(default=False),
        ),
    ]