# Generated by Django 3.1.7 on 2021-03-04 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0005_auto_20210303_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='amt_chg',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='attrition_flag',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='avg_open_to_buy',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='avg_utilization_ratio',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='card_category',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='contacts_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='credit_limit',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ct_change',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='dependent_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='education_level',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='income_category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='marital_status',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='months_inactive',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='months_on_book',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='relation_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='revolving_bal',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='trans_amt',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='trans_ct',
            field=models.FloatField(null=True),
        ),
    ]
