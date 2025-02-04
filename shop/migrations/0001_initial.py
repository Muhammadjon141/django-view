# Generated by Django 5.0.6 on 2024-07-21 12:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vegitables', '0002_fruit_image_vegitable_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('count', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fruit', models.ManyToManyField(null=True, to='vegitables.fruit')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vegitable', models.ManyToManyField(null=True, to='vegitables.vegitable')),
            ],
        ),
    ]
