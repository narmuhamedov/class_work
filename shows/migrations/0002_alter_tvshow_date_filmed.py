# Generated by Django 4.0.1 on 2022-01-14 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='date_filmed',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
