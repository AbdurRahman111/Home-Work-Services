# Generated by Django 3.1.4 on 2021-02-28 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='Customer_name',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
        ),
    ]