from django.contrib.auth import authenticate
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.db import models
from sistema.models import Cursos

generos = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outros')
)
cidades = (
    ('RB', 'Rio Branco'),
    ('CS', 'Cruzeiro do Sul'),
)
PERMISSOES = (
    (1, 'Admin'),
    (2, 'Aluno'),
    (3, 'Monitor'),
    (4, 'Tutor'),
    (5, 'Interprete'),
)

# Create your models here.

class CustomUserManager(BaseUserManager):
    #USER_TYPE = (
    #     (1, 'Admin'),
    #     (2, 'Aluno'),
    #     (3, 'Monitor'),
    #     (4, 'Tutor'),
    #     (5, 'Interprete'),
    #)
    def create_user(self, username, email, user_type, password=None):
        if not user_type:
            raise ValueError('Users must have a type')
        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            user_type=user_type,
        )
        user.is_active = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.is_active = True
        user.user_type = 1
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
class CustomUser(AbstractUser, PermissionsMixin):
    user_type = models.PositiveSmallIntegerField(choices=PERMISSOES)
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

class Administrador(models.Model):
    adm_id = models.AutoField(db_column='adm_id', primary_key=True)
    adm_nome = models.CharField(db_column='adm_nome', max_length=255)
    adm_cpf = models.CharField(db_column='adm_cpf', max_length=11)
    adm_email = models.EmailField(db_column='adm_email', max_length=255)
    adm_usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_column='adm_usuario')
    permissao = models.IntegerField(db_column='permissao', choices=PERMISSOES, default=1)

    class Meta:
        managed = False
        db_table = 'administrador'
    def __str__(self):
        return self.adm_nome

class AlunoPcd(models.Model):
    alu_id = models.AutoField(db_column='alu_id', primary_key=True)
    alu_nome = models.CharField(db_column='alu_nome', max_length=255)
    alu_cpf = models.CharField(db_column='alu_cpf', max_length=11)
    alu_genero = models.CharField(db_column='alu_genero', max_length=1, choices=generos)
    alu_email_pessoal = models.EmailField(db_column='alu_email_pessoal', max_length=255)
    alu_email_institucional = models.EmailField(db_column='alu_email_institucional', max_length=255)
    alu_telefone = models.CharField(db_column='alu_telefone', max_length=255)
    alu_endereco_cep = models.CharField(db_column='alu_endereco_cep', max_length=255)
    alu_endereco_descricao = models.CharField(db_column='alu_endereco_descricao', max_length=255)
    alu_endereco_cidade = models.CharField(db_column='alu_endereco_cidade', max_length=255, choices=cidades)
    alu_matricula = models.CharField(db_column='alu_matricula', max_length=11)
    alu_deficiencias = models.CharField(db_column='alu_deficiencias', max_length=255, blank=True, null=True)
    alu_curso = models.ForeignKey(Cursos, on_delete=models.PROTECT, db_column='alu_curso', blank=True, null=True)
    alu_periodo_academico = models.CharField(db_column='alu_periodo_academico', max_length=255)  # Field name made lowercase.
    alu_data_nascimento = models.DateField(db_column='alu_data_nascimento')
    alu_ativo = models.BooleanField(db_column="alu_ativo", default=False)
    alu_usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_column='alu_usuario')
    permissao = models.IntegerField(db_column='permissao', choices=PERMISSOES, default=2)

    class Meta:
        managed = False
        db_table = 'aluno_pcd'

    def __str__(self):
        return self.alu_nome

    def ativar(self, request):
        self.alu_ativo = True
        self.alu_usuario.is_active = True
        self.alu_usuario.save()
        self.save()

    def desativar(self, request):
        self.alu_ativo = False
        self.alu_usuario.is_active = False
        self.alu_usuario.save()
        self.save()

