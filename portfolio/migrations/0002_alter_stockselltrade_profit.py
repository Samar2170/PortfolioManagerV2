# Generated by Django 4.0.4 on 2022-05-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockselltrade',
            name='profit',
            field=models.FloatField(null=True),
        ),
    ]