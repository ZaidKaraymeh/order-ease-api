# Generated by Django 4.2.5 on 2023-11-17 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_restaurantcategory_is_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantcategory',
            name='icon',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
