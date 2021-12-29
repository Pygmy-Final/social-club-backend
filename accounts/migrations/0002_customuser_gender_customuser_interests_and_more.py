# Generated by Django 4.0 on 2021-12-29 12:30

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=26),
        ),
        migrations.AddField(
            model_name='customuser',
            name='interests',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Reading', 'Reading'), ('Cycling', 'Cycling'), ('Hiking', 'Hiking'), ('Drawing', 'Drawing'), ('Photography', 'Photography'), ('Swimming', 'Swimming'), ('Sleeping', 'Sleeping'), ('Sports', 'Sports'), ('Gaming', 'Gaming')], max_length=26, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phonenumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profilePicture',
            field=models.ImageField(default='ProfilePictures/default.jpg', upload_to='ProfilePictures/'),
        ),
    ]