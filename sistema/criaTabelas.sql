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

-- INSERINDO DADOS NO MODELO RELACIONAL DA EMPRESA DE ÔNIBUS

-- 1. UF
INSERT INTO EmpresaOnibus.UF (siglaUF, nomeUF) VALUES 
('SP', 'São Paulo'),
('RJ', 'Rio de Janeiro'),
('MG', 'Minas Gerais'),
('MS', 'Mato Grosso do Sul');

-- 2. CIDADE
INSERT INTO EmpresaOnibus.Cidade (nome, endereco_terminal, siglaUF) VALUES 
('Campinas', 'Terminal Barão Geraldo', 'SP'),
('São Paulo', 'Terminal Centro', 'SP'),
('Campo Grande', 'Terminal Campo Grande', 'MS');

-- 3. MOTORISTA
INSERT INTO EmpresaOnibus.Motorista (nome) VALUES 
('Carlos Silva'),
('Maria Oliveira'),
('João Pereira');

-- 4. ÔNIBUS
INSERT INTO EmpresaOnibus.Onibus (capacidade, marca, modelo, placa) VALUES 
(50, 'Mercedes', 'OF-1721', 'BRA1C23'),
(42, 'Volvo', 'B270F', 'DEF2D45'),
(36, 'Scania', 'K310', 'GHI3E67');

-- 5. VIAGEM
INSERT INTO EmpresaOnibus.Viagem (distancia, custo, idCidadeOrigem, idCidadeDestino, idOnibus, idMotorista, dataSaida) VALUES 
(100, 80.00, 1, 2, 1, 1, '2025-05-20T10:00:00'),   -- Campinas -> São Paulo
(600, 150.00, 2, 3, 2, 2, '2025-05-20T10:00:00'),  -- São Paulo -> Campo Grande
(100, 85.00, 3, 1, 3, 3, '2025-05-20T10:00:00');   -- Campo Grande -> Campinas

-- 6. PASSAGEIRO
INSERT INTO EmpresaOnibus.Passageiro (cpf, nome, telefone, dataNascimento, email) VALUES 
('12345678901', 'Ana Souza', '11987654321', '1990-05-10', 'ana@gmail.com'),
('23456789012', 'Pedro Lima', '11998765432', '1985-08-22', 'pedro@gmail.com'),
('34567890123', 'Juliana Costa', '11991234567', '1995-03-15', 'juliana@gmail.com');

-- 7. PASSAGEM
INSERT INTO EmpresaOnibus.Passagem (assento, idViagem, idPassageiro) VALUES 
(12, 1, 1),
(8, 2, 1),
(5, 3, 3);


select * from EmpresaOnibus.Passageiro
select * from EmpresaOnibus.Passagem
select * from EmpresaOnibus.Viagem
select * from EmpresaOnibus.Onibus
select * from EmpresaOnibus.UF
select * from EmpresaOnibus.Cidade
select * from EmpresaOnibus.Motorista
