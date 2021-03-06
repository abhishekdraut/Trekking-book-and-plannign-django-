# Generated by Django 3.2.7 on 2021-09-05 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('pincode', models.IntegerField(max_length=6)),
                ('image', models.ImageField(upload_to='uploaded_content')),
                ('mobile', models.IntegerField(max_length=10)),
            ],
        ),
    ]
