# Generated by Django 3.0.6 on 2020-05-20 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('position', models.CharField(choices=[('JR', 'Junior'), ('SR', 'Senior'), ('MA', 'Manager')], default='JR', max_length=2)),
                ('commission', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
            ],
        ),
    ]
