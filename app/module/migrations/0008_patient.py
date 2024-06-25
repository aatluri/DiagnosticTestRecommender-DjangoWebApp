# Generated by Django 4.0.10 on 2024-06-22 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0007_delete_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150)),
                ('phonenumber', models.IntegerField()),
                ('emailaddress', models.CharField(max_length=150)),
                ('dateofbirth', models.DateField(max_length=8)),
                ('gender', models.CharField(max_length=6)),
                ('smokingstatus', models.CharField(max_length=20)),
                ('drinkingstatus', models.CharField(max_length=20)),
                ('previnfection_hiv', models.CharField(max_length=20)),
                ('previnfection_hbv', models.CharField(max_length=20)),
                ('previnfection_hcv', models.CharField(max_length=20)),
                ('menstrualhistory', models.CharField(max_length=50)),
                ('comments', models.TextField(blank=True)),
            ],
        ),
    ]