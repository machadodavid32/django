# Generated by Django 4.2.7 on 2023-11-08 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invista', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='investimento',
            name='nivel',
            field=models.IntegerField(default=1),
        ),
    ]
