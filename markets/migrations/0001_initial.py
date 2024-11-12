# Generated by Django 5.1.2 on 2024-11-10 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
                ('country_second_name', models.CharField(blank=True, max_length=100, null=True)),
                ('country_code', models.CharField(max_length=3)),
                ('region', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=3)),
                ('capital_city', models.CharField(max_length=100)),
                ('most_recent_GDP_USD', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('GDP_USD_2023', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('GDP_USD_2022', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('population_size_2023', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DailyPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True)),
                ('asset_class', models.CharField(max_length=50)),
                ('ticker', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('open', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True)),
                ('high', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True)),
                ('low', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True)),
                ('adj_close', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True)),
                ('volume', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bond_Tickers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_class', models.CharField(max_length=50)),
                ('ticker', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(max_length=100)),
                ('name_from_source', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('custom_region', models.CharField(blank=True, max_length=50, null=True)),
                ('economic_power_region', models.CharField(blank=True, max_length=50, null=True)),
                ('issuer_type', models.CharField(blank=True, max_length=50, null=True)),
                ('maturity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('credit_quality', models.CharField(blank=True, max_length=50, null=True)),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'unique_together': {('asset_class', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Commodity_Tickers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_class', models.CharField(max_length=50)),
                ('commodity_category', models.CharField(max_length=50)),
                ('commodity_subtype', models.CharField(blank=True, max_length=50, null=True)),
                ('ticker', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(max_length=100)),
                ('name_from_source', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'unique_together': {('asset_class', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Cryptocurrency_Tickers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_class', models.CharField(max_length=50)),
                ('ticker', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(max_length=100)),
                ('name_from_source', models.CharField(blank=True, max_length=100, null=True)),
                ('token_category', models.CharField(blank=True, max_length=50, null=True)),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'unique_together': {('asset_class', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Equity_Tickers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_class', models.CharField(max_length=50)),
                ('ticker', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(max_length=100)),
                ('name_from_source', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_region', models.CharField(blank=True, max_length=100, null=True)),
                ('custom_region', models.CharField(blank=True, max_length=50, null=True)),
                ('constituents_count', models.PositiveIntegerField(blank=True, null=True)),
                ('market_cap', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'unique_together': {('asset_class', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Forex_Tickers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_class', models.CharField(max_length=50)),
                ('ticker', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(max_length=100)),
                ('name_from_source', models.CharField(blank=True, max_length=100, null=True)),
                ('domestic_country_or_region', models.CharField(blank=True, max_length=100, null=True)),
                ('foreign_country_or_region', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'unique_together': {('asset_class', 'name')},
            },
        ),
    ]