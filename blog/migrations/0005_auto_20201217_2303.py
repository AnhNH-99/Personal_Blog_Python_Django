# Generated by Django 3.1.3 on 2020-12-17 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replys', to='blog.comment'),
        ),
    ]