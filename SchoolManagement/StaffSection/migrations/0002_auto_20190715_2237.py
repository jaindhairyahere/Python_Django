# Generated by Django 2.2.1 on 2019-07-15 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StaffSection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='helper',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]