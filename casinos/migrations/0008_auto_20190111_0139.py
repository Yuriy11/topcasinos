# Generated by Django 2.1.5 on 2019-01-10 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0007_auto_20190111_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casino',
            name='casino_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='casino',
            name='languages',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='os_supported',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='casino',
            name='software',
            field=models.CharField(max_length=400),
        ),
    ]
