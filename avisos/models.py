from django.db import models
from django.utils import timezone
from membros.models import Administrador

class Avisos(models.Model):
    avi_id = models.AutoField(db_column='avi_id', primary_key=True)
    avi_titulo = models.CharField(db_column='avi_titulo', max_length=255)
    avi_descricao = models.TextField(db_column='avi_descricao', max_length=255, blank=True, null=True)
    avi_data = models.DateTimeField(db_column='avi_data', default = timezone.now)
    avi_arquivos = models.FileField(db_column='avi_arquivos', blank=True, null=True)
    avi_administrador = models.ForeignKey(Administrador, on_delete=models.SET_NULL, db_column='avi_administrador', blank=True, null=True)
    avi_mostrar = models.BooleanField(db_column="avi_mostrar", default=True)
    def __str__(self):
        return self.avi_titulo

    class Meta:
        managed = False
        db_table = 'avisos'