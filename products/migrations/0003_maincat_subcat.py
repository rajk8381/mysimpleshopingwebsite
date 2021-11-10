# Generated by Django 3.1.3 on 2021-11-06 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211105_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('maincat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.maincat')),
            ],
        ),
    ]
