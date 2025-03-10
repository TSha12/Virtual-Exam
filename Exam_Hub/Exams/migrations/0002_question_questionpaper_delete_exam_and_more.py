# Generated by Django 5.1.5 on 2025-03-01 12:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('option_1', models.CharField(max_length=255)),
                ('option_2', models.CharField(max_length=255)),
                ('option_3', models.CharField(blank=True, max_length=255, null=True)),
                ('option_4', models.CharField(blank=True, max_length=255, null=True)),
                ('correct_option', models.CharField(help_text="Specify correct option (e.g., 'option_1')", max_length=255)),
                ('time_limit', models.IntegerField(help_text='Time limit in seconds per question')),
                ('marks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=100)),
                ('total_marks', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
        migrations.AddField(
            model_name='question',
            name='question_paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='Exams.questionpaper'),
        ),
    ]
