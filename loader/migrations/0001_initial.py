# Generated by Django 4.0.4 on 2022-05-21 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0013_rename_accrued_interest_unlistedbondholding_interest_rate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FileField(upload_to='uploads/')),
                ('file_name', models.CharField(max_length=100)),
                ('format', models.CharField(max_length=100)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('parsed', models.BooleanField(default=False)),
                ('parse_response', models.TextField(default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StockHoldingFile',
            fields=[
                ('file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='loader.file')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.demataccount')),
            ],
            bases=('loader.file',),
        ),
        migrations.CreateModel(
            name='ListedNCDHoldingFile',
            fields=[
                ('file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='loader.file')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.demataccount')),
            ],
            bases=('loader.file',),
        ),
        migrations.CreateModel(
            name='FDHoldingFile',
            fields=[
                ('file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='loader.file')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.bankaccount')),
            ],
            bases=('loader.file',),
        ),
    ]
