# Generated by Django 4.2.3 on 2023-07-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(verbose_name='date'),
        ),
    ]
