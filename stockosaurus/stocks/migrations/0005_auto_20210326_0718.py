# Generated by Django 3.1.7 on 2021-03-26 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_auto_20210326_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockprice',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
