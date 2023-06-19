from django.db import models
from django.utils import timezone
from membros.models import AlunoPcd, Monitor, Tutor, Interprete
from sistema.models import Disciplinas

Dias = (
    ('Segunda-feira', 'Segunda-feira'),
    ('Terça-feira', 'Terça-feira'),
    ('Quarta-feira', 'Quarta-feira'),
    ('Quinta-feira', 'Quinta-feira'),
    ('Sexta-feira', 'Sexta-feira'),
    ('Sábado', 'Sábado')
)

class Acompanhamentos(models.Model):
    aco_id = models.AutoField(db_column='aco_id', primary_key=True)
    aco_semestre = models.CharField(db_column='aco_semestre', max_length=6)
    aco_inicio = models.DateField(db_column='aco_inicio', default = timezone.now)
    aco_fim = models.DateField(db_column='aco_fim', default = timezone.now)
    aco_aluno_pcd = models.ForeignKey(AlunoPcd, on_delete=models.SET_NULL, db_column='aco_aluno_pcd', blank=True, null=True)
    aco_disciplinas = models.ManyToManyField(Disciplinas, through='AcompanhamentoDisciplinas')
    aco_interpretes = models.ManyToManyField(Interprete, through='AcompanhamentoInterpretes')
    aco_monitores = models.ManyToManyField(Monitor, through='AcompanhamentoMonitores')
    aco_tutores = models.ManyToManyField(Tutor, through='AcompanhamentoTutores')
    def __str__(self):
        return "{0}: {1}".format(self.aco_aluno_pcd, self.aco_semestre)

    class Meta:
        managed = False
        db_table = 'acompanhamento'

class AcompanhamentoDisciplinas(models.Model):
    AsDis_id = models.AutoField(db_column='AsDis_id', primary_key=True)
    AsDis_disciplina = models.ForeignKey(Disciplinas, on_delete=models.SET_NULL, db_column='AsDis_disciplina', blank=True, null=True)
    AsDis_acompanhamento = models.ForeignKey(Acompanhamentos, on_delete=models.SET_NULL, db_column='AsDis_acompanhamento', blank=True, null=True)

    def __str__(self):
        return self.AsDis_disciplina.__str__()

    class Meta:
        managed = False
        db_table = 'acompanhamento_disciplina'

class AcompanhamentoInterpretes(models.Model):
    AsInt_id = models.AutoField(db_column='AsInt_id', primary_key=True)
    AsInt_inicio = models.DateField(db_column='AsInt_inicio', default = timezone.now)
    AsInt_fim = models.DateField(db_column='AsInt_fim', default = timezone.now)
    AsInt_interprete = models.ForeignKey(Interprete, on_delete=models.SET_NULL, db_column='AsInt_interprete', blank=True, null=True)
    AsInt_acompanhamento = models.ForeignKey(Acompanhamentos, on_delete=models.SET_NULL, db_column='AsInt_acompanhamento', blank=True, null=True)

    def __str__(self):
        return "{0}: {1}".format(self.AsInt_interprete, self.AsInt_acompanhamento)

    class Meta:
        managed = False
        db_table = 'acompanhamento_interprete'

class AcompanhamentoMonitores(models.Model):
    AsMon_id = models.AutoField(db_column='AsMon_id', primary_key=True)
    AsMon_inicio = models.DateField(db_column='AsMon_inicio', default = timezone.now)
    AsMon_fim = models.DateField(db_column='AsMon_fim', default = timezone.now)
    AsMon_monitor = models.ForeignKey(Monitor, on_delete=models.SET_NULL, db_column='AsMon_monitor', blank=True, null=True)
    AsMon_acompanhamento = models.ForeignKey(Acompanhamentos, on_delete=models.SET_NULL, db_column='AsMon_acompanhamento', blank=True, null=True)

    def __str__(self):
        return "{0}: {1}".format(self.AsMon_monitor, self.AsMon_acompanhamento)

    class Meta:
        managed = False
        db_table = 'acompanhamento_monitoria'

class AcompanhamentoTutores(models.Model):
    AsTut_id = models.AutoField(db_column='AsTut_id', primary_key=True)
    AsTut_inicio = models.DateField(db_column='AsTut_inicio', default = timezone.now)
    AsTut_fim = models.DateField(db_column='AsTut_fim', default = timezone.now)
    AsTut_tutor = models.ForeignKey(Tutor, on_delete=models.SET_NULL, db_column='AsTut_tutor', blank=True, null=True)
    AsTut_acompanhamento = models.ForeignKey(Acompanhamentos, on_delete=models.SET_NULL, db_column='AsTut_acompanhamento', blank=True, null=True)

    def __str__(self):
        return "{0}: {1}".format(self.AsTut_tutor, self.AsTut_acompanhamento)

    class Meta:
        managed = False
        db_table = 'acompanhamento_tutoria'

class HorariosDisciplina(models.Model):
    HoDis_id = models.AutoField(db_column='HoDis_id', primary_key=True)
    HoDis_dia = models.CharField(db_column='HoDis_dia', max_length=255, choices=Dias)
    HoDis_inicio = models.TimeField(db_column='HoDis_inicio', default=timezone.now)
    HoDis_fim = models.TimeField(db_column='HoDis_Fim', default=timezone.now)
    HoDis_disciplina = models.ForeignKey(AcompanhamentoDisciplinas, on_delete=models.SET_NULL, db_column='HoDis_disciplina', blank=True, null=True)

    def __str__(self):
        return self.HoDis_disciplina.__str__()

    class Meta:
        managed = False
        db_table = 'horarios_disciplina'