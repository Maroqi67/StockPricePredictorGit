# Generated by Django 5.1.2 on 2024-11-14 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0004_allregionsstockperformance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allregionsstockperformance',
            name='custom_region_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='allregionsstockperformance',
            name='region_name',
            field=models.CharField(max_length=100),
        ),
    ]
