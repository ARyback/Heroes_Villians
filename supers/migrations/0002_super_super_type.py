# Generated by Django 4.0.3 on 2022-03-26 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0001_initial'),
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='super',
            name='super_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='super_types.supertype'),
        ),
    ]
