# Generated by Django 5.0.3 on 2024-03-16 07:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate_asset', '0011_companyadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetlog',
            name='asset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asset_log', to='corporate_asset.asset'),
        ),
    ]
