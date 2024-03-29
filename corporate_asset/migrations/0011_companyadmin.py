# Generated by Django 5.0.3 on 2024-03-15 10:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate_asset', '0010_rename_employee_assetlog_lent_to'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admins', to='corporate_asset.company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company_admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
