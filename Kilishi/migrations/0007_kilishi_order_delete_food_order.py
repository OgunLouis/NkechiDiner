# Generated by Django 5.1.1 on 2025-03-14 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kilishi', '0006_food_order_delete_kilishi_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='kilishi_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('phone_num', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=400)),
                ('size', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='food_order',
        ),
    ]
