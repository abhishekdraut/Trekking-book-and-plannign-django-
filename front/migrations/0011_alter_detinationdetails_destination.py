# Generated by Django 3.2.9 on 2021-12-02 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0010_detinationdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detinationdetails',
            name='Destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_detail', to='front.destinations'),
        ),
    ]