# Generated by Django 5.1.4 on 2025-02-09 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_reference',
            field=models.CharField(default='40d987628ff849e8b1acde80b447a3b8', max_length=100, unique=True),
        ),
    ]
