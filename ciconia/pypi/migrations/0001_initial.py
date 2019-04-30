# Generated by Django 2.2 on 2019-04-29 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PythonPackage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=64)),
                (
                    "version",
                    models.CharField(max_length=16, verbose_name="Latest version"),
                ),
                ("updated", models.DateTimeField(verbose_name="Last updated")),
                (
                    "info",
                    models.TextField(null=True, verbose_name="Package information"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PackageFile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("filename", models.CharField(max_length=64)),
                ("fileobj", models.FileField(upload_to="pypi")),
                ("pkg_type", models.CharField(max_length=16)),
                (
                    "package",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pypi.PythonPackage",
                    ),
                ),
            ],
        ),
    ]