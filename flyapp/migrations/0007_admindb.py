# Generated by Django 4.1.3 on 2023-01-04 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyapp', '0006_remove_bikedata_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='admindb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=20, null=True)),
                ('Email', models.CharField(blank=True, max_length=20, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Password', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
