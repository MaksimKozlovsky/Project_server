# Generated by Django 4.1.4 on 2023-01-12 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svr', '0008_remove_position_qty_position_qty_p'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='qty_p',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=2, null=True),
        ),
    ]