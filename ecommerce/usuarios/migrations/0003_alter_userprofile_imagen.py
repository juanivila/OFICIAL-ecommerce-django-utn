# Generated by Django 4.1.1 on 2022-12-02 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0002_userprofile_delete_datosusuario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="imagen",
            field=models.ImageField(
                blank=True, null=True, upload_to="producto/%Y/%m/%d"
            ),
        ),
    ]
