# Generated by Django 2.1.5 on 2019-01-10 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0006_auto_20190111_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casino',
            name='casino_description',
            field=models.CharField(max_length=2000),
        ),
    ]