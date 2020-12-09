# Generated by Django 3.1.2 on 2020-12-09 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convertedimagefile',
            name='checksum',
        ),
        migrations.RemoveField(
            model_name='convertedimagefile',
            name='file',
        ),
        migrations.RemoveField(
            model_name='convertedimagefile',
            name='last_validation',
        ),
        migrations.RemoveField(
            model_name='convertedimagefile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='convertedimagefile',
            name='validate_checksum',
        ),
        migrations.AddField(
            model_name='convertedimagefile',
            name='converted_file',
            field=models.OneToOneField(
                null=True, on_delete=django.db.models.deletion.CASCADE, to='geodata.arbitraryfile'
            ),
        ),
    ]