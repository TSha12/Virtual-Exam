# Generated by Django 5.1.5 on 2025-03-02 13:03

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='status',
        ),
        migrations.AddField(
            model_name='result',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='result',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='result',
            name='score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='result',
            name='student',
            field=models.ForeignKey(limit_choices_to={'is_staff': False}, on_delete=django.db.models.deletion.CASCADE, related_name='student_results', to=settings.AUTH_USER_MODEL),
        ),
    ]
