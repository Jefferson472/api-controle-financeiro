from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255)
    valor = models.FloatField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    # TODO: verificar se a data criação fixa e data_att variável 
    data_att = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao
