# Generated by Django 4.0.4 on 2022-06-24 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_alter_tag_options_board_rules_board_unique board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='post',
            name='url_title',
            field=models.TextField(max_length=200),
        ),
    ]
