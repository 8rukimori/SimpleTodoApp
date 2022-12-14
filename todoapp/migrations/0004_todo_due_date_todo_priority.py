# Generated by Django 4.1.1 on 2022-10-02 05:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("todoapp", "0003_remove_todo_due_date_todo_memo"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="due_date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="todo",
            name="priority",
            field=models.CharField(
                choices=[("danger", "high"), ("warning", "normal"), ("primary", "low")],
                default="warning",
                max_length=50,
            ),
            preserve_default=False,
        ),
    ]
