# Generated by Django 4.0.4 on 2022-05-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_stockselltrade_profit'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockbuytrade',
            name='trade_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AddField(
            model_name='stockselltrade',
            name='trade_id',
            field=models.UUIDField(null=True),
        ),
    ]
