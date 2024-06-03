# Generated by Django 4.2.6 on 2024-01-04 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('model_info', models.TextField(max_length=255)),
                ('model_image', models.ImageField(upload_to='media.models_images')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Моделі',
            },
        ),
    ]
