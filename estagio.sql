CREATE DATABASE estagio;

#NOME DO BANCO
use estagio;

#CRIAÇÃO DE TABELAS

create table if not exists CURSOS (
	cur_id int not null auto_increment,
    cur_nome varchar(255) not null,
    cur_quant_periodos int not null,
    cur_turno enum('Manhã','Tarde','Noite','Integral') not null,
    primary key(cur_id)
);

create table if not exists DISCIPLINAS (
	dis_id int not null auto_increment,
    dis_nome varchar(255) not null,
    dis_curso int,
    dis_carga_horaria int not null,
    primary key(dis_id),
    foreign key(dis_curso) references CURSOS(cur_id)
);

create table if not exists ALUNO_PCD (
	alu_id int not null auto_increment,
    alu_nome varchar(255) not null,
    alu_cpf char(11) not null,
    alu_genero char(1) not null,
    alu_email_pessoal varchar(255) not null,
    alu_email_institucional varchar(255) not null,
    alu_telefone varchar(255) not null,
    alu_endereco_cep varchar(255),
    alu_endereco_descricao varchar(255),
    alu_endereco_cidade char(2),
    alu_matricula char(11) not null,
    alu_deficiencias varchar(255),
    alu_curso int,
    alu_periodo_academico varchar(255) not null,
    alu_data_nascimento date not null,
    alu_ativo bool,
    alu_usuario int,
    permissao int,
    primary key(alu_id),
    foreign key(alu_curso) references CURSOS(cur_id)
);

create table if not exists MONITOR (
	mon_id int not null auto_increment,
    mon_nome varchar(255) not null,
    mon_cpf char(11) not null,
    mon_genero char(1) not null,
    mon_email_pessoal varchar(255) not null,
    mon_email_institucional varchar(255) not null,
    mon_telefone varchar(255) not null,
    mon_endereco_cep varchar(255),
    mon_endereco_descricao varchar(255),
    mon_endereco_cidade char(2),
    mon_matricula char(11) not null,
    mon_curso int,
    mon_periodo_academico varchar(255) not null,
    mon_ativo bool,
    mon_usuario int,
    permissao int,
    primary key(mon_id),
    foreign key(mon_curso) references CURSOS(cur_id)
);

create table if not exists TUTOR (
	tut_id int not null auto_increment,
    tut_nome varchar(255) not null,
    tut_cpf char(11) not null,
    tut_genero char(1) not null,
    tut_email_pessoal varchar(255) not null,
    tut_email_institucional varchar(255) not null,
    tut_telefone varchar(255) not null,
    tut_endereco_cep varchar(255),
    tut_endereco_descricao varchar(255),
    tut_endereco_cidade char(2),
    tut_matricula char(11) not null,
    tut_curso int,
    tut_periodo_academico varchar(255) not null,
    tut_ativo bool,
    tut_usuario int,
    permissao int,
    primary key(tut_id),
    foreign key(tut_curso) references CURSOS(cur_id)
);

create table if not exists ADMINISTRADOR (
	adm_id int not null auto_increment,
    adm_nome varchar(255) not null,
    adm_cpf char(11) not null,
    adm_email varchar(255) not null,
    adm_usuario int,
    permissao int,
    primary key(adm_id)
);

create table if not exists AVISOS (
	avi_id int not null auto_increment,
    avi_titulo varchar(255) not null,
    avi_descricao varchar(255),
    avi_data datetime not null,
    avi_arquivos mediumtext,
    avi_administrador int,
    avi_mostrar bool,
    primary key(avi_id),
    foreign key(avi_administrador) references ADMINISTRADOR(adm_id)
);

create table if not exists ACOMPANHAMENTO (
	aco_id int not null auto_increment,
    aco_semestre char(6),
    aco_inicio date not null,
    aco_fim date,
    aco_aluno_pcd int,
    aco_monitor int,
    aco_tutor int,
    primary key(aco_id),
    foreign key(aco_aluno_pcd) references ALUNO_PCD(alu_id)
);

create table if not exists INTERPRETE (
	int_id int not null auto_increment,
    int_nome varchar(255) not null,
    int_cpf char(11) not null,
    int_genero char(1) not null,
    int_email_pessoal varchar(255) not null,
    int_email_institucional varchar(255) not null,
    int_telefone varchar(255) not null,
    int_ativo bool,
    int_usuario int,
    permissao int,
    primary key(int_id)
);

create table if not exists ACOMPANHAMENTO_DISCIPLINA (
	AsDis_id int not null auto_increment,
    AsDis_disciplina int,
    AsDis_acompanhamento int,
    primary key(AsDis_id),
    foreign key(AsDis_disciplina) references DISCIPLINAS(dis_id),
    foreign key(AsDis_acompanhamento) references ACOMPANHAMENTO(aco_id)
);

create table if not exists ACOMPANHAMENTO_INTERPRETE (
	AsInt_id int not null auto_increment,
    AsInt_inicio date not null,
    AsInt_fim date,
    AsInt_interprete int,
    AsInt_acompanhamento int,
    primary key(AsInt_id),
    foreign key(AsInt_Interprete) references INTERPRETE(int_id),
    foreign key(AsInt_Acompanhamento) references ACOMPANHAMENTO(aco_id)
);

