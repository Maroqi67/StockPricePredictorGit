# Generated by Django 5.1.2 on 2024-11-01 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0006_alter_asset_country_alter_asset_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='market_cap_coverage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
