# Generated by Django 4.1.3 on 2022-11-05 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("latestTech", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="information", old_name="Email", new_name="email",
        ),
        migrations.RenameField(
            model_name="information", old_name="Father_Name", new_name="father_Name",
        ),
        migrations.RenameField(
            model_name="information", old_name="File", new_name="file",
        ),
        migrations.RenameField(
            model_name="information", old_name="Gender", new_name="gender",
        ),
        migrations.RenameField(
            model_name="information", old_name="Name", new_name="name",
        ),
        migrations.RenameField(
            model_name="information", old_name="Password", new_name="password",
        ),
    ]
