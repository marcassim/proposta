# -*- Mode: Python; coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.db import models
from django.db.models import Avg, Sum
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from localflavor.br.br_states import STATE_CHOICES


class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=100)

    def __str__(self):
        return self.nome


class Proposta(models.Model):
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    cpf = models.CharField("CPF", blank=True, max_length=14)
    cnpj = models.CharField("CNPJ", blank=True, max_length=18)
    endereco = models.CharField("Endereço", blank=True, max_length=200)
    bairro = models.CharField("Bairro", blank=True, max_length=100)
    cidade = models.CharField("Cidade", blank=True, max_length=100)
    estado = models.CharField(
        max_length=2, null=True, blank=True, choices=STATE_CHOICES
    )
    data = models.DateField("Data de Emissão")
    VALIDADE_CHOICES = (
        ("Quinze", "15 (Quinze)"),
        ("Trinta", "30 (Trinta)"),
        ("Sessenta", "60 (Sessenta)"),
    )

    validade = models.CharField(
        "Validade", blank=True, max_length=200, choices=VALIDADE_CHOICES
    )
    valor = models.DecimalField("Valor a pagar", max_digits=8, decimal_places=2)
    CATEGORY_CHOICES = (
        ("Atrasado", "Atrasado"),
        ("AVencer", "Á Vencer"),
        ("Pago", "Pago"),
    )

    situacao = models.CharField("Situação", max_length=200, choices=CATEGORY_CHOICES)
    pago = models.BooleanField(default=False)

    dominio = models.CharField(
        "Dominio do Site",
        blank=True,
        max_length=200,
        help_text="URL - exe: seudominio.com.br",
    )
    dominio_login = models.CharField(
        "Acesso ao Admin",
        max_length=200,
        blank=True,
        help_text="URL - exe: seudominio.com.br/admin",
    )
    login = models.CharField("Login", max_length=30, blank=True)
    senha = models.CharField("Senha", max_length=30, blank=True)

    def imprimir(self):
        return mark_safe(
            """<a href=\"/proposta/%s/\" target="_blank"><img src=\"/static/images/b_print.png\"></a>"""
            % self.id
        )

    class Meta:
        ordering = ["-data"]
        verbose_name = "Proposta"
        verbose_name_plural = "Propostas"

    def __str__(self):
        if self.cliente.nome:
            return self.cliente.nome
        else:
            return self.custom_alias_name
