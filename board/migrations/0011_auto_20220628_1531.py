# Generated by Django 3.2.13 on 2022-06-28 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_alter_tag_show_in_header_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
    ]
