# Generated by Django 3.2.9 on 2021-12-02 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0009_alter_userdetails_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetinationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('Route', models.TextField()),
                ('Best_period', models.TextField()),
                ('Destination', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='destination_detail', to='front.destinations')),
            ],
        ),
    ]