# Generated by Django 4.0.4 on 2022-08-23 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='name',
        ),
        migrations.RemoveField(
            model_name='review',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.movie'),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
