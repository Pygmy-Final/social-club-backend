# Generated by Django 4.0 on 2021-12-31 19:45

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_friendrequest_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='interests',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Reading', 'Reading'), ('Cycling', 'Cycling'), ('Hiking', 'Hiking'), ('Drawing', 'Drawing'), ('Photography', 'Photography'), ('Swimming', 'Swimming'), ('Sleeping', 'Sleeping'), ('Sports', 'Sports'), ('Gaming', 'Gaming')], max_length=100, null=True),
        ),
    ]