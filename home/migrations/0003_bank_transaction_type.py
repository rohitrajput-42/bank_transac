# Generated by Django 4.2 on 2025-04-04 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_bank_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='transaction_type',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
