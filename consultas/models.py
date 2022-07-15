from turtle import back
import uuid
from django import forms
from django.forms import DateField
from django.utils import timezone
from django.db import models


class Consulta(models.Model):
    id               = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    paciente         = models.ForeignKey('pacientes.Paciente', related_name='consulta', blank=True, null=True, on_delete=models.CASCADE)
    usuario          = models.ForeignKey('usuarios.Usuario', related_name='consulta', on_delete=models.CASCADE)
    medico           = models.ForeignKey('medicos.Medico', related_name='consulta', on_delete=models.CASCADE)
    
    confirmado       = models.BooleanField(default=False)
    compareceu       = models.BooleanField(default=False)
    pago             = models.BooleanField(default=False)
    data_da_consulta = models.DateTimeField(blank=True, default=timezone.now)
    criado_em        = models.DateTimeField(default=timezone.now)
    atualizado_em    = models.DateTimeField(auto_now=True)
