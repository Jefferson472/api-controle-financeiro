from django.contrib import admin

from .models.Receita import Receita
from .models.Despesa import Despesa


admin.site.register(Receita)
admin.site.register(Despesa)
