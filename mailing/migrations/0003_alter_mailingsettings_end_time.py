# Generated by Django 5.0.6 on 2024-05-10 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_rename_message_mailingmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingsettings',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Конец рассылки'),
        ),
    ]