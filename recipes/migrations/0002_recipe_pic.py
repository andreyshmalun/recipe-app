# Generated by Django 4.1.7 on 2023-02-22 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(default='no_image.jpg', upload_to='recipes'),
        ),
    ]