# Generated by Django 4.2.4 on 2023-10-08 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0004_detailindustry_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='flags/'),
        ),
    ]