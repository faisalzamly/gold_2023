# Generated by Django 4.1.7 on 2023-08-17 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableapp', '0002_table_gold_dinar_table_price_market'),
    ]

    operations = [
        migrations.CreateModel(
            name='name_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='price_numper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numper', models.FloatField(default=1)),
            ],
        ),
    ]
