# Generated by Django 3.2.9 on 2021-11-30 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0007_alter_userdetails_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='Mobile',
            field=models.IntegerField(max_length=12),
        ),
    ]
