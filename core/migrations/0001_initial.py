# Generated by Django 4.1 on 2022-08-16 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bootle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('volume', models.IntegerField(default=10)),
                ('maker', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('expired', models.BooleanField(default=False)),
            ],
        ),
    ]
