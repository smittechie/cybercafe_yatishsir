# Generated by Django 4.1.7 on 2023-03-03 05:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0002_alter_history_login_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='history',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 3, 5, 24, 11, 212216, tzinfo=datetime.timezone.utc)),
        ),
    ]