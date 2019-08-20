# Generated by Django 2.2.2 on 2019-08-04 15:37

import apps.documents.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20190804_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediafile',
            name='file',
            field=models.FileField(max_length=255, upload_to='goal', validators=[apps.documents.models.validate_file_extension]),
        ),
    ]