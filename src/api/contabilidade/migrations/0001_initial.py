# Generated by Django 4.1 on 2022-08-20 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Despesa",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("descricao", models.CharField(max_length=255)),
                ("valor", models.FloatField(default=0)),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Despesa",
                "verbose_name_plural": "Despesas",
                "db_table": "despesa",
            },
        ),
        migrations.CreateModel(
            name="Receita",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("descricao", models.CharField(max_length=255)),
                ("valor", models.FloatField(default=0)),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Receita",
                "verbose_name_plural": "Receitas",
                "db_table": "receita",
            },
        ),
    ]
