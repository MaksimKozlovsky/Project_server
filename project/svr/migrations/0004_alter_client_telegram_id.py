# Generated by Django 4.1.4 on 2023-01-23 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svr', '0003_delete_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
