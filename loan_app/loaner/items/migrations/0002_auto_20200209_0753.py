# Generated by Django 3.0.3 on 2020-02-09 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='items',
            name='dueDate',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='items',
            name='owner',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='items',
            name='rate',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='items',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
