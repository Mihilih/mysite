# Generated by Django 3.2.5 on 2022-01-08 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerps', '0007_alter_journal_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='journal', to='cerps.People'),
        ),
    ]
