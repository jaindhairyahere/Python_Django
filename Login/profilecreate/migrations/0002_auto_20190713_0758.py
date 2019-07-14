# Generated by Django 2.2.1 on 2019-07-13 07:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profilecreate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumni',
            name='email',
        ),
        migrations.RemoveField(
            model_name='alumni',
            name='name',
        ),
        migrations.AddField(
            model_name='alumni',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_pic'),
        ),
        migrations.AddField(
            model_name='alumni',
            name='user_model',
            field=models.OneToOneField(default='', on_delete='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumni',
            name='phone_no',
            field=models.CharField(blank=True, default='9999999999', max_length=11),
        ),
    ]