class Monitor(models.Model):
    mon_id = models.AutoField(db_column='mon_id', primary_key=True)
    mon_nome = models.CharField(db_column='mon_nome', max_length=255)
    mon_cpf = models.CharField(db_column='mon_cpf', max_length=11)
    mon_genero = models.CharField(db_column='mon_genero', max_length=1, choices=generos)
    mon_email_pessoal = models.EmailField(db_column='mon_email_pessoal', max_length=255)
    mon_email_institucional = models.EmailField(db_column='mon_email_institucional', max_length=255)
    mon_telefone = models.CharField(db_column='mon_telefone', max_length=255)
    mon_endereco_cep = models.CharField(db_column='mon_endereco_cep', max_length=255)
    mon_endereco_descricao = models.CharField(db_column='mon_endereco_descricao', max_length=255)
    mon_endereco_cidade = models.CharField(db_column='mon_endereco_cidade', max_length=255, choices=cidades)
    mon_matricula = models.CharField(db_column='mon_matricula', max_length=11)
    mon_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='mon_curso', blank=True, null=True)
    mon_periodo_academico = models.CharField(db_column='mon_periodo_academico', max_length=255)
    mon_ativo = models.BooleanField(db_column="mon_ativo", default=False)
    mon_usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_column='mon_usuario')
    permissao = models.IntegerField(db_column='permissao', choices=PERMISSOES, default=3)

    class Meta:
        managed = False
        db_table = 'monitor'

    def __str__(self):
        return self.mon_nome

    def ativar(self, request):
        self.mon_ativo = True
        self.mon_usuario.is_active = True
        self.mon_usuario.save()
        self.save()

    def desativar(self, request):
        self.mon_ativo = False
        self.mon_usuario.is_active = False
        self.mon_usuario.save()
        self.save()

class Tutor(models.Model):
    tut_id = models.AutoField(db_column='tut_id', primary_key=True)
    tut_nome = models.CharField(db_column='tut_nome', max_length=255)
    tut_cpf = models.CharField(db_column='tut_cpf', max_length=11)
    tut_genero = models.CharField(db_column='tut_genero', max_length=1, choices=generos)
    tut_email_pessoal = models.EmailField(db_column='tut_email_pessoal', max_length=255)
    tut_email_institucional = models.EmailField(db_column='tut_email_institucional', max_length=255)
    tut_telefone = models.CharField(db_column='tut_telefone', max_length=255)
    tut_endereco_cep = models.CharField(db_column='tut_endereco_cep', max_length=255)
    tut_endereco_descricao = models.CharField(db_column='tut_endereco_descricao', max_length=255)
    tut_endereco_cidade = models.CharField(db_column='tut_endereco_cidade', max_length=255, choices=cidades)
    tut_matricula = models.CharField(db_column='tut_matricula', max_length=11)
    tut_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='tut_curso', blank=True, null=True)
    tut_periodo_academico = models.CharField(db_column='tut_periodo_academico', max_length=255)
    tut_ativo = models.BooleanField(db_column="tut_ativo", default=False)
    tut_usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_column='tut_usuario')
    permissao = models.IntegerField(db_column='permissao', choices=PERMISSOES, default=4)

    class Meta:
        managed = False
        db_table = 'tutor'
    def __str__(self):
        return self.tut_nome

    def ativar(self, request):
        self.tut_ativo = True
        self.tut_usuario.is_active = True
        self.tut_usuario.save()
        self.save()

    def desativar(self, request):
        self.tut_ativo = False
        self.tut_usuario.is_active = False
        self.tut_usuario.save()
        self.save()

class Interprete(models.Model):
    int_id = models.AutoField(db_column='int_id', primary_key=True)
    int_nome = models.CharField(db_column='int_nome', max_length=255)
    int_cpf = models.CharField(db_column='int_cpf', max_length=11)
    int_genero = models.CharField(db_column='int_genero', max_length=1, choices=generos)
    int_email_pessoal = models.EmailField(db_column='int_email_pessoal', max_length=255)
    int_email_institucional = models.EmailField(db_column='int_email_institucional', max_length=255)
    int_telefone = models.CharField(db_column='int_telefone', max_length=255)
    int_ativo = models.BooleanField(db_column="int_ativo", default=True)
    int_usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_column='int_usuario')
    permissao = models.IntegerField(db_column='permissao', choices=PERMISSOES, default=5)

    class Meta:
        managed = False
        db_table = 'interprete'
    def __str__(self):
        return self.int_nome

    def ativar(self, request):
        self.int_ativo = True
        self.int_usuario.is_active = True
        self.int_usuario.save()
        self.save()

    def desativar(self, request):
        self.int_ativo = False
        self.int_usuario.is_active = False
        self.int_usuario.save()
        self.save()