# Generated by Django 4.0.4 on 2022-05-27 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="courses",
            name="name",
            field=models.CharField(max_length=155, unique=True),
        ),
    ]
