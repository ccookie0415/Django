# Generated by Django 3.2.18 on 2023-03-22 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20230322_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='director',
            field=models.TextField(default='Unknown', max_length=20),
        ),
    ]