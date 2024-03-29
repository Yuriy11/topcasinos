# Generated by Django 2.1.5 on 2019-01-10 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0008_auto_20190111_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casino',
            name='casino_link',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='casino',
            name='currencies',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='deposit_methods',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='established_on',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='jurisdiction',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='minimal_deposit',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='rating_ours',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='casino',
            name='rating_users',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='casino',
            name='sister_casinos',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='withdrawal_limits',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='withdrawal_methods',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='withdrawal_min_amount',
            field=models.CharField(max_length=400),
        ),
    ]
