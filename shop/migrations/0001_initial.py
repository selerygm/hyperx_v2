# Generated by Django 4.1.7 on 2023-03-24 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('discsecond', models.TextField(blank=True)),
                ('discthirs', models.TextField(blank=True)),
                ('price', models.IntegerField(blank=True)),
                ('availability', models.BooleanField()),
                ('group', models.CharField(choices=[('keyboards', 'keyboards'), ('microphones', 'microphones'), ('headphones', 'headphones'), ('mouse', 'mouse'), ('monitors', 'monitors')], default='headphones', max_length=20)),
                ('img', models.ImageField(default='no_image.webp', upload_to='img')),
            ],
        ),
    ]
