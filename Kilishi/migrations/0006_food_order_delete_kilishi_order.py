# Generated by Django 5.1.1 on 2025-03-11 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kilishi', '0005_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='food_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone_num', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=400)),
            ],
        ),
        migrations.DeleteModel(
            name='kilishi_order',
        ),
    ]
