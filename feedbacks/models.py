from django.db import models
from django.utils import timezone
from acompanhamentos.models import Acompanhamentos
from membros.models import CustomUser

titulo = (
    ('Genérico', 'Genérico'),
    ('Construtivo', 'Construtivo'),
    ('Negativo', 'Negativo'),
    ('Positivo', 'Positivo'),
    ('Ocorrência ofensiva', 'Ocorrência ofensiva'),
)
class Feedbacks(models.Model):
    fee_id = models.AutoField(db_column='fee_id', primary_key=True)
    fee_titulo = models.CharField(db_column='fee_titulo', max_length=255, choices=titulo, default='Prefiro não Falar')
    fee_descricao = models.TextField(db_column='fee_descricao', max_length=255, blank=True, null=True)
    fee_data = models.DateTimeField(db_column='fee_data', default = timezone.now)
    fee_arquivo = models.FileField(db_column='fee_arquivo', blank=True, null=True)
    fee_acompanhamento = models.ForeignKey(Acompanhamentos, on_delete=models.CASCADE, db_column='fee_acompanhamento')
    fee_emissor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, db_column='fee_emissor', blank=True, null=True)
    fee_inicial = models.IntegerField(db_column='fee_inicial', blank=True)
    fee_anterior = models.IntegerField(db_column='fee_anterior', blank=True)
    fee_proximo = models.IntegerField(db_column='fee_proximo', blank=True)
    fee_new = models.BooleanField(db_column='fee_new', default=True)
    def __str__(self):
        return self.fee_titulo

    class Meta:
        managed = False
        db_table = 'feedbacks'
