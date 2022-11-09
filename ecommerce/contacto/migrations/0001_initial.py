# Generated by Django 4.1.1 on 2022-11-08 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('respondido', models.BooleanField(default=False)),
            ],
        ),
    ]
