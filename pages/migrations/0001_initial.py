# Generated by Django 4.0.4 on 2022-06-29 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('btntext', models.CharField(max_length=100)),
            ],
        ),
    ]