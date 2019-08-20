# Generated by Django 2.2.2 on 2019-08-11 07:29

import apps.documents.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0007_auto_20190811_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediafile',
            name='file',
            field=models.FileField(max_length=255, upload_to='file', validators=[apps.documents.models.validate_file_extension]),
        ),
    ]