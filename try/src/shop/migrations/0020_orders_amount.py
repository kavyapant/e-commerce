# Generated by Django 3.0.6 on 2020-05-31 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20200522_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
