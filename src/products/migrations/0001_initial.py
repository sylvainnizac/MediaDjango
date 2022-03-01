# Generated by Django 2.2 on 2022-03-01 11:18

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
                ('name', models.CharField(max_length=128)),
                ('price', models.FloatField(default=0.0)),
                ('stockpile', models.IntegerField(default=0)),
                ('can_be_sold', models.BooleanField(default=True)),
            ],
        ),
    ]
