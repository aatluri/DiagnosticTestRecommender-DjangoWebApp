# Generated by Django 4.0.10 on 2024-06-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0009_alter_patient_drinkingstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='menstrualhistory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
