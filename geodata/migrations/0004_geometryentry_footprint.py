# Generated by Django 3.0.8 on 2020-07-10 19:09

import django.contrib.gis.db.models.fields
from django.contrib.gis.geos import Polygon
from django.db import migrations


def fill_footprint(apps, schema_editor):
    geom_entry = apps.get_model('geodata', 'geometryentry')

    for row in geom_entry.objects.all():
        row.footprint = row.data.convex_hull
        row.save(update_fields=['footprint'])


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '0003_geometryarchive_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='geometryentry',
            name='footprint',
            field=django.contrib.gis.db.models.fields.PolygonField(
                default=Polygon([[0, 0]] * 4), srid=4326
            ),
            preserve_default=False,
        ),
        migrations.RunPython(fill_footprint, lambda *args, **kwargs: None),
    ]
