# Generated by Django 2.2.14 on 2020-07-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images/profile/default_profile.png', null=True, upload_to='images/profile/'),
        ),
    ]
