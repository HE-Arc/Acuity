# Generated by Django 3.2.11 on 2022-03-23 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acuityapp', '0004_user_score_mean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='score_mean',
            field=models.FloatField(default=3.0),
        ),
    ]