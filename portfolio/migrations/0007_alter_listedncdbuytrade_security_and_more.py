# Generated by Django 4.0.4 on 2022-05-16 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('securities', '0004_delete_fd'),
        ('portfolio', '0006_alter_listedncdbuytrade_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listedncdbuytrade',
            name='security',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='securities.listedncd'),
        ),
        migrations.AlterField(
            model_name='listedncdselltrade',
            name='security',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='securities.listedncd'),
        ),
    ]
