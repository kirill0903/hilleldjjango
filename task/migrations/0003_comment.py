# Generated by Django 3.1 on 2022-06-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
