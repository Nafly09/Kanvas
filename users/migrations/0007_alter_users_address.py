# Generated by Django 4.0.4 on 2022-05-27 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_users_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='users.address'),
        ),
    ]