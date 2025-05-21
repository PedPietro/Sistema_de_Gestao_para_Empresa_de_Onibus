/* Lógico_Passagem: */

CREATE TABLE Motorista(
	nome varchar(50),
	idMotorista int primary key identity
	)

CREATE TABLE Onibus (
    idOnibus int PRIMARY KEY Identity,
    capacidade int,
    marca varchar(20),
    modelo varchar(20),
	idMotorista int,
	constraint fkIdidMotorista foreign key(idMotorista)
		references Motorista(idMotorista),
);

CREATE TABLE Passageiro (
    cpf char(11) PRIMARY KEY,
    nome varchar(50),
    telefone varchar(15),
    dataNascimento datetime,
    email varchar(100)
)

CREATE TABLE Cidade (
    idCidade int PRIMARY KEY Identity,
    nome varchar(50),
    endereco_terminal varchar(100),
    siglaUF char(2)
)

/*
Terminal: 
	Terminal Centro
	Terminal Campo Grande
	Terminal Barão Geraldo
*/



CREATE TABLE Viagem (
    idViagem int PRIMARY KEY Identity,
    distancia int,  
    custo money,
    idCidadeOrigem int,
    idCidadeDestino int,
	constraint fkIdCidadeOrigem foreign key(idCidadeOrigem)
		references Cidade(idCidade),
    constraint fkIdCidadeDestino foreign key(idCidadeDestino)
		references Cidade(idCidade)
)

CREATE TABLE Passagem (
    IdPassagem int PRIMARY KEY Identity,
    assento int,
    data_e_hora datetime,
    idOnibus int,
    cpf char(11),
    idViagem int
)

CREATE TABLE UF (
    siglaUF char(2) PRIMARY KEY,
    nomeUF varchar(30)
);
 
ALTER TABLE Cidade ADD CONSTRAINT FK_Cidade_2
    FOREIGN KEY (siglaUF)
    REFERENCES UF (siglaUF)
    ON DELETE CASCADE;
 
ALTER TABLE Passagem ADD CONSTRAINT FK_Passagem_2
    FOREIGN KEY (idOnibus)
    REFERENCES Onibus (idOnibus)
    ON DELETE CASCADE;
 
ALTER TABLE Passagem ADD CONSTRAINT FK_Passagem_3
    FOREIGN KEY (cpf)
    REFERENCES Passageiro (cpf);
 
ALTER TABLE Passagem ADD CONSTRAINT FK_Passagem_4
    FOREIGN KEY (idViagem)
    REFERENCES Viagem (idViagem);

select * from Passageiro
select * from Passagem
select * from Viagem
select * from Onibus
select * from UF
select * from Cidade
select * from Motorista