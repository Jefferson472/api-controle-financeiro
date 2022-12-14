# Generated by Django 4.1 on 2022-08-24 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contabilidade", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="despesa",
            name="categoria",
            field=models.CharField(
                choices=[
                    ("alimentacao", "Alimentação"),
                    ("saude", "Saúde"),
                    ("moradia", "Moradia"),
                    ("transporte", "Transporte"),
                    ("educacao", "Educação"),
                    ("lazer", "Lazer"),
                    ("imprevistos", "Imprevistos"),
                    ("outras", "Outras"),
                ],
                default="Outras",
                max_length=11,
            ),
        ),
        migrations.AlterField(
            model_name="despesa",
            name="update_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="receita",
            name="update_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
