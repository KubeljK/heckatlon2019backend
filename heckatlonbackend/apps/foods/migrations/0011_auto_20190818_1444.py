# Generated by Django 2.2.4 on 2019-08-18 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0010_auto_20190818_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
