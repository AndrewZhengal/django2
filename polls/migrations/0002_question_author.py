# Generated by Django 4.1.7 on 2023-02-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="author",
            field=models.CharField(default="Andrew Z.", max_length=255),
        ),
    ]