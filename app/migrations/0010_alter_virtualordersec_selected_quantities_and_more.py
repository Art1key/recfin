# Generated by Django 5.0.6 on 2024-05-10 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_virtualordersec_selected_dishes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtualordersec',
            name='selected_quantities',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='virtualordersec',
            name='total_cost',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
    ]
