from django.db import models


class Despesa(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255)
    valor = models.FloatField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    # TODO: verificar se a data criação fixa e data_att variável 
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'
        db_table = 'despesa'
