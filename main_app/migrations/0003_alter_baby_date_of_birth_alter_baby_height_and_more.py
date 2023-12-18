# Generated by Django 5.0 on 2023-12-18 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby',
            name='date_of_birth',
            field=models.DateField(verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='baby',
            name='height',
            field=models.FloatField(verbose_name='Height (cm)'),
        ),
        migrations.AlterField(
            model_name='baby',
            name='weight',
            field=models.FloatField(verbose_name='Weight (lb)'),
        ),
    ]