# Generated by Django 2.2 on 2019-09-04 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0003_auto_20190904_0210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='satelite_images',
            new_name='satellite_images',
        ),
    ]
