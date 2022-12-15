# Generated by Django 4.1.4 on 2022-12-15 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100, verbose_name='Клиент')),
                ('client_status', models.CharField(blank=True, choices=[('S', 'Silver'), ('G', 'Gold'), ('P', 'Platinum')], max_length=1, null=True)),
                ('telegram_id', models.PositiveIntegerField(blank=True, null=True)),
                ('telegram_payload', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=250, verbose_name='Коментарий к заказу')),
                ('order_created', models.DateTimeField(auto_now_add=True)),
                ('order_receipt', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery', models.CharField(max_length=100, verbose_name='Способ доставки')),
            ],
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(verbose_name='Колличество')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наимерование')),
                ('category', models.CharField(choices=[('C', 'Coffee'), ('D', 'Desert')], max_length=1, verbose_name='Категория')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to='svr.client', verbose_name='Клиент')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='svr.comment')),
                ('delivery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='svr.delivery')),
                ('positions', models.ManyToManyField(through='svr.Extra', to='svr.position')),
            ],
        ),
        migrations.AddField(
            model_name='extra',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='svr.order', verbose_name='Заказ'),
        ),
        migrations.AddField(
            model_name='extra',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='svr.position', verbose_name='Каталог'),
        ),
    ]
