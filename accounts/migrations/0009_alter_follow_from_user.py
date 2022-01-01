# Generated by Django 4.0 on 2022-01-01 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_follow_from_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='accounts.customuser'),
        ),
    ]