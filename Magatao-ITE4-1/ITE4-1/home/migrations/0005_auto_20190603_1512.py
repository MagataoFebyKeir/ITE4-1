# Generated by Django 2.2.1 on 2019-06-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190603_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicperson',
            name='NIC_No',
            field=models.IntegerField(default=0, max_length=13),
        ),
    ]
