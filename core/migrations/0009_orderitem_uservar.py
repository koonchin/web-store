# Generated by Django 2.2.14 on 2022-03-28 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20220328_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='uservar',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
