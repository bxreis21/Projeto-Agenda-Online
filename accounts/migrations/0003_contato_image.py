# Generated by Django 4.0.3 on 2022-05-08 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_contato_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='image',
            field=models.ImageField(default=None, upload_to='upload/% Y/% m/% d/'),
            preserve_default=False,
        ),
    ]