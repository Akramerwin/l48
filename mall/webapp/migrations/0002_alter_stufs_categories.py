# Generated by Django 4.1.2 on 2022-11-13 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stufs',
            name='categories',
            field=models.TextField(blank=True, choices=[('other', 'разное'), ('electronics', 'электроника'), ('clothes', 'одежда'), ('for_home', 'Для дома'), ('sports', 'спорт')], default='other', verbose_name='categories'),
        ),
    ]
