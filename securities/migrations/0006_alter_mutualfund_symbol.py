# Generated by Django 4.0.4 on 2022-05-23 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securities', '0005_remove_bullion_name_bullion_symbol_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mutualfund',
            name='symbol',
            field=models.CharField(max_length=100, null=True),
        ),
    ]