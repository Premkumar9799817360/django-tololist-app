# Generated by Django 4.0.3 on 2022-04-07 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0002_remove_storage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
