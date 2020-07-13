# Generated by Django 3.0.8 on 2020-07-13 13:09

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


def switch_to_nonabstract(apps, schema_editor):
    """
    Populate the SpatialEntry values for each entry.

    For each RasterEntry and each GeometryEntry, create a new SpatialEntry
    that contains the relevant information.
    """
    SpatialEntry = apps.get_model('geodata', 'SpatialEntry')
    RasterEntry = apps.get_model('geodata', 'RasterEntry')
    GeometryEntry = apps.get_model('geodata', 'GeometryEntry')
    for entry in RasterEntry.objects.all():
        entry.spatialentry_ptr_id = SpatialEntry.objects.create(
            modified=entry.modified,
            modifier=entry.modifier,
            creator=entry.creator,
            created=entry.created,
            name=entry.name,
            description=entry.description,
            acquisition_date=entry.acquisition_date,
            footprint=entry.footprint,
        ).id
        entry.save()
    for entry in GeometryEntry.objects.all():
        entry.spatialentry_ptr_id = SpatialEntry.objects.create(
            modified=entry.modified,
            modifier=entry.modifier,
            creator=entry.creator,
            created=entry.created,
            name=entry.name,
            description=entry.description,
            acquisition_date=entry.acquisition_date,
            footprint=entry.data.convex_hull,
        ).id
        entry.save()


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '0004_geometryentry_footprint'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpatialEntry',
            fields=[
                (
                    'modifiableentry_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='geodata.ModifiableEntry',
                    ),
                ),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('acquisition_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('footprint', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            bases=('geodata.modifiableentry',),
        ),
        migrations.AddField(
            model_name='geometryentry',
            name='spatialentry_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                # primary_key=True,
                serialize=False,
                to='geodata.SpatialEntry',
                null=True,
                blank=True,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rasterentry',
            name='spatialentry_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                # primary_key=True,
                serialize=False,
                to='geodata.SpatialEntry',
                null=True,
                blank=True,
            ),
            preserve_default=False,
        ),
        migrations.RunPython(switch_to_nonabstract),
    ]
