# Generated by Django 3.2.7 on 2021-10-05 09:37

from django.db import migrations, models
import motivo.validators


class Migration(migrations.Migration):

    dependencies = [
        ('motivo', '0004_alter_challenge_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='image',
        ),
        migrations.AlterField(
            model_name='challenge',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/challenge_files/', validators=[motivo.validators.validate_file_size]),
        ),
    ]