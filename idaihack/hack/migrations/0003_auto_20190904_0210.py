# Generated by Django 2.2 on 2019-09-04 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0002_auto_20190904_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='satelite_images',
            field=models.CharField(max_length=500),
        ),
    ]