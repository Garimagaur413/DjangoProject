# Generated by Django 2.2.2 on 2019-06-26 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]