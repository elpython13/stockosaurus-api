# Generated by Django 3.1.7 on 2021-04-10 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0014_remove_stockprice_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='NasdaqDaily',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('close', models.FloatField()),
                ('volume', models.IntegerField()),
                ('ticker', models.TextField()),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
