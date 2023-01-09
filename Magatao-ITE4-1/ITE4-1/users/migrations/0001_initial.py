# Generated by Django 2.2b1 on 2019-06-13 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0006_auto_20190604_0505'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('basicperson_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.BasicPerson')),
                ('bill', models.TextField(default='', max_length=1000)),
                ('installment', models.TextField(default='', max_length=1000)),
                ('status', models.TextField(default='', max_length=1000)),
            ],
            bases=('home.basicperson',),
        ),
    ]
