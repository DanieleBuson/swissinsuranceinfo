# Generated by Django 5.0 on 2024-01-01 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface_backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='helpful',
            field=models.CharField(default='N', max_length=1),
        ),
    ]