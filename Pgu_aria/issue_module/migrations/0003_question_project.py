# Generated by Django 5.1.3 on 2024-11-28 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_module', '0002_answer_message_parent'),
        ('workspace_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='workspace_module.project'),
            preserve_default=False,
        ),
    ]
