# Generated by Django 3.0.6 on 2021-05-01 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20210501_2140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('-added_at',)},
        ),
    ]
