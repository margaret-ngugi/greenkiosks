# Generated by Django 4.2.3 on 2023-07-14 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('is_delivered', models.BooleanField(default=False)),
            ],
        ),
    ]
