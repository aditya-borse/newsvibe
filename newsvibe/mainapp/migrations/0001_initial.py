# Generated by Django 4.2.14 on 2024-07-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("summary", models.TextField(max_length=4000)),
                ("link", models.URLField()),
                ("sentiment", models.CharField(max_length=100)),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                ("thumbnail_link", models.URLField(max_length=500)),
            ],
        ),
    ]