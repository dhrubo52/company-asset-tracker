# Generated by Django 5.0.3 on 2024-03-15 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate_asset', '0005_remove_employee_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='condition_lent',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='condition_returned',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='return_by',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='returned_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
