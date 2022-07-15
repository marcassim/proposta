from core.models import Cliente, Proposta
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


# Proposta
@login_required(redirect_field_name="redirect_to")
def proposta(request, id=None, *args, **kwargs):
    contexto = {}
    contexto["proposta_base"] = Proposta.objects.get(id=id)

    return render(request, "proposta.html", contexto)
