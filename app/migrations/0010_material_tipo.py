# Generated by Django 5.1.1 on 2024-09-30 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_delete_tipomaterial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='tipo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
