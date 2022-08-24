from django.db import models


class Despesa(models.Model):
    CATEGORIES = (
        ('alimentacao', 'Alimentação'),
        ('saude', 'Saúde'),
        ('moradia', 'Moradia'),
        ('transporte', 'Transporte'),
        ('educacao', 'Educação'),
        ('lazer', 'Lazer'),
        ('imprevistos', 'Imprevistos'),
        ('outras', 'Outras'),
    )

    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255)
    valor = models.FloatField(default=0)
    categoria = models.CharField(
        max_length=11, choices=CATEGORIES, default='Outras') 
    create_at = models.DateTimeField(auto_now_add=True)
    # TODO: verificar se a data criação fixa e data_att variável
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'
        db_table = 'despesa'
