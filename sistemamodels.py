# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acompanhamento(models.Model):
    aco_id = models.IntegerField(primary_key=True)
    aco_semestre = models.CharField(max_length=6, blank=True, null=True)
    aco_aluno_pcd = models.ForeignKey('AlunoPcd', models.DO_NOTHING, db_column='aco_aluno_pcd', blank=True, null=True)
    aco_monitor = models.ForeignKey('Monitor', models.DO_NOTHING, db_column='aco_monitor', blank=True, null=True)
    aco_tutor = models.ForeignKey('Tutor', models.DO_NOTHING, db_column='aco_tutor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acompanhamento'


class AcopanhamentoDisciplina(models.Model):
    asdis_id = models.IntegerField(db_column='AsDis_id', primary_key=True)  # Field name made lowercase.
    asdis_disciplina = models.ForeignKey('Disciplinas', models.DO_NOTHING, db_column='AsDis_disciplina', blank=True, null=True)  # Field name made lowercase.
    asdis_acompanhamento = models.ForeignKey(Acompanhamento, models.DO_NOTHING, db_column='AsDis_acompanhamento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'acopanhamento_disciplina'


class Administrador(models.Model):
    adm_id = models.IntegerField(primary_key=True)
    adm_nome = models.CharField(max_length=255)
    adm_cpf = models.CharField(max_length=11)
    adm_email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'administrador'


class AlunoPcd(models.Model):
    alu_id = models.IntegerField(primary_key=True)
    alu_nome = models.CharField(max_length=255)
    alu_cpf = models.CharField(max_length=11)
    alu_sexo = models.CharField(max_length=1)
    alu_email = models.CharField(max_length=255)
    alu_telefone = models.CharField(max_length=255)
    alu_matricula = models.CharField(max_length=11)
    alu_deficiencias = models.CharField(max_length=255, blank=True, null=True)
    alu_curso = models.ForeignKey('Cursos', models.DO_NOTHING, db_column='alu_curso', blank=True, null=True)
    alu_periodo_academico = models.CharField(db_column='alu_Periodo_Academico', max_length=255)  # Field name made lowercase.
    alu_data_nascimento = models.DateField()

    class Meta:
        managed = False
        db_table = 'aluno_pcd'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class Avisos(models.Model):
    avi_id = models.IntegerField(primary_key=True)
    avi_titulo = models.CharField(max_length=255)
    avi_descricao = models.CharField(max_length=255, blank=True, null=True)
    avi_data = models.DateTimeField()
    avi_arquivos = models.TextField(blank=True, null=True)
    avi_administrador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='avi_administrador', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avisos'


class ContasUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    is_administrador = models.IntegerField()
    is_aluno = models.IntegerField()
    is_interprete = models.IntegerField()
    is_monitor = models.IntegerField()
    is_tutor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contas_user'


class ContasUserGroups(models.Model):
    user = models.ForeignKey(ContasUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contas_user_groups'
        unique_together = (('user', 'group'),)


class ContasUserUserPermissions(models.Model):
    user = models.ForeignKey(ContasUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contas_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cursos(models.Model):
    cur_id = models.IntegerField(primary_key=True)
    cur_nome = models.CharField(max_length=255)
    cur_quant_periodos = models.IntegerField()
    cur_horario = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'cursos'


class Disciplinas(models.Model):
    dis_id = models.IntegerField(primary_key=True)
    dis_nome = models.CharField(max_length=255)
    dis_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='dis_curso', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplinas'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(ContasUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Feedback(models.Model):
    fee_id = models.IntegerField(primary_key=True)
    fee_titulo = models.CharField(max_length=255)
    fee_descricao = models.CharField(max_length=255)
    fee_data = models.DateTimeField()
    fee_remetente = models.JSONField(blank=True, null=True)
    fee_acompanhamento = models.ForeignKey(Acompanhamento, models.DO_NOTHING, db_column='fee_acompanhamento', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback'


class Interpretacao(models.Model):
    asint_id = models.IntegerField(db_column='AsInt_id', primary_key=True)  # Field name made lowercase.
    asint_inicio = models.DateField(db_column='AsInt_inicio')  # Field name made lowercase.
    asint_fim = models.DateField(db_column='AsInt_fim', blank=True, null=True)  # Field name made lowercase.
    asint_interprete = models.ForeignKey('Interprete', models.DO_NOTHING, db_column='AsInt_interprete', blank=True, null=True)  # Field name made lowercase.
    asint_acompanhamento = models.ForeignKey(Acompanhamento, models.DO_NOTHING, db_column='AsInt_acompanhamento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'interpretacao'


class Interprete(models.Model):
    int_id = models.IntegerField(primary_key=True)
    int_nome = models.CharField(max_length=255)
    int_cpf = models.CharField(max_length=11)
    int_sexo = models.CharField(max_length=1)
    int_email = models.CharField(max_length=255)
    int_telefone = models.CharField(max_length=255)
    int_acompanhamento = models.ForeignKey(Acompanhamento, models.DO_NOTHING, db_column='int_acompanhamento', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interprete'


class Monitor(models.Model):
    mon_id = models.IntegerField(primary_key=True)
    mon_nome = models.CharField(max_length=255)
    mon_cpf = models.CharField(max_length=11)
    mon_sexo = models.CharField(max_length=1)
    mon_email = models.CharField(max_length=255)
    mon_telefone = models.CharField(max_length=255)
    mon_matricula = models.CharField(max_length=11)
    mon_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='mon_curso', blank=True, null=True)
    mon_periodo_academico = models.CharField(max_length=255)
    mon_tipo = models.CharField(max_length=7)
    mon_arquivos = models.TextField(blank=True, null=True)
    mon_aluno_pcd = models.ForeignKey(AlunoPcd, models.DO_NOTHING, db_column='mon_aluno_pcd', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitor'


class Monitoria(models.Model):
    asmon_id = models.IntegerField(db_column='AsMon_id', primary_key=True)  # Field name made lowercase.
    asmon_inicio = models.DateField(db_column='AsMon_inicio')  # Field name made lowercase.
    asmon_fim = models.DateField(db_column='AsMon_fim', blank=True, null=True)  # Field name made lowercase.
    asmon_monitor = models.ForeignKey(Monitor, models.DO_NOTHING, db_column='AsMon_monitor', blank=True, null=True)  # Field name made lowercase.
    asmon_acompanhamento = models.ForeignKey(Acompanhamento, models.DO_NOTHING, db_column='AsMon_acompanhamento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'monitoria'


class SistemaAvisos(models.Model):
    avi_id = models.IntegerField(primary_key=True)
    avi_titulo = models.CharField(max_length=255)
    avi_descricao = models.CharField(max_length=255, blank=True, null=True)
    avi_data = models.DateTimeField()
    avi_arquivos = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sistema_avisos'


class Tutor(models.Model):
    tut_id = models.IntegerField(primary_key=True)
    tut_nome = models.CharField(max_length=255)
    tut_cpf = models.CharField(max_length=11)
    tut_sexo = models.CharField(max_length=1)
    tut_email = models.CharField(max_length=255)
    tut_telefone = models.CharField(max_length=255)
    tut_matricula = models.CharField(max_length=11)
    tut_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='tut_curso', blank=True, null=True)
    tut_periodo_academico = models.CharField(max_length=255)
    tut_tipo = models.CharField(max_length=7)
    tut_arquivos = models.TextField(blank=True, null=True)
    tut_aluno_pcd = models.ForeignKey(AlunoPcd, models.DO_NOTHING, db_column='tut_aluno_pcd', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tutor'


class Tutoria(models.Model):
    astut_id = models.IntegerField(db_column='AsTut_id', primary_key=True)  # Field name made lowercase.
    astut_inicio = models.DateField(db_column='AsTut_inicio')  # Field name made lowercase.
    astut_fim = models.DateField(db_column='AsTut_fim', blank=True, null=True)  # Field name made lowercase.
    astut_tutor = models.ForeignKey(Tutor, models.DO_NOTHING, db_column='AsTut_tutor', blank=True, null=True)  # Field name made lowercase.
    astut_acompanhamento = models.ForeignKey(Acompanhamento, models.DO_NOTHING, db_column='AsTut_acompanhamento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tutoria'
