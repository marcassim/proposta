from django import forms
from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.db.models import Avg, Sum
from django.utils.html import format_html

from .models import Cliente, Proposta


class PropostaAdmin(admin.ModelAdmin):
    
    # def get_changelist(self, request, **kwargs):
    #     return TotalChangeList

    list_display = ['cliente','data','pago','valor','imprimir']
    search_field=['cliente']
    list_filter=['cliente','data','situacao']
    # lista_editable=['valor']
    lista_per_page=30
    save_on_top=True

class ClienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Proposta, PropostaAdmin)
admin.site.register(Cliente, ClienteAdmin)
