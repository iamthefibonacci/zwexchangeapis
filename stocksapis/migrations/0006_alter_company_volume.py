# Generated by Django 4.1.1 on 2022-09-07 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stocksapis", "0005_alter_company_closing_alter_company_opening"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="volume",
            field=models.IntegerField(default="0.00"),
        ),
    ]