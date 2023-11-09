# Generated by Django 3.2.3 on 2023-11-01 21:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0003_auto_20231101_2223'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created_on',), 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='product',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]