# Generated by Django 4.0.5 on 2022-06-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_indexpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indexpage',
            name='welcom_description',
        ),
        migrations.AddField(
            model_name='indexpage',
            name='welcome_description',
            field=models.TextField(default='No_dsc'),
            preserve_default=False,
        ),
    ]
