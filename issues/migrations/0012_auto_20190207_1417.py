# Generated by Django 2.0.7 on 2019-02-07 14:17

from django.db import migrations, models
import tagulous.models.fields
import tagulous.models.models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0011_savedissue_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tagulous_Issue_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AlterField(
            model_name='issue',
            name='issue_type',
            field=models.CharField(choices=[('BUG', 'bug'), ('FEATURE', 'feature')], default='BUG', max_length=9),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('TODO', 'todo'), ('DOING', 'doing'), ('DONE', 'done')], default='TODO', max_length=7),
        ),
        migrations.RemoveField(
            model_name='issue',
            name='tag',
        ),
        migrations.AlterUniqueTogether(
            name='tagulous_issue_tag',
            unique_together={('slug',)},
        ),
        migrations.AddField(
            model_name='issue',
            name='tag',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, help_text='Enter a comma-separated tag string', to='issues.Tagulous_Issue_tag'),
        ),
    ]