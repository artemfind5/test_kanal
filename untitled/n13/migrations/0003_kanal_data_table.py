# Generated by Django 3.2.6 on 2022-09-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('n13', '0002_acts'),
    ]

    operations = [
        migrations.CreateModel(
            name='kanal_data_table',
            fields=[
                ('order_numb', models.IntegerField(primary_key=True, serialize=False)),
                ('price_d', models.IntegerField()),
                ('term', models.DateField()),
                ('price_r', models.IntegerField()),
            ],
        ),
    ]
