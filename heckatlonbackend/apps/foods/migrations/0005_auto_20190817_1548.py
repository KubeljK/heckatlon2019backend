# Generated by Django 2.2.4 on 2019-08-17 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_auto_20190817_1509'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='nutrients',
            unique_together={('name', 'ingredient')},
        ),
    ]