create table if not exists ACOMPANHAMENTO_MONITORIA (
	AsMon_id int not null auto_increment,
    AsMon_inicio date not null,
    AsMon_fim date,
    AsMon_monitor int,
    AsMon_acompanhamento int,
    primary key(AsMon_id),
    foreign key(AsMon_monitor) references MONITOR(mon_id),
    foreign key(AsMon_acompanhamento) references ACOMPANHAMENTO(aco_id)
);

create table if not exists ACOMPANHAMENTO_TUTORIA (
	AsTut_id int not null auto_increment,
    AsTut_inicio date not null,
    AsTut_fim date,
    AsTut_tutor int,
    AsTut_acompanhamento int,
    primary key(AsTut_id),
    foreign key(AsTut_tutor) references TUTOR(tut_id),
    foreign key(AsTut_acompanhamento) references ACOMPANHAMENTO(aco_id)
);

create table if not exists HORARIOS_DISCIPLINA (
	HoDis_id int not null auto_increment,
    HoDis_dia enum('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado'),
    HoDis_inicio time,
    HoDis_fim time,
    HoDis_disciplina int,
    primary key(HoDis_id),
    foreign key(HoDis_disciplina) references ACOMPANHAMENTO_DISCIPLINA(AsDis_id)
);

create table if not exists FEEDBACKS (
	fee_id int not null auto_increment,
    fee_titulo varchar(255) not null,
    fee_descricao varchar(255) not null,
    fee_data datetime not null,
    fee_arquivo mediumtext,
    fee_acompanhamento int,
    primary key(fee_id),
    foreign key(fee_acompanhamento) references ACOMPANHAMENTO(aco_id)
);

create table if not exists LAUDOS (
	lau_id int not null auto_increment,
    lau_status enum('Ativo', 'Inativo') not null,
    lau_numero varchar(255) not null,
    lau_nome varchar(255) not null,
    lau_arquivo mediumtext not null,
    lau_aluno int,
    primary key(lau_id),
    foreign key(lau_aluno) references ALUNO_PCD(alu_id)
);

create table if not exists RELATORIOS_MONITORIA (
	relM_id int not null auto_increment,
    relM_titulo varchar(255) not null,
    relM_data datetime not null,
    relM_verificado bool,
    relM_arquivo mediumtext,
    relM_monitoria int,
    primary key(relM_id),
    foreign key(relM_monitoria) references ACOMPANHAMENTO_MONITORIA(AsMon_id)
);

create table if not exists RELATORIOS_TUTORIA (
	relT_id int not null auto_increment,
    relT_titulo varchar(255) not null,
    relT_data datetime not null,
    relT_verificado bool,
    relT_arquivo mediumtext,
    relT_tutoria int,
    primary key(relT_id),
    foreign key(relT_tutoria) references ACOMPANHAMENTO_TUTORIA(AsTut_id)
);


use estagio;

#CCET
insert into CURSOS (cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (1, "Sistemas de Informação", 8, 4);
insert into CURSOS (cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (2, "Engenharia Civil", 10, 4);
insert into CURSOS (cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (3, "Engenharia Elétrica", 10, 4);
insert into CURSOS (cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (4, "Matemática", 8, 2);

#CELA
insert into CURSOS (cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (5, "Artes Cênicas: Teatro", 8, 2);
insert into CURSOS (cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (6, "Letras: Espanhol", 8, 3);
insert into CURSOS (cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (7, "Letras: Francês", 8, 2);
insert into CURSOS (cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (8, "Letras: Inglês", 8, 2);
insert into CURSOS (cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (9, "Letras: Libras - Língua Portuguesa", 8, 2);
insert into CURSOS (cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (10, "Letras: Português", 8, 2);
insert into CURSOS (cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (11, "Música", 8, 3);
insert into CURSOS (cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (12, "Pedagogia", 8, 2);

#CCBN
insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (13, "Ciências Biológicas", 8, 1);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (14, "Engenharia Agronômica", 10, 4);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (15, "Engenharia Florestal", 10, 4);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (16, "Física", 8, 2);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (17, "Medicina Veterinária", 10, 4);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (18, "Química", 8, 1);


#CCSD
insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (19, "Educação Física (bacharelado)", 8, 1);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (20, "Educação Física (licenciatura)", 8, 1);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (21, "Enfermagem", 8, 4);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (22, "Medicina", 12, 4);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (23, "Nutrição", 10, 4);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (24, "Saúde Coletiva", 8, 4);


#CCJSA
insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (25, "Ciências Econômicas", 10, 3);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (26, "Direito", 10, 3);


#CFCH
insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (27, "Ciênicas Sociais", 6, 4);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (28, "Comunicação Social/Jornalismo", 8, 3);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (29, "Filosofia", 8, 3);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (30, "Geografia (bacharelado)", 8, 2);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (31, "Geografia (licenciatura)", 8, 1);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (32, "História (bacharelado)", 8, 1);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (33, "História (licenciatura - matutino)", 8, 1);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (34, "História (licenciatura - noturno)", 8, 3);

insert into CURSOS ( cur_id, cur_nome, cur_quant_periodos, cur_turno)
	values (35, "Psicologia", 10, 4);