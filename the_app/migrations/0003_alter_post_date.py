# Generated by Django 4.2.3 on 2023-07-31 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_app', '0002_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(verbose_name='date of posting'),
        ),
    ]
