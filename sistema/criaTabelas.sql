create schema EmpresaOnibus

/* Lógico_Passagem: */

CREATE TABLE EmpresaOnibus.Motorista(
	nome varchar(50),
	idMotorista int primary key identity
	)

CREATE TABLE EmpresaOnibus.Onibus (
    idOnibus int PRIMARY KEY Identity,
    capacidade int,
    marca varchar(20),
    modelo varchar(20),
	idMotorista int,
	constraint fkIdidMotorista foreign key(idMotorista)
		references EmpresaOnibus.Motorista(idMotorista),
);

CREATE TABLE EmpresaOnibus.Passageiro (
	idPassageiro int primary key identity,
    cpf char(11),
    nome varchar(50),
    telefone varchar(15),
    dataNascimento date,
    email varchar(100)
)

CREATE TABLE EmpresaOnibus.Cidade (
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



CREATE TABLE EmpresaOnibus.Viagem (
    idViagem int PRIMARY KEY Identity,
    distancia int,  
    custo money,
    idCidadeOrigem int,
    idCidadeDestino int,
	constraint fkIdCidadeOrigem foreign key(idCidadeOrigem)
		references EmpresaOnibus.Cidade(idCidade),
    constraint fkIdCidadeDestino foreign key(idCidadeDestino)
		references EmpresaOnibus.Cidade(idCidade)
)

CREATE TABLE EmpresaOnibus.Passagem (
    IdPassagem int PRIMARY KEY Identity,
    assento int,
    data_e_hora datetime,
    idOnibus int,
    idPassageiro int,
    idViagem int
)

CREATE TABLE EmpresaOnibus.UF (
    siglaUF char(2) PRIMARY KEY,
    nomeUF varchar(30)
);
 
ALTER TABLE EmpresaOnibus.Cidade ADD CONSTRAINT FK_Cidade_2
    FOREIGN KEY (siglaUF)
    REFERENCES EmpresaOnibus.UF (siglaUF)
    ON DELETE CASCADE;
 
ALTER TABLE EmpresaOnibus.Passagem ADD CONSTRAINT FK_Passagem_2
    FOREIGN KEY (idOnibus)
    REFERENCES EmpresaOnibus.Onibus (idOnibus)
    ON DELETE CASCADE;
 
ALTER TABLE EmpresaOnibus.Passagem ADD CONSTRAINT FK_Passagem_3
    FOREIGN KEY (idPassageiro)
    REFERENCES EmpresaOnibus.Passageiro (idPassageiro);
 
ALTER TABLE EmpresaOnibus.Passagem ADD CONSTRAINT FK_Passagem_4
    FOREIGN KEY (idViagem)
    REFERENCES EmpresaOnibus.Viagem (idViagem);

select * from EmpresaOnibus.Passageiro
select * from EmpresaOnibus.Passagem
select * from EmpresaOnibus.Viagem
select * from EmpresaOnibus.Onibus
select * from EmpresaOnibus.UF
select * from EmpresaOnibus.Cidade
select * from EmpresaOnibus.Motorista


--1 - Tabela UF

INSERT INTO EmpresaOnibus.UF (siglaUF, nomeUF) VALUES 
('SP', 'São Paulo'),
('RJ', 'Rio de Janeiro'),
('MG', 'Minas Gerais'),
('MS', 'Mato Grosso do Sul');


--2 - Tabela Cidade

INSERT INTO EmpresaOnibus.Cidade (nome, endereco_terminal, siglaUF) VALUES 
('Campinas', 'Terminal Barão Geraldo', 'SP'),
('São Paulo', 'Terminal Centro', 'SP'),
('Campo Grande', 'Terminal Campo Grande', 'MS');


--3 - Tabela Motorista

INSERT INTO EmpresaOnibus.Motorista (nome) VALUES 
('Carlos Silva'),
('Maria Oliveira'),
('João Pereira');


--4 - Tabela Onibus

INSERT INTO EmpresaOnibus.Onibus (capacidade, marca, modelo, idMotorista) VALUES 
(50, 'Mercedes', 'OF-1721', 1),
(42, 'Volvo', 'B270F', 2),
(36, 'Scania', 'K310', 3);


--5 - Tabela Passageiro

INSERT INTO EmpresaOnibus.Passageiro (cpf, nome, telefone, dataNascimento, email) VALUES 
('12345678901', 'Ana Souza', '11987654321', '1990-05-10', 'ana@gmail.com'),
('23456789012', 'Pedro Lima', '11998765432', '1985-08-22', 'pedro@gmail.com'),
('34567890123', 'Juliana Costa', '11991234567', '1995-03-15', 'juliana@gmail.com');


--6 - Tabela Viagem

INSERT INTO EmpresaOnibus.Viagem (distancia, custo, idCidadeOrigem, idCidadeDestino) VALUES 
(100, 80.00, 1, 2), -- Campinas -> São Paulo
(600, 150.00, 2, 3), -- São Paulo -> Campo Grande
(100, 85.00, 3, 1); -- Campo Grande -> Campinas


--7 - Tabela Passagem

INSERT INTO EmpresaOnibus.Passagem (assento, data_e_hora, idOnibus, idPassageiro,idViagem) VALUES 
(12, '2025-05-20T10:00:00', 1, 1,1),
(8, '2025-05-22T08:30:00', 2, 1,2),
(5, '2025-05-25T07:00:00', 3, 3,3);

--SE NECESSÁRIO:
/*drop table EmpresaOnibus.Passageiro
drop table EmpresaOnibus.Passagem
drop table EmpresaOnibus.UF
drop table EmpresaOnibus.Viagem
drop table EmpresaOnibus.Onibus
drop table EmpresaOnibus.Motorista
drop table EmpresaOnibus.Cidade*/

--SELECTS DO JEITO DO CHICO:
--POR QUE FEZ ISSO? Para podermos se necessário guardas
--se necessário as colunas em PYTHON e porque o Chico fez o mesmo :p

--UF
SELECT siglaUF, nomeUF FROM EmpresaOnibus.UF 
--CIDADE
SELECT nome, endereco_terminal, siglaUF FROM EmpresaOnibus.Cidade 
--MOTORISTA
SELECT nome FROM EmpresaOnibus.Motorista
--ONIBUS
SELECT capacidade, marca, modelo, idMotorista FROM EmpresaOnibus.Onibus
--PASSAGEIRO
SELECT cpf, nome, telefone, dataNascimento, email FROM EmpresaOnibus.Passageiro
--VIAGEM
SELECT distancia, custo, idCidadeOrigem, idCidadeDestino FROM EmpresaOnibus.Viagem
--PASSAGEM
SELECT assento, data_e_hora, idOnibus, idPassageiro,idViagem FROM EmpresaOnibus.Passagem
--PASSAGEIRO
SELECT cpf, nome, telefone, dataNascimento, email FROM EmpresaOnibus.Passageiro
