# Generated by Django 5.0.6 on 2024-06-14 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0005_mailingmessage_owner_mailingsettings_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailingsettings',
            options={'permissions': [('change_mailingsettings_setting_status', 'Can change mailingsettings setting_status')], 'verbose_name': 'Настройка рассылки', 'verbose_name_plural': 'Настройки рассылки'},
        ),
    ]
