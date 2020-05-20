# Generated by Django 3.0.6 on 2020-05-20 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='sale date')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('commission', models.DecimalField(decimal_places=2, max_digits=3)),
                ('items', models.ManyToManyField(to='sales.Product')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Staff')),
            ],
        ),
    ]