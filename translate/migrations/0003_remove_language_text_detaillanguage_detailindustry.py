# Generated by Django 4.2.4 on 2023-10-08 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0002_language_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='text',
        ),
        migrations.CreateModel(
            name='DetailLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('img', models.ImageField(blank=True, null=True, upload_to='detaillanguage_pic/')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detaillanguage', to='translate.language')),
            ],
        ),
        migrations.CreateModel(
            name='DetailIndustry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('img', models.ImageField(blank=True, null=True, upload_to='detailindustry_pic/')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detailindustry', to='translate.industry')),
            ],
        ),
    ]
