from .BaseModel import BaseModel


class Despesa(BaseModel):
    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'
        db_table = 'despesa'
