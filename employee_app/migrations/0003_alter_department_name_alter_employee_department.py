# Generated by Django 4.2.7 on 2023-12-02 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0002_alter_empskills_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(max_length=200),
        ),
    ]
