CREATE SCHEMA EmpresaOnibus;

-- 1. Tabela UF
CREATE TABLE EmpresaOnibus.UF (
    siglaUF CHAR(2) PRIMARY KEY,
    nomeUF VARCHAR(30) NOT NULL
);

-- 2. Tabela Cidade
CREATE TABLE EmpresaOnibus.Cidade (
    idCidade INT PRIMARY KEY IDENTITY,
    nome VARCHAR(50) NOT NULL,
    endereco_terminal VARCHAR(100),
    siglaUF CHAR(2),
    CONSTRAINT FK_Cidade_UF FOREIGN KEY (siglaUF)
        REFERENCES EmpresaOnibus.UF(siglaUF)
        ON DELETE CASCADE
);

-- 3. Tabela Motorista
CREATE TABLE EmpresaOnibus.Motorista (
    idMotorista INT PRIMARY KEY IDENTITY,
    nome VARCHAR(50) NOT NULL
);

-- 4. Tabela Ônibus
CREATE TABLE EmpresaOnibus.Onibus (
    idOnibus INT PRIMARY KEY IDENTITY,
    capacidade INT NOT NULL,
    marca VARCHAR(20),
    modelo VARCHAR(20),
    placa VARCHAR(8) NOT NULL,
    CONSTRAINT chk_placa_mercosul CHECK (
        placa LIKE '[A-Z][A-Z][A-Z][0-9][A-Z][0-9][0-9]'
    )
);

-- 5. Tabela Viagem (conecta cidades, motorista e ônibus)
CREATE TABLE EmpresaOnibus.Viagem (
    idViagem INT PRIMARY KEY IDENTITY,
    distancia INT,
	dataSaida DATETIME,
    custo MONEY,
    idCidadeOrigem INT,
    idCidadeDestino INT,
    idOnibus INT,
    idMotorista INT,
    CONSTRAINT FK_Viagem_CidadeOrigem FOREIGN KEY (idCidadeOrigem)
        REFERENCES EmpresaOnibus.Cidade(idCidade),
    CONSTRAINT FK_Viagem_CidadeDestino FOREIGN KEY (idCidadeDestino)
        REFERENCES EmpresaOnibus.Cidade(idCidade),
    CONSTRAINT FK_Viagem_Onibus FOREIGN KEY (idOnibus)
        REFERENCES EmpresaOnibus.Onibus(idOnibus),
    CONSTRAINT FK_Viagem_Motorista FOREIGN KEY (idMotorista)
        REFERENCES EmpresaOnibus.Motorista(idMotorista)
);

-- 6. Tabela Passageiro
CREATE TABLE EmpresaOnibus.Passageiro (
    idPassageiro INT PRIMARY KEY IDENTITY,
    cpf CHAR(11) NOT NULL UNIQUE,
    nome VARCHAR(50) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    dataNascimento DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- 7. Tabela Passagem
CREATE TABLE EmpresaOnibus.Passagem (
    idPassagem INT PRIMARY KEY IDENTITY,
    assento INT,
    idViagem INT,
    idPassageiro INT,
    CONSTRAINT FK_Passagem_Viagem FOREIGN KEY (idViagem)
        REFERENCES EmpresaOnibus.Viagem(idViagem)
        ON DELETE CASCADE,
    CONSTRAINT FK_Passagem_Passageiro FOREIGN KEY (idPassageiro)
        REFERENCES EmpresaOnibus.Passageiro(idPassageiro)
);

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


/*
drop table EmpresaOnibus.Passagem
drop table EmpresaOnibus.Viagem
drop table EmpresaOnibus.Cidade
drop table EmpresaOnibus.UF
drop table EmpresaOnibus.Onibus
drop table EmpresaOnibus.Motorista
drop table EmpresaOnibus.Passageiro

drop schema EmpresaOnibus
*/