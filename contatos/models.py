from django.db import models
from django.contrib.auth.models import User


class Contato(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=150)
    email = models.EmailField(blank=True,null=True)
    categoria = models.CharField(max_length=30)
    ps = models.CharField(max_length=200,blank=True,null=True)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nome