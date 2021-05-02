-- DISCENTE: YANKA RAÍSSA RIBEIRO DA SILVA

create database irrealalagoas;
ALTER SCHEMA `irrealalagoas`  DEFAULT CHARACTER SET utf8  DEFAULT COLLATE utf8_general_ci ;
use irrealalagoas;

create table Passageiro (
		CPF VARCHAR(14),
		Nome VARCHAR(70),
		DataNasc DATE,
		PesoBagagem DECIMAL(3,1),
        Rodoviaria ENUM('S', 'N'),
        primary key (CPF)
);

-- describe Passageiro;

create table BilheteIda (
	BilheteID INT NOT NULL AUTO_INCREMENT,
	CPF VARCHAR(14),
    CidOrigem VARCHAR(20),
	CidDestino VARCHAR(20),
	Arrival DATETIME,
    Valor DECIMAL(4,2),
    foreign key (CPF) references Passageiro(CPF),
    primary key (BilheteID)
);

-- describe BilheteIda;

create table BilheteVolta (
	BilheteID INT NOT NULL AUTO_INCREMENT,
	CPF VARCHAR(14),
	CidOrigem VARCHAR(20),
    CidDestino VARCHAR(20),
	Departure DATETIME,
    Valor DECIMAL(4,2),
    foreign key (CPF) references Passageiro(CPF),
    primary key (BilheteID)
);

-- describe BilheteVolta;

insert into Passageiro values
	('897.481.814-05', 'Paulo de Oliveira Silva', '1953-08-05', 'Maceió', 'Recife', '25.5', 'S'),
	('226.754.814-32', 'Júlio César de Araújo', '1997-10-28', 'Paulo Afonso', 'Maceio', '12.2', 'N'),
	('321.781.424-00', 'Tânia Feitosa dos Santos', '1971-02-11', 'Santana do Ipanema', 'Palmeira dos Indios', '30.0', 'N'),
	('520.175.704-87', 'Genivaldo Ferreira Costa', '1978-12-24', 'Cacimbinhas', 'Satuba', '05.7', 'N')
;

insert into BilheteIda values
	(DEFAULT, '897.481.814-05', 'Maceió', 'Recife', '2020-10-30 03:30:00', '95.00'),
    (DEFAULT, '226.754.814-32', 'Paulo Afonso', 'Maceio', '2020-11-05 05:00:00', '75.00'),
    (DEFAULT, '321.781.424-00', 'Santana do Ipanema', 'Palmeira dos Indios', '2020-11-01 11:20:00', '50.00'),
    (DEFAULT, '520.175.704-87', 'Cacimbinhas', 'Satuba', '2020-11-10 23:15:00', '50.00')
;

insert into BilheteVolta values
	(DEFAULT, '897.481.814-05', 'Recife', 'Maceió', '2020-11-03 07:30:00', '95.00'),
    (DEFAULT, '226.754.814-32', 'Maceio', 'Paulo Afonso', '2020-11-15 05:00:00', '75.00'),
    (DEFAULT, '321.781.424-00', 'Palmeira dos Indios', 'Santana do Ipanema', '2020-11-02 05:20:00', '50.00'),
    (DEFAULT, '520.175.704-87', 'Satuba', 'Cacimbinhas', '2020-11-25 15:30:00', '50.00')
;


select * from Passageiro pass
join BilheteIda bIda
on pass.CPF = bIda.CPF
order by pass.Nome;

select Nome, PesoBagagem, Rodoviaria, Valor, CidOrigem, CidDestino, Departure from Passageiro pass
join BilheteVolta bVol
on pass.CPF = bVol.CPF
order by bVol.Valor;

select * from Passageiro pass
join BilheteIda bIda
on pass.CPF = bIda.CPF
where PesoBagagem<30 and Valor>50
order by Valor DESC;

