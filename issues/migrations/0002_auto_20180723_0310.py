# Generated by Django 2.0.7 on 2018-07-23 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='resolved_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]