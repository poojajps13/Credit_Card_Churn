# Generated by Django 3.1.7 on 2021-03-03 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0004_auto_20210303_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='naive_bayes_1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='naive_bayes_2',
            field=models.FloatField(null=True),
        ),
    ]
