# Generated by Django 4.0.3 on 2022-05-08 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_contato_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
