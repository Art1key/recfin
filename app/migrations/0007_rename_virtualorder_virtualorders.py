# Generated by Django 5.0.6 on 2024-05-10 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_virtualorder_total_cost'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VirtualOrder',
            new_name='VirtualOrders',
        ),
    ]
