# Generated by Django 2.2.4 on 2019-08-18 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0008_auto_20190818_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.CharField(default='by taste', max_length=255),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(default='g', max_length=255),
        ),
    ]
