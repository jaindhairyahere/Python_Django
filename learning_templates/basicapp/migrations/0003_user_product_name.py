# Generated by Django 2.2.1 on 2019-07-12 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0002_user_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='product_name',
            field=models.CharField(default='', max_length=264),
            preserve_default=False,
        ),
    ]
