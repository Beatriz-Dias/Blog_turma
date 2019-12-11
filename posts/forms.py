from django import forms
from .models import Pedido

class PedidoForms(forms.ModelForm):
 class Meta:
        model = Pedido
        fields = [
            'nome',
            'email',
            'cartao',
            'pagamento',
        ]
