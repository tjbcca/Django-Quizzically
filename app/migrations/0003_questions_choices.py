# Generated by Django 5.1.2 on 2024-11-12 21:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_remove_questions_wrong1_remove_questions_wrong2_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="questions",
            name="choices",
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]