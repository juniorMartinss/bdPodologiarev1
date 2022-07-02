create database bdpodologia;
use bdpodologia;

create table colaborador(
	codigo int unsigned not null primary key auto_increment,
    nome varchar(30) not null,
    salario double not null default '0',
    departamento varchar(45) not null,
    telefone varchar(20) not null,
    dataDeNascimento date not null,
    endereco varchar(150) not null,
    cep varchar(20) not null,
    valeTransporte varchar(5) not null,
    obs varchar(1000)

)Engine = InnoDB;

create table paciente(
	CPF int not null primary key auto_increment,
	nome varchar(150) not null,
	dateDeNascimento date not null,
    telefone varchar(100) not null,
    endereco varchar(150) not null,
    CEP varchar(20) not null
    
)Engine = InnoDB;

create table estoque(
	codigo int unsigned not null primary key auto_increment,
    produto varchar(200) not null,
    valor double(10,2) not null,
    quantidade int not null,
    fabricante varchar(150) not null,
    fornecedor varchar(150) not null,
    origem varchar(50) not null,
    obs varchar(1000) 
    
)Engine = InnoDB;

create table procedimentos(
	codigo int unsigned not null primary key auto_increment,
    procedimento varchar(100) not null,
    valor double(10,2) not null,
    paciente_CPF int unsigned default null
    
)Engine = InnoDB;

drop table estoque;

select * from colaborador