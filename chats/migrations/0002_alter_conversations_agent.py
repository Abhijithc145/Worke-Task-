# Generated by Django 4.1.1 on 2022-10-17 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversations',
            name='agent',
            field=models.CharField(max_length=100),
        ),
    ]
