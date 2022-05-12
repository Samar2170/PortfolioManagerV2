# Generated by Django 4.0.4 on 2022-05-12 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('securities', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_code', models.CharField(max_length=100, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio.account')),
                ('balance', models.FloatField(default=0)),
                ('account_no', models.CharField(max_length=100, unique=True)),
                ('bank_name', models.CharField(max_length=100)),
                ('bank_code', models.CharField(max_length=100)),
            ],
            bases=('portfolio.account',),
        ),
        migrations.CreateModel(
            name='DematAccount',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio.account')),
                ('balance', models.FloatField(default=0)),
                ('account_no', models.CharField(max_length=100, unique=True)),
                ('broker', models.CharField(max_length=100)),
            ],
            bases=('portfolio.account',),
        ),
        migrations.CreateModel(
            name='GeneralAccount',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio.account')),
                ('account_no', models.CharField(max_length=100, unique=True)),
            ],
            bases=('portfolio.account',),
        ),
        migrations.CreateModel(
            name='StockSellTrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('buy_price', models.FloatField()),
                ('sell_price', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('trade_date', models.DateField()),
                ('profit', models.FloatField()),
                ('security', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='securities.stock')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.demataccount')),
            ],
        ),
        migrations.CreateModel(
            name='StockHolding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('buy_price', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('security', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='securities.stock')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.demataccount')),
            ],
        ),
        migrations.CreateModel(
            name='StockBuyTrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('price', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('trade_date', models.DateField()),
                ('security', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='securities.stock')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.demataccount')),
            ],
        ),
    ]