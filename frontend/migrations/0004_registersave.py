# Generated by Django 4.1.3 on 2023-01-12 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_emailsubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registersave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=20, null=True)),
                ('Email', models.CharField(blank=True, max_length=20, null=True)),
                ('Password', models.CharField(blank=True, max_length=20, null=True)),
                ('Password1', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
