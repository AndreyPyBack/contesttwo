# Generated by Django 4.1.7 on 2023-04-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_task_prepod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
