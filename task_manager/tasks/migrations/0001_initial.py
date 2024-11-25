# Generated by Django 5.1.3 on 2024-11-20 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa: E501
                ('name', models.CharField(max_length=120, unique=True, verbose_name='имя')),  # noqa: E501
                ('description', models.TextField(blank=True, verbose_name='Description')),  # noqa: E501
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskLabels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa: E501
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='labels.labels')),  # noqa: E501
            ],
        ),
    ]
