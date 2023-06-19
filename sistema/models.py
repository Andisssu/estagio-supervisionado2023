from django.db import models
from django.utils import timezone

Turnos = (
    ('manha', 'Manha'),
    ('tarde', 'Tarde'),
    ('noite', 'Noite'),
    ('integral', 'Integral'),
)
LaudoStatus = (
    ('ativo', 'Ativo'),
    ('inativo', 'Inativo'),
)

class Cursos(models.Model):

    cur_id = models.AutoField(db_column='cur_id', primary_key=True)
    cur_nome = models.CharField(db_column="cur_nome", max_length=255)
    cur_quant_periodos = models.IntegerField(db_column="cur_quant_periodos")
    cur_turno = models.CharField(db_column="cur_turno", max_length=8, choices=Turnos, default='manha')

    class Meta:
        managed = False
        db_table = 'cursos'

    def __str__(self):
        return self.cur_nome

class Disciplinas(models.Model):

    dis_id = models.AutoField(db_column='dis_id', primary_key=True)
    dis_nome = models.CharField(db_column='dis_nome', max_length=255)
    dis_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='dis_curso', blank=True, null=True)
    dis_carga_horaria = models.IntegerField(db_column='dis_carga_horaria')

    class Meta:
        managed = False
        db_table = 'disciplinas'
    def __str__(self):
        return "{0} ({1})".format(self.dis_nome, self.dis_curso)

class Laudos(models.Model):

    lau_id = models.AutoField(db_column='lau_id', primary_key=True)
    lau_status = models.CharField(db_column='lau_status', max_length=255, choices=LaudoStatus, default='ativo')
    lau_numero = models.CharField(db_column='lau_numero', max_length=255)
    lau_nome = models.CharField(db_column='lau_nome', max_length=255)
    lau_arquivo = models.FileField(db_column='lau_arquivo', blank=True, null=True)
    lau_aluno = models.ForeignKey('membros.AlunoPcd', on_delete=models.DO_NOTHING, db_column='lau_aluno', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laudos'

    def __str__(self):
        return "{0}: {1}".format(self.lau_numero, self.lau_nome)