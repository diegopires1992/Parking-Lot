# Generated by Django 3.2.2 on 2021-05-12 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliable_motorcycle_spaces', models.IntegerField()),
                ('avaliable_car_spaces', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('fill_priority', models.IntegerField()),
                ('avaliable_spaces', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='levels.avaliable')),
            ],
        ),
    ]
