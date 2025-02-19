create database ProjetoSI;
use ProjetoSi; 
show tables;
desc cliente;
desc categorias;
desc estabelecimento;
desc itempedido;
desc pedido;
desc produtos;
desc pagamento;

create table cliente (
IdCliente int auto_increment,
nome varchar(50) not null,
email varchar(50) unique not null,
cpf varchar(20) null,
senha varchar(40) not null,
telefone varchar(20) not null,
endereco text null,
constraint pk_usuarios primary key (IdCliente)
);

create table estabelecimento (
IdEstabelecimento int auto_increment,
nome varchar(100) not null,
cnpj varchar(30) not null, 
tipo enum ('Restaurante','Mercado','Farmácia') null,
telefone varchar(20) not null,
endereco text,
descricao text,
constraint pk_estabelecimento primary key (IdEstabelecimento)
);

create table categorias (
IdCategoria int auto_increment,
nome varchar(50) not null,
constraint pk_categoria primary key (IdCategoria)
);

create table produtos (
IdProduto int auto_increment,
nome varchar(50) not null unique,
descricao text null,
preco decimal not null,
IdCategoria int not null,
IdEstabelecimento int not null,
constraint pk_produtos primary key (IdProduto),
constraint fk_produtos_categoria foreign key (IdCategoria) references categorias(IdCategoria) ,
constraint fk_produtos_estabelecimento foreign key (IdEstabelecimento) references estabelecimento(IdEstabelecimento)
);

create table pedido (
IdPedido int auto_increment,
IdCliente int not null,
IdEstabelecimento int not null,
IdCategoria int not null,
status enum ('Pendente','Preparando','Saiu para Entrega','Entregue','Cancelado') default 'pendente',
total decimal(5,2) not null,
constraint pk_pedido primary key (IdPedido),
constraint fk_pedido_cliente foreign key (IdCliente) references cliente(IdCliente),
constraint fk_pedido_categoria foreign key (IdCategoria) references categorias(IdCategoria),
constraint fk_pedido_estabelecimento foreign key (IdEstabelecimento) references estabelecimento(IdEstabelecimento)
);

create table pagamento (
IdPagamento int auto_increment,
IdPedido int not null,
metodo enum	('PIX','Cartão de Crédito'),
status enum ('Pendente','Aprovado','Recusado') default 'Pendente',
constraint pk_pagamento primary key (IdPagamento),
constraint fk_pagamento foreign key (IdPedido) references pedido(IdPedido)
);

create table ItemPedido (
IdItemPedido int auto_increment,
IdPedido int not null,
IdProduto int not null,
Quantidade int not null,
preco decimal (5,2) not null,
constraint pk_item_pedido primary key (IdItemPedido),
constraint fk_item_pedido foreign key (IdPedido) references pedido(IdPedido),
constraint fk_item_produto foreign key (IdProduto) references produtos(IdProduto)
);
