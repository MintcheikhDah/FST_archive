# Generated by Django 5.0.1 on 2024-03-18 12:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudient', '0002_delegue_date_joined_delegue_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegue',
            name='etudiant',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='delegue', to='etudient.etudiant'),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='etudiant', to='etudient.utilisateur'),
        ),
    ]