# Generated by Django 2.0.1 on 2018-01-25 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caiso', '0004_auto_20180125_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='generation',
            name='generation_mix',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='caiso.GenerationMix'),
            preserve_default=False,
        ),
    ]
