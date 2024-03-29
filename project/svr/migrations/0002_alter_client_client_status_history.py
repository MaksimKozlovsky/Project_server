# Generated by Django 4.1.4 on 2023-01-23 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('svr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_status',
            field=models.CharField(blank=True, choices=[('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum')], default='Silver', max_length=8, null=True),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='svr.order')),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='svr.client', verbose_name='Клиент')),
            ],
        ),
    ]
