# Generated by Django 4.1.1 on 2022-10-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_alter_conversations_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversations',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('close', 'open')], default='open', max_length=10),
        ),
    ]
