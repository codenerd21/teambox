# Generated by Django 2.2.3 on 2019-09-23 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_strength'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='strengths',
            field=models.ManyToManyField(to='main_app.Strength'),
        ),
    ]