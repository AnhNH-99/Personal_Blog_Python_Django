# Generated by Django 3.1.3 on 2020-12-19 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20201219_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
