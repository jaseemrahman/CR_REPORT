# Generated by Django 4.0.6 on 2022-07-21 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_consutationlist_pt_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consutationlist',
            name='pt_contact',
            field=models.CharField(max_length=10),
        ),
    ]
