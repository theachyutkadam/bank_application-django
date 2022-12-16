# Generated by Django 4.1.3 on 2022-12-13 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('building', models.CharField(max_length=30)),
                ('flat_number', models.CharField(max_length=30)),
                ('road', models.CharField(max_length=150)),
                ('taluka', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('pin_code', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'address',
            },
        ),
    ]
