# Generated by Django 4.1.1 on 2022-10-16 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_rename_bot_channel_bot_rename_bot_conversations_bot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chats.organization'),
            preserve_default=False,
        ),
    ]
