# Generated by Django 3.1.6 on 2021-06-12 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createquiz',
            name='title',
            field=models.SlugField(),
        ),
    ]