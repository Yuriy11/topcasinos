# Generated by Django 2.1.5 on 2019-01-10 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0004_casino_casino_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casino',
            name='currencies',
            field=models.CharField(default='SOMESTRING', max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='deposit_methods',
            field=models.CharField(default='SOMESTRING', max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='established_on',
            field=models.CharField(default='SOMESTRING', max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='jurisdiction',
            field=models.CharField(default='SOMESTRING', max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='languages',
            field=models.CharField(default='SOMESTRING', max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='minimal_deposit',
            field=models.CharField(default='SOMESTRING', max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='os_supported',
            field=models.CharField(default='SOMESTRING', max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='sister_casinos',
            field=models.CharField(default='SOMESTRING', max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='software',
            field=models.CharField(default='SOMESTRING', max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='withdrawal_limits',
            field=models.CharField(default='SOMESTRING', max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='withdrawal_methods',
            field=models.CharField(default='SOMESTRING', max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='withdrawal_min_amount',
            field=models.CharField(default='SOMESTRING', max_length=400),
        ),
    ]