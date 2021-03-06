# Generated by Django 2.2.2 on 2019-06-16 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("packages", "0002_auto_20190522_1547")]

    operations = [
        migrations.AddField(
            model_name="package",
            name="downloads",
            field=models.IntegerField(default=0, verbose_name="Downloads count"),
        ),
        migrations.AddField(
            model_name="package",
            name="public",
            field=models.BooleanField(
                default=True, verbose_name="Package visible to all"
            ),
        ),
    ]
