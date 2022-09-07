# Generated by Django 4.1.1 on 2022-09-07 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stocksapis", "0003_alter_company_trading_day"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="closing",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="company",
            name="opening",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]