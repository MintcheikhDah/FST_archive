# Generated by Django 5.0.1 on 2024-03-18 13:18

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudient', '0004_remove_delegue_date_joined_remove_delegue_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateur',
            name='nom',
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='etudiant', to='etudient.utilisateur'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]