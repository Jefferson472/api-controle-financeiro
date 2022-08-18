from .BaseModel import BaseModel


class Receita(BaseModel):
    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        db_table = 'receita'
