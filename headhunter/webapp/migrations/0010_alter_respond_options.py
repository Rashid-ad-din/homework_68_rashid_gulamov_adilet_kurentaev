# Generated by Django 4.1.3 on 2022-11-25 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_respondmessage_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='respond',
            options={'verbose_name': 'Отклик', 'verbose_name_plural': 'Отклики'},
        ),
    ]
