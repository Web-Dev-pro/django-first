# Generated by Django 4.1.7 on 2023-04-20 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_foot'),
    ]

    operations = [
        migrations.AddField(
            model_name='foot',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
