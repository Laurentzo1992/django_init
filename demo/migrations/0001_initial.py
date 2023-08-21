# Generated by Django 4.2.4 on 2023-08-14 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                (
                    "nom_article",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Nom de l'article",
                    ),
                ),
                ("prix", models.FloatField()),
                ("description", models.TextField()),
            ],
        ),
    ]
