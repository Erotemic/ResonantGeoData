# Generated by Django 3.1.1 on 2020-09-29 17:33
import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '0002_fmventry_fmvfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fmventry',
            old_name='ground_frame',
            new_name='ground_frames',
        ),
        migrations.AddField(
            model_name='fmventry',
            name='frame_numbers',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fmventry',
            name='frame_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fmventry',
            name='ground_union',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(
                blank=True, null=True, srid=4326
            ),
        ),
    ]
