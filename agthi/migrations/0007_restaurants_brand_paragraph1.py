# Generated by Django 5.0.6 on 2024-08-02 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agthi', '0006_alter_job_application_apl_rec_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='brand_paragraph1',
            field=models.TextField(null=True),
        ),
    ]
