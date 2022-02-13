from django.db import models


class Empregado (models.Model):
    nome = models.CharField(max_length=100, help_text="Nome do Empregado")

    def __str__(self):
        return self.nome


