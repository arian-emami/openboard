# Generated by Django 4.0.5 on 2022-06-13 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcome_title', models.CharField(max_length=50)),
                ('welcom_description', models.TimeField()),
                ('default_index', models.BooleanField()),
            ],
        ),
    ]
