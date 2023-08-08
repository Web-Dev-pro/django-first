# Generated by Django 4.1.7 on 2023-04-23 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_delete_foot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=70)),
                ('text', models.TextField(max_length=8000)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Foot',
                'verbose_name_plural': 'Foot',
            },
        ),
    ]