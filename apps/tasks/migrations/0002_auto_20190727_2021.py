# Generated by Django 2.2.2 on 2019-07-28 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklists', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='checklist',
        ),
        migrations.AddField(
            model_name='task',
            name='checklist',
            field=models.ManyToManyField(to='checklists.Checklist'),
        ),
    ]
