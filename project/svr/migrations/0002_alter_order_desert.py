# Generated by Django 4.1.4 on 2022-12-14 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('svr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='desert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='desert', to='svr.catalog'),
        ),
    ]
