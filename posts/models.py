from django.db import models
from django.utils import timezone

class Postagem(models.Model):
    opcoes_tema = [('RO', 'Romance'),
    ('TE', 'Tecnologia'),
    ('NO', 'Novidades'),
    ]

    nome = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)
    idade = models.IntegerField(default=1)
    tema  = models.CharField(max_length=2, choices=opcoes_tema)
    
    def __str__(self):
        return self.nome
    
class Pedido(models.Model):
    metodo_pagamento = [
        ('AV', 'Pagamento à vista'),
        ('P2', 'Parcelado em 2x'),
        ('P3', 'Parcelado em 3x'),
    ]
    nome = models.CharField(max_length=140)
    email = models.EmailField()
    cartao = models.IntegerField()
    pagamento = models.CharField(max_length=2, choices=metodo_pagamento)
    criado_em = models.DateTimeField(default=timezone.now)

    def __str__ (self):
        return self.nome