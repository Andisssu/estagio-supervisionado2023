from django.db import models
from django.utils import timezone
from acompanhamentos.models import AcompanhamentoMonitores, AcompanhamentoTutores

class RelatoriosMon(models.Model):
    relM_id = models.AutoField(db_column='relM_id', primary_key=True)
    relM_titulo = models.CharField(db_column='relM_titulo', max_length=255)
    relM_data = models.DateTimeField(db_column='relM_data', default = timezone.now)
    relM_verificado = models.BooleanField(db_column='relM_verificado', default=False)
    relM_arquivo = models.FileField(db_column='relM_arquivo', blank=True, null=True)
    relM_monitoria = models.ForeignKey(AcompanhamentoMonitores, on_delete=models.SET_NULL, db_column='relM_monitoria', blank=True, null=True)
    def __str__(self):
        return self.relM_titulo

    class Meta:
        managed = False
        db_table = 'relatorios_monitoria'

    def verificar(self, request):
        self.relM_verificado = True
        self.save()

    def reverter(self, request):
        self.relM_verificado = False
        self.save()

class RelatoriosTut(models.Model):
    relT_id = models.AutoField(db_column='relT_id', primary_key=True)
    relT_titulo = models.CharField(db_column='relT_titulo', max_length=255)
    relT_data = models.DateTimeField(db_column='relT_data', default = timezone.now)
    relT_verificado = models.BooleanField(db_column='relT_verificado', default=False)
    relT_arquivo = models.FileField(db_column='relT_arquivo', blank=True, null=True)
    relT_tutoria = models.ForeignKey(AcompanhamentoTutores, on_delete=models.SET_NULL, db_column='relT_tutoria', blank=True, null=True)
    def __str__(self):
        return self.relT_titulo

    class Meta:
        managed = False
        db_table = 'relatorios_tutoria'

    def verificar(self, request):
        self.relT_verificado = True
        self.save()

    def reverter(self, request):
        self.relT_verificado = False
        self.save()
