# Generated by Django 3.1.3 on 2020-12-29 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essentialatm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useracc',
            old_name='user_email',
            new_name='email',
        ),
        migrations.AddField(
            model_name='useracc',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
