# Generated by Django 3.1.4 on 2021-02-28 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210228_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='Service_provider_name',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='store.serviceprovider'),
        ),
    ]
