# Generated by Django 2.2.1 on 2019-07-13 06:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basicapp', '0003_user_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_pics')),
                ('password', models.OneToOneField(on_delete='', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
