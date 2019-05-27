# Generated by Django 2.2.1 on 2019-05-18 05:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("packages", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="PackageFile",
            fields=[
                (
                    "packagefile_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="packages.PackageFile",
                    ),
                ),
                ("pkg_type", models.CharField(max_length=16)),
                ("sha256", models.CharField(max_length=64, unique=True)),
                ("_metadata", models.TextField()),
            ],
            bases=("packages.packagefile",),
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "package_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="packages.Package",
                    ),
                )
            ],
            bases=("packages.package",),
        ),
    ]
