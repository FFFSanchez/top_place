# Generated by Django 4.1.7 on 2023-03-10 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_group_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]