# Generated by Django 5.0.3 on 2024-03-31 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petclinic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1, null=True),
        ),
    ]
