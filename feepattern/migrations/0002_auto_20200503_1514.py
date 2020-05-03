# Generated by Django 2.2.12 on 2020-05-03 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feepattern', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feepattern',
            name='fee_pattern_academic_fee',
        ),
        migrations.RemoveField(
            model_name='feepattern',
            name='fee_pattern_tution_fee',
        ),
        migrations.AddField(
            model_name='feepattern',
            name='fee_pattern_batch',
            field=models.CharField(default='not given', max_length=50),
        ),
        migrations.AlterField(
            model_name='feepattern',
            name='fee_pattern_class_name',
            field=models.CharField(default='not given', max_length=50),
        ),
        migrations.AlterField(
            model_name='feepattern',
            name='fee_pattern_type',
            field=models.CharField(default='not given', max_length=50),
        ),
    ]
