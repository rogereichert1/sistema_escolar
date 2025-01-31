from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    TIPO_USUARIO = [
        ("pai", "Pai"),
        ("filho", "Filho"),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_USUARIO)


class Filho(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="filhos/", null=True, blank=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)


class Atividade(models.Model):
    descricao = models.TextField()
    data = models.DateField()
    status = models.CharField(
        max_length=10, choices=[("concluído", "Concluído"),
                                ("pendente", "Pendente")]
    )
    nota = models.FloatField(null=True, blank=True)
    filho = models.ForeignKey(Filho, on_delete=models.CASCADE)


class Meta(models.Model):
    descricao = models.TextField()
    data_limite = models.DateField()
    progresso = models.FloatField(default=0)
    filho = models.ForeignKey(Filho, on_delete=models.CASCADE)
