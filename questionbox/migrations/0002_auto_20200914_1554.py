# Generated by Django 3.1.1 on 2020-09-14 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionbox', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
        migrations.AlterField(
            model_name='answer',
            name='body',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='questionbox.question'),
        ),
    ]
