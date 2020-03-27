# -*- coding: utf-8 -*-
"""
Modulo especifico da estrutura das tabelas do banco de dados para sua manupulação
"""
from datetime import datetime
from sqlalchemy import BLOB, Boolean, Column, Date, DateTime, DECIMAL, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


BASE = declarative_base()


class Pais(BASE):
    """
    Classe da estrutura da tabela "país" do banco de dados
    Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
    Parâmetros:
        - __tablename__: nome da tabela no banco de dados do tipo string
        - id_pais: index do país, do tipo coluna, inteiro, chave primaria, autoincrementada e nunca nula
        - pais: nome do país, representando a coluna, do tipo texto, de tamanho 50 nunca nulo
        - sigla: sigla de identificação do país, representando a coluna e do tipo texto, de tamanho 2
    """
    __tablename__ = 'pais'
    id_pais = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    pais = Column(String(100))
    sigla = Column(String(2))

    def __init__(self, id_pais:int, pais:str, sigla=str):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Parâmetros:
            - id_country: index do país do tipo inteiro
            - country: nome do país do tipo texto
            - country_pt: nome do país em português do tipo texto
            - initials: sigla do  país do tipo texto
            - bacem: codigo da entidade financeira do tipo inteiro
        """
        self.id_pais = id_pais
        self.pais = pais
        self.sigla = sigla

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retorna apenas a valor contido em pais
        """
        return self.pais


class Estado(BASE):
    """
    Classe da estrutura da tabela "estado" do banco de dados
    Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
    Parâmetros:
        - __tablename__: nome da tabela no banco de dados do tipo texto
        - uf: sigla (index) do estado, representando a coluna, do tipo texto, de tamanho 2, chave primaria, nunca nulo
        - estado: nome do estado, representando a coluna, do tipo texto, de tamanho 100, nunca nulo
        - id_pais: index do país, representando a coluna,, do tipo inteiro, chave estrangeira
    """
    __tablename__ = 'estado'
    uf = Column(String(2), primary_key=True, nullable=False)
    estado = Column(String(75))
    id_pais = Column(Integer, ForeignKey('pais.id_pais', onupdate="RESTRICT", ondelete="RESTRICT",
                                         name='fk_id_pais_estado'))

    def __init__(self, uf: str, estado: str, id_pais: int):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
        Parâmetros:
            - uf: sigla (index) do estado do tipo texto
            - estado: nome do estado do tipo texto
            - id_pais: index do país do tipo inteiro
        """
        self.uf = uf
        self.estado = estado
        self.id_pais = id_pais

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retorna apenas a valor contido em estado
        """
        return self.estado, self.uf


class Cidade(BASE):
    """
    Classe da estrutura da tabela "cidade" do banco de dados
    Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
    Parâmetros:
        - __tablename__: nome da tabela no banco de dados do tipo texto
        - id_cidade: index da cidade, representando a coluna, do tipo inteiro, chave primaria, nunca nulo
        - cidade: nome da cidade, representando a coluna, do tipo texto, de tamanho 100, nunca nulo
        - uf: sigla (index) do estado, representando a coluna, do tipo texto, de tamanho 2 chave estrnageira, nunca nulo
        - cep: numero do cep da cidade, representando a coluna, do tipo texto, de tamanho 16
    """
    __tablename__ = 'cidade'
    id_cidade = Column(Integer, primary_key=True, nullable=False)
    cidade = Column(String(100))
    uf = Column(String(2), ForeignKey('estado.uf', onupdate="RESTRICT", ondelete="RESTRICT",
                                      name='fk_uf_cidade'))
    cep = Column(String(16))

    def __init__(self, id_cidade: int, cidade: str, uf: str, cep: str):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Parâmetros:
            - id_cidade: index da cidade do tipo inteiro
            - cidade: nome da cidade do tipo texto
            - uf: sigla (index) do estado do tipo texto
            - cep: numero do cep da cidade do tipo texto
        """
        self.id_cidade = id_cidade
        self.cidade = cidade
        self.uf = uf
        self.cep = cep

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retorna apenas o valor contido em cidade
        """
        return self.cidade, self.uf, self.cep


class Bairro(BASE):
    """
    Classe da estrutura da tabela "bairro" do banco de dados
    Herança:
        - db.Model: atributo padrão da biblioteca SqlAlchemy, responsvel por utilizar a classe que à herdou para
                    produzir schema da tabela ao qual cria um mapeador.
    Parâmetros:
        - __tablename__: nome da tabela no banco de dados do tipo texto
        - id_bairro: index do bairro, representando a coluna, do tipo inteiro, chave primaria, autoincrementada,
                            nunca nula
        - bairro: nome do bairro, representando a coluna, do tipo texto, de tamanho 100, nunca nulo
        - id_cidade: index da cidade, representando a coluna, do tipo inteiro, nunca nulo
    """
    __tablename__ = 'bairro'
    id_bairro = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    bairro = Column(String(100))
    id_cidade = Column(Integer, ForeignKey('cidade.id_cidade', onupdate="RESTRICT", ondelete="RESTRICT",
                                           name='fk_id_cidade_bairro'))
    city = relationship("City", backref="neighborhood")

    def __init__(self, id_bairro: int, bairro: str, id_cidade: int):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Parâmetros:
            - id_bairro: index do bairro, do tipo inteiro
            - bairro: nome do bairro, do tipo texto
            - id_cidade: index da cidade, do tipo inteiro
        """
        self.id_bairro = id_bairro
        self.bairro = bairro
        self.id_cidade = id_cidade

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retornar apenas os valores contidos em id_bairro, bairro, id_cidade
        """
        return self.id_bairro, self.bairro, self.id_cidade


class Logradouro(BASE):
    """
    Classe da estrutura da tabela "logradouro" do banco de dados
    Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
    Parâmetros:
        - __tablename__: nome da tabela no banco de dados do tipo texto
        - cep: número do CEP (index) da endereço, representando a coluna, do tipo texto, de tamanho 10, chave primaria, nunca nulo
        - logradouro: nome do endereço, representando a coluna, do tipo texto, de tamanho 200
        - type_logradouro: tipo de endereço, representando a coluna do tipo texto, de tamanho 80
        - complemento: descrição complementar do endereço, representando a coluna, do tipo texto, de tamanho 100
        - local: descrição do local do endereço, representando a coluna, do tipo texto, de tamnho 120
        - id_cidade: index da cidada, representando a coluna, do tipo inteiro, chave estrangeira
        - id_bairro: index do bairro, representando a coluna, do tipo inteiro, chave estrangeira
    """
    __tablename__ = 'logradouro'
    cep = Column(String(10), primary_key=True, nullable=False)
    logradouro = Column(String(200))
    tipo_logradouro = Column(String(80))
    complemento = Column(String(100))
    local = Column(String(120))
    id_cidade = Column(Integer, ForeignKey('cidade_id_cidade', onupdate="CASCADE", ondelete="RESTRICT",
                                           name='fk_id_cidade_logradouro'))
    id_bairro = Column(Integer, ForeignKey('bairro.id_bairro', onupdate="RESTRICT", ondelete="RESTRICT",
                                           name='fk_id_cidade_logradouro'))

    def __init__(self, cep: str, logradouro: str, tipo_logradouro: str,  complemento: str, local=str,
                 id_cidade=int, id_bairro=int):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Parâmetros:
            - cep: número do CEP (index) do endereço, do tipo texto
            - logradouro: nome do endereço, do tipo texto
            - type_logradouro: tipo de endereço, do tipo texto
            - complemento: descrição complementar do endereço, do tipo texto
            - local: descrição do local do endereço, do tipo texto
            - id_cidade: index da cidada, do tipo inteiro,
            - id_bairro: index do bairro, do tipo inteiro
        """
        self.cep = cep
        self.logradouro = logradouro
        self.tipo_logradouro = tipo_logradouro
        self.complemento = complemento
        self.local = local
        self.id_cidade = id_cidade
        self.id_bairro = id_bairro

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retorna apenas volores contidos em cep, logradouro, complemento, local da tabela logradouro
        """
        return self.cep, self.logradouro, self.complemento, self.local


class TipoPessoa(BASE):
    """
    Classe da estrutura da tabela "tipo_pessoa" do banco de dados
    Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
    Parâmetro:
        - __tablename__: nome da tabela no banco de dados do tipo texto
        - id_tipo_pessoa: index do tipo da pessoa, representando a coluna, do tipo inteiro, chave primaria,
                           autoincrementado, nunca nulo
        - tipo_pessoa: descrição do tipo de pessoa, representando a coluna, do tipo texto, de tamanho 30
    """
    __tablename__ = 'tipo_pessoa'
    id_tipo_pessoa = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    tipo_pessoa = Column(String(30))

    def __init__(self, id_tipo_pessoa: int, tipo_pessoa: str):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Parâmetro:
            - id_tipo_pessoa: index do tipo de pessoa, do tipo inteiro
            - tipo_pessoa: descrição do tipo de pessoa, do tipo texto
        """
        self.id_tipo_pessoa = id_tipo_pessoa
        self.tipo_pessoa = tipo_pessoa

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retorna apenas a volor contido em genre
        """
        return self.id_tipo_pessoa, self.tipo_pessoa


class Pessoa(BASE):
    """
    Classe da estrutura da tabela "pessoa" do banco de dados
    Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
    Parâmetros:
        - __tablename__: nome da tabela no banco de dados do tipo texto
        - id_pessoa: index da pessoa, representando a coluna, do tipo inteiro, chave primaria, autoincrementada,
                      nunca nulo
        - nome_razao_social: nome da pessoa ou razão social, representando a coluna, do tipo texto, de tamanho 150,
                             nunca nulo
        - sobrenome_fantasia: sobrenome da pessoa ou nome fantasia, representando a coluna, do tipo texto, de tamanho
                              150, nunca nulo
        - cpf_cnpj: número de CPF ou CNPJ da pessoa, representando a coluna, do tipo texto, de tamanho 11, unico,
                    nunca nulo
        - rg_ie: número de RG e CNPJ da pessoa, representando a coluna, do tipo texto, de tamanho 11, unico, nunca nulo
        - orgao_expeditor: sigla do orgão expeditor, representando a coluna, do tipo texto, de tamanho 5
        - uf_orgao_expeditor: sigla do estado, representando a coluna, do tipo texto, de tamanho 2
        - endereco: descrição do endereço, representando a coluna, do tipo texto, de tamanho 200, nunca nulo
        - complemento: descrição complementar, representando a coluna, do tipo texto, de tamanho 100
        - bairro: nome do bairro, representação a coluna, do tipo texto, de tamanho 100
        - cidade: nome da cidade, representando a coluna, do tipo texto, de tamanho 100
        - estado: nome do estado, representando a coluna, do tipo texto, de tamanho 50
        - cep: número do CEP, representando a coluna, representando a coluna, do tipo texto, de tamanho 10
        - telefone: número de telefone, representando a coluna, do tipo texto, de tamanho 15
        - celular: número de celular, representando a coluna, do tipo texto, de tamanho 15
        - observacao: descrição da observação, representando a coluna, do tipo texto, de tamanho 300
        - situacao: situação cadastrar, representando a coluna, do tipo boolean
        - id_usuario_criou: index do usuário, representando a coluna, do tipo inteiro, chave estrangeira
        - registrado: data e hora do registro, representando a coluna, do tipo data e hora, nunca falso
        - modificado: data e hora de modificação, representando a coluna, do tipo data e hora
    """
    __tablename__ = 'pessoa'
    id_pessoa = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    id_tipo_pessoa = Column(Integer, ForeignKey('tipo_pessoa.id_tipo_pessoa', onupdate="RESTRICT",
                                                ondelete="RESTRICT", name='fk_id_tipo_pessoa_pessoa'))
    name_razao_social = Column(String(75))
    sobrenome_nome_fantasia = Column(String(75))
    cpf_cnpj = Column(String(15), unique=True)
    rg_ie = Column(String(15), unique=True)
    organ_espedidor = Column(String(5))
    uf_organ_espedidor = Column(String(2))
    endereco = Column(String(100))
    complemento = Column(String(80))
    bairro = Column(String(70))
    cidade = Column(String(100))
    estado = Column(String(50))
    cep = Column(String(15))
    telefone = Column(String(15))
    celular = Column(String(15))
    email = Column(String(255))
    observacao = Column(Text())
    situacao = Column(Boolean)
    id_usuario_criou = Column(Integer, ForeignKey('usuario.id_usuario', onupdate="CASCADE", ondelete="RESTRICT",
                                                  name='fk_id_usuario_criou_pessoa'))
    registrado = Column(DateTime, default=datetime.utcnow)
    modificado = Column(DateTime)

    def __init__(self, id_pessoa: int, name_razao_social: str, sobrenome_nome_fantasia: str, cpf_cnpj: str,
                 rg_ie: str, organ_espedidor: str, uf_organ_espedidor: str, endereco: str, complemento: str,
                 bairro: str, cidade: str, estado: str, cep: str, telefone: str, celular: str, email: str,
                 observacao: str, situacao: bool, id_usuario_criou: int, registrado: datetime, modificado:datetime):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Parâmetro:
            - id_pessoa: index da pessoa, representando a coluna, do tipo inteiro, chave primaria, autoincrementada,
                      nunca nulo
            - nome_razao_social: nome da pessoa ou razão social, do tipo texto
            - sobrenome_fantasia: sobrenome da pessoa ou nome fantasia,  do tipo texto
            - cpf_cnpj: número de CPF ou CNPJ da pessoa,  do tipo texto, de tamanho 11
            - rg_ie: número de RG e CNPJ da pessoa, do tipo texto, de tamanho 11
            - orgao_expeditor: sigla do orgão expeditor,  do tipo texto
            - uf_orgao_expeditor: sigla do estado,  do tipo texto, de tamanho 2
            - endereco: descrição do endereço,  do tipo texto
            - complemento: descrição complementar,  do tipo texto
            - bairro: nome do bairro, do tipo texto
            - cidade: nome da cidade, do tipo texto
            - estado: nome do estado, do tipo texto
            - cep: número do CEP, representando a coluna, do tipo texto
            - telefone: número de telefone, do tipo texto
            - celular: número de celular, do tipo texto
            - observacao: descrição da observação, do tipo texto
            - situacao: situação cadastrar, do tipo boolean
            - id_usuario_criou: index do usuário, do tipo inteiro
            - registrado: data e hora do registro, do tipo data e hora
            - modificado: data e hora de modificação, do tipo data e hora
        """
        self.id_pessoa = id_pessoa
        self.name_razao_social = name_razao_social
        self.sobrenome_nome_fantasia = sobrenome_nome_fantasia
        self.cpf_cnpj = cpf_cnpj
        self.rg_ie = rg_ie
        self.organ_espedidor = organ_espedidor
        self.uf_organ_espedidor = uf_organ_espedidor
        self.endereco = endereco
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.telefone = telefone
        self.celular = celular
        self.email = email
        self.observacao = observacao
        self.situacao = situacao
        self.id_usuario_criou = id_usuario_criou
        self.registrado= registrado
        self.modificado = modificado

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retornar apenas o valor contido em name_razao_social, sobrenome_nome_fantasia, cpf_cnpj, rg_ie,
            organ_espedidor, uf_organ_espedidor, endereco, complemento, bairro, cidade, estado, cep, telefone, celular,
            email, observacao, situacao
        """
        return self.name_razao_social, self.sobrenome_nome_fantasia, self.cpf_cnpj, self.rg_ie, self.organ_espedidor, \
               self.uf_organ_espedidor, self.endereco, self.complemento, self.bairro, self.cidade, self.estado, \
               self.cep, self.telefone, self.celular, self.email, self.observacao, self.situacao


class TipoEmpresa(BASE):
    """
    Classe da estrutura da tabela "tipo_empresa" do banco de dados
    Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
    Parâmetro:
        - __tablename__: nome da tabela no banco de dados do tipo texto
        - id_tipo_empresa: index do tipo da empresa, representando a coluna, do tipo inteiro, chave primaria,
                            autoincrementado, nunca nulo
        - tipo_empresa: descrição do tipo de empresa, representando a coluna, do tipo texto, de tamanho 30
    """
    __tablename__ = 'tipo_empresa'
    id_tipo_empresa = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    tipo_empresa = Column(String(30))

    def __init__(self, id_tipo_empresa: int, tipo_empresa: str):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Parâmetro:
            - id_tipo_empresa: index do tipo de empresa, do tipo inteiro
            - tipo_empresa: descrição do tipo de empresa, do tipo texto
        """
        self.id_tipo_empresa = id_tipo_empresa
        self.tipo_empresa = tipo_empresa

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retorna apenas a volor contido em genre
        """
        return self.id_tipo_empresa, self.tipo_empresa


class Empresa(BASE):
    """
    Classe da estrutura da tabela "empresa" do banco de dados
    Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
    Parâmetro:
        - __tablename__: nome da tabela no banco de dados do tipo texto
        - id_empresa: index da empresa, representando a coluna, do tipo inteiro, chave primaria, autoincrementado,
                       nunca nulo
        - inscricao_municipal: número da inscrição estadual, representando a coluna, do tipo texto, de tamanho 15
        - logo: logo, , representando a coluna, do tipo byte
        - id_empresa_matriz: index do empresa matriz, representando a coluna, do tipo inteiro
        - id_tipo_empresa: index do tipo de empresa, representando a coluna, do tipo inteiro
    """
    __tablename__ = 'empresa'
    id_empresa = Column(Integer, ForeignKey('pessoa.id_pessoa', onupdate="CASCADE", ondelete="CASCADE",
                                            name='fk_id_pessoa_empresa'), primary_key=True, autoincrement=True,
                        nullable=False)
    inscricao_municipal = Column(String(15))
    logo = Column(BLOB)
    id_empresa_matriz = Column(Integer, ForeignKey('empresa.id_empresa', onupdate="CASCADE",
                                                   ondelete="RESTRICT", name='fk_id_empresa_empresa'))
    id_tipo_empresa = Column(Integer, ForeignKey('tipo_empresa.id_tipo_empresa', onupdate="RESTRICT",
                                                 ondelete="RESTRICT", name='fk_id_usuario_criou_empresa'))
    id_usuario_criou = Column(Integer, ForeignKey('usuario.id_usuario', onupdate="CASCADE", ondelete="RESTRICT",
                                                  name='fk_id_usuario_criou_empresa'))
    registrado = Column(DateTime, default=datetime.utcnow)
    modificado = Column(DateTime)

    def __init__(self, id_empresa: int, inscricao_municipal: str, logo: bytes, id_empresa_matriz: int,
                 id_tipo_empresa: int, id_usuario_criou: int, regstrado: datetime, modificado: datetime):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Parâmetro:
            - id_empresa: index da empresa, representando a coluna, do tipo inteiro, chave primaria, autoincrementado,
                       nunca nulo
            - inscricao_municipal: número da inscrição estadual, do tipo texto
            - logo: logo, do tipo byte
            - id_empresa_matriz: index do empresa matriz, do tipo inteiro
            - id_tipo_empresa: index do tipo de empresa, do tipo inteiro
            - id_usuario_criou: index do usuário, representando a coluna, do tipo inteiro, chave estrangeira
            - registrado: data e hora do registro, representando a coluna, do tipo data e hora, nunca falso
            - modificado: data e hora de modificação, representando a coluna, do tipo data e hora
        """
        self.id_empresa = id_empresa
        self.inscricao_municipal = inscricao_municipal
        self.logo = logo
        self.id_empresa_matriz = id_empresa_matriz
        self.id_tipo_empresa = id_tipo_empresa
        self.id_usuario_criou = id_usuario_criou
        self.registrado = regstrado
        self.modificado = modificado

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retorna apenas a volor contido em inscricao_municipal, logo, id_empresa_matriz, id_tipo_empresa
        """
        return self.inscricao_municipal, self.logo, self.id_empresa_matriz, self.id_tipo_empresa


class Cliente(BASE):
    """
    Classe da estrutura da tabela "cliente" do banco de dados
    Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
    Parâmetro:
        - __tablename__: nome da tabela no banco de dados do tipo texto
        - id_cliente: index da cliente, representando a coluna, do tipo inteiro, chave primaria, autoincrementado,
                       nunca nulo
        - inscricao_municipal: número da inscrição estadual, representando a coluna, do tipo texto, de tamanho 15
        - id_usuario_criou: index do usuário, representando a coluna, do tipo inteiro, chave estrangeira
        - registrado: data e hora do registro, representando a coluna, do tipo data e hora, nunca falso
        - modificado: data e hora de modificação, representando a coluna, do tipo data e hora
    """
    __tablename__ = 'cliente'
    id_cliente = Column(Integer, ForeignKey('pessoa.id_pessoa', onupdate="CASCADE", ondelete="CASCADE",
                                            name='fk_id_pessoa_cliente'), primary_key=True, autoincrement=True,
                        nullable=False)
    inscricao_municipal = Column(String(15))
    id_usuario_criou = Column(Integer, ForeignKey('usuario.id_usuario', onupdate="CASCADE", ondelete="RESTRICT",
                                                  name='fk_id_usuario_criou_cliente'))
    registrado = Column(DateTime)
    modificado = Column(DateTime)

    def __init__(self, id_cliente: int, inscricao_municipal: str, id_usuario_criou: int,
                 registrado: datetime, modificado: datetime):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Parâmetro:
            - id_empresa: index da empresa, representando a coluna, do tipo inteiro, chave primaria, autoincrementado,
                       nunca nulo
            - inscricao_municipal: número da inscrição estadual, do tipo texto
            - logo: logo, do tipo byte
            - id_empresa_matriz: index do empresa matriz, do tipo inteiro
            - id_tipo_empresa: index do tipo de empresa, do tipo inteiro
        """
        self.id_cliente = id_cliente
        self.inscricao_municipal = inscricao_municipal
        self.id_usuario_criou = id_usuario_criou
        self.registrado = registrado
        self.modificado = modificado

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retorna apenas a volor contido em genre
        """
        return self.inscricao_municipal


class Transportadora(BASE):
    """
    Classe da estrutura da tabela "transportadora" do banco de dados
    Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
    Parâmetro:
        - __tablename__: nome da tabela no banco de dados do tipo texto
        - id_transportadora: index da transportadora, representando a coluna, do tipo inteiro, chave primaria,
                             autoincrementado, nunca nulo
        - inscricao_municipal: número da inscrição estadual, representando a coluna, do tipo texto, de tamanho 15
        - id_usuario_criou: index do usuário, representando a coluna, do tipo inteiro, chave estrangeira
        - registrado: data e hora do registro, representando a coluna, do tipo data e hora, nunca falso
        - modificado: data e hora de modificação, representando a coluna, do tipo data e hora
    """
    __tablename__ = 'transportadora'
    id_transportadora = Column(Integer, ForeignKey('pessoa.id_pessoa', onupdate="CASCADE", ondelete="CASCADE",
                                            name='fk_id_pessoa_transportadora'), primary_key=True, autoincrement=True,
                        nullable=False)
    inscricao_municipal = Column(String(15))
    id_usuario_criou = Column(Integer, ForeignKey('usuario.id_usuario', onupdate="CASCADE", ondelete="RESTRICT",
                                                  name='fk_id_usuario_criou_transportadora'))
    registrado = Column(DateTime, default=datetime.utcnow)
    modificado = Column(DateTime)

    def __init__(self, id_transportadora: int, inscricao_municipal: str, id_usuario_criou: int,
                 registrado: datetime, modificado: datetime):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Parâmetro:
            - id_empresa: index da empresa, representando a coluna, do tipo inteiro, chave primaria, autoincrementado,
                       nunca nulo
            - inscricao_municipal: número da inscrição estadual, do tipo texto
            - logo: logo, do tipo byte
            - id_empresa_matriz: index do empresa matriz, do tipo inteiro
            - id_tipo_empresa: index do tipo de empresa, do tipo inteiro
        """
        self.id_transportadora = id_transportadora
        self.inscricao_municipal = inscricao_municipal
        self.id_usuario_criou = id_usuario_criou
        self.registrado = registrado
        self.modificado = modificado

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retorna apenas a volor contido em genre
        """
        return self.inscricao_municipal


class Veiculo(BASE):
    """
    Classe da estrutura da tabela "veiculo" do banco de dados
    Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
    Parâmetro:
        - __tablename__: nome da tabela no banco de dados do tipo texto
        - id_veiculo: index da veiculo, representando a coluna, do tipo inteiro, chave primaria,
                       autoincrementado, nunca nulo
        - id_transportadora: index da transportadora, representando a coluna, do tipo inteiro, chave estrangeira
        - nome_motorista: nome do motorista, representando a coluna, do tipo texto, de tamanho 75
        - marca: marca do veiculo, representando a coluna, do tipo texto, de tamanho 70
        - modelo: modelo do veiculo, representando a coluna, do tipo texto, de tamanho 70
        - placa: placa do veiculo,  representando a coluna, do tipo texto, de tamanho 7
        - uf_placa: estado da placa do veiculo,  representando a coluna, do tipo texto, de tamanho 2
        - antt: número da ANTT,  representando a coluna, do tipo texto, de tamanho 11
        - placa_reboque_primeiro: placa do veiculo,  representando a coluna, do tipo texto, de tamanho 7
        - uf_placa_reboque_primeiro: estado da placa do veiculo,  representando a coluna, do tipo texto, de tamanho 2
        - antt_reboque_primeiro: número da ANTT,  representando a coluna, do tipo texto, de tamanho 11
        - placa_reboque_segundo: placa do veiculo,  representando a coluna, do tipo texto, de tamanho 7
        - uf_placa_reboque_segundo: estado da placa do veiculo,  representando a coluna, do tipo texto, de tamanho 2
        - antt_reboque_segundo: número da ANTT,  representando a coluna, do tipo texto, de tamanho 11
        - placa_reboque_terceiro: placa do veiculo,  representando a coluna, do tipo texto, de tamanho 7
        - uf_placa_reboque_terceiro: estado da placa do veiculo,  representando a coluna, do tipo texto, de tamanho 2
        - antt_reboque_terceiro: número da ANTT, representando a coluna, do tipo texto, de tamanho 11
        - ano_fabricacao = ano de fabricação, representando a coluna, do tipo texto, de tamanho 4
        - ano_modelo = ano do modelo, representando a coluna, do tipo texto, de tamanho 4
        - peso_tara = valor do peso tara, representando a coluna, do tipo numerico
        - peso_bruto = valor do peso bruto, representando a coluna, do tipo numerico
        - id_usuario_criou: index do usuário, representando a coluna, do tipo inteiro, chave estrangeira
        - registrado: data e hora do registro, representando a coluna, do tipo data e hora, nunca falso
        - modificado: data e hora de modificação, representando a coluna, do tipo data e hora
    """
    __tablename__ = 'veiculo'
    id_veiculo = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    id_transportadora = Column(Integer, ForeignKey('transportadora.id_transportadora', onupdate="CASCADE",
                                                   ondelete="RESTRICT", name='fk_id_transportadora_veiculo'))
    nome_motorista = Column(String(75))
    marca = Column(String(70))
    modelo = Column(String(70))
    placa = Column(String(7))
    uf_placa = Column(String(2))
    antt = Column(String(11))
    placa_reboque_primeiro = Column(String(7))
    uf_placa_reboque_primeiro = Column(String(2))
    antt_reboque_primeiro = Column(String(11))
    placa_reboque_segundo = Column(String(7))
    uf_placa_reboque_segundo = Column(String(2))
    antt_reboque_segundo = Column(String(11))
    placa_reboque_terceiro = Column(String(7))
    uf_placa_reboque_terceiro = Column(String(2))
    antt_reboque_terceiro = Column(String(11))
    ano_fabricacao = Column(String(4))
    ano_modelo = Column(String(4))
    peso_tara = Column(Numeric)
    peso_bruto = Column(Numeric)
    id_usuario_criou = Column(Integer, ForeignKey('usuario.id_usuario', onupdate="CASCADE", ondelete="RESTRICT",
                                                  name='fk_id_usuario_criou_veiculo'))
    registrado = Column(DateTime, default=datetime.utcnow)
    modificado = Column(DateTime)

    def __init__(self, id_veiculo: int, id_transportadora: int, nome_motorista: str, marca: str, modelo: str,
                 placa: str, uf_placa: str, antt: str, placa_reboque_primeiro: str, uf_placa_reboque_primeiro: str,
                 antt_reboque_primeiro: str, placa_reboque_segundo: str, uf_placa_reboque_segundo: str,
                 antt_reboque_segundo: str, placa_reboque_terceiro: str, uf_placa_reboque_terceiro: str,
                 antt_reboque_terceiro: str, ano_fabricacao: str, ano_modelo: str, peso_tara: int,  peso_bruto: int,
                 id_usuario_criou: int, registrado: datetime, modificado: datetime):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Parâmetro:
            - id_veiculo: index da veiculo, representando a coluna, do tipo inteiro, chave primaria,
                       autoincrementado, nunca nulo
        - id_transportadora: index da transportadora, do tipo inteiro,
        - nome_motorista: nome do motorista, do tipo texto
        - marca: marca do veiculo, do tipo texto
        - modelo: modelo do veiculo, do tipo texto
        - placa: placa do veiculo, do tipo texto
        - uf_placa: estado da placa do veiculo,  do tipo texto
        - antt: número da ANTT, do tipo texto
        - placa_reboque_primeiro: placa do veiculo, do tipo texto
        - uf_placa_reboque_primeiro: estado da placa do veiculo,  do tipo texto
        - antt_reboque_primeiro: número da ANTT
        - placa_reboque_segundo: placa do veiculo
        - uf_placa_reboque_segundo: estado da placa do veiculo, do tipo texto
        - antt_reboque_segundo: número da ANTT, do tipo texto
        - placa_reboque_terceiro: placa do veiculo, do tipo text
        - uf_placa_reboque_terceiro: estado da placa do veiculo, do tipo texto
        - antt_reboque_terceiro: número da ANTT, do tipo texto
        - ano_fabricacao = ano de fabricação, do tipo texto
        - ano_modelo = ano do modelo, do tipo texto
        - peso_tara = valor do peso tara, do tipo numerico
        - peso_bruto = valor do peso bruto, do tipo numerico
        - id_usuario_criou: index do usuário, do tipo inteiro
        - registrado: data e hora do registro, do tipo data e hora
        - modificado: data e hora de modificação, do tipo data e hora
        """
        self.id_veiculo = id_veiculo
        self.id_transportadora = id_transportadora
        self.nome_motorista = nome_motorista
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.uf_placa = uf_placa
        self.antt = antt
        self.placa_reboque_primeiro = placa_reboque_primeiro
        self.uf_placa_reboque_primeiro = uf_placa_reboque_primeiro
        self.antt_reboque_primeiro = antt_reboque_primeiro
        self.placa_reboque_segundo = placa_reboque_segundo
        self.uf_placa_reboque_segundo = uf_placa_reboque_segundo
        self.antt_reboque_segundo = antt_reboque_segundo
        self.placa_reboque_terceiro = placa_reboque_terceiro
        self.uf_placa_reboque_terceiro = uf_placa_reboque_terceiro
        self.antt_reboque_terceiro = antt_reboque_terceiro
        self.ano_fabricacao = ano_fabricacao
        self.ano_modelo = ano_modelo
        self.peso_tara = peso_tara
        self.peso_bruto = peso_bruto
        self.id_usuario_criou = id_usuario_criou
        self.registrado = registrado
        self.modificado = modificado

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retorna apenas a volor contido em id_veiculo, nome_motorista, marca, modelo, placa, uf_placa
        """
        return self.id_veiculo, self.nome_motorista, self.marca, self.modelo, self.placa, self.uf_placa


class Usuario(BASE):
    """
    Classe da estrutura da tabela "usuario" do banco de dados
    Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
    Parâmetro:
        - __tablename__: nome da tabela no banco de dados do tipo texto
        - id_usuario: index da usuario, representando a coluna, do tipo inteiro, chave primaria,
                       autoincrementado, nunca nulo
        - login: nome de login, representando a coluna, do tipo texto, de tamanho 20
        - senha: senha do usuario, representando a coluna, do tipo texto, de tamnaho 255
        - expira: data de expiração, representando a coluna, do tipo texto, do tipo data
        - id_usuario_criou: index do usuário, representando a coluna, do tipo inteiro, chave estrangeira
        - registrado: data e hora do registro, representando a coluna, do tipo data e hora, nunca falso
        - modificado: data e hora de modificação, representando a coluna, do tipo data e hora
    """
    __tablename__ = 'usuario'
    id_usuario = Column(Integer,  primary_key=True, autoincrement=True, nullable=False)
    login = Column(String(20))
    senha = Column(String(255))
    expira = Column(DateTime)
    id_usuario_criou = Column(Integer, ForeignKey('usuario.id_usuario', onupdate="CASCADE", ondelete="RESTRICT",
                                                  name='fk_id_usuario_criou_usuario'))
    registrado = Column(DateTime, default=datetime.utcnow)
    modificado = Column(DateTime)

    def __init__(self, id_usuario: int, login: str, senha: str, expira: datetime, id_usuario_criou: int,
                 registrado: datetime, modificado: datetime):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Parâmetro:
            - id_usuario: index da usuario, representando a coluna, do tipo inteiro, chave primaria,
                           autoincrementado, nunca nulo
            - login: nome de login, do tipo texto
            - senha: senha do usuario, do tipo texto
            - expira: data de expiração, do tipo texto, do tipo data
            - id_usuario_criou: index do usuário, do tipo inteiro
            - registrado: data e hora do registro, do tipo data e hora
            - modificado: data e hora de modificação,  do tipo data e hora
        """
        self.id_usuario = id_usuario
        self.login = login
        self.senha = senha
        self.expira = expira
        self.id_usuario_criou = id_usuario_criou
        self.registrado = registrado
        self.modificado = modificado

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retorna apenas a volor contido em genre
        """
        return self.login, self.senha, self.expira


class UsuarioPermissao(BASE):
    """
    Classe da estrutura da tabela "usuario_permissao" do banco de dados
    Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
    Parâmetro:
        - __tablename__: nome da tabela no banco de dados do tipo texto
        - id_usuario_permissao: index da permissão de usuario, representando a coluna, do tipo inteiro, chave primaria,
                       autoincrementado, nunca nulo
        - id_usuario: index de usuario, representando a coluna, do tipo inteiro, chave estrangeira
        - acesso: permissão para acessar, representando a coluna, do tipo boolean
        - registra: permissão para registrar, representando a coluna, do tipo boolean
        - editar: permissão para registrar, representando a coluna, do tipo boolean
        - delete: permissão para delertar, representando a coluna, do tipo boolean
        - pesquisar: permissão para pesquisar, representando a coluna, do tipo boolean
        - visualisar: permissão para visualisar, representando a coluna, do tipo boolean
        - id_usuario_criou: index do usuário, representando a coluna, do tipo inteiro, chave estrangeira
        - registrado: data e hora do registro, representando a coluna, do tipo data e hora, nunca falso
        - modificado: data e hora de modificação, representando a coluna, do tipo data e hora
    """
    __tablename__ = 'usuario_permissao'
    id_usuario_permissao = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    id_usuario = Column(Integer)
    acesso = Column(Boolean)
    registra = Column(Boolean)
    editar = Column(Boolean)
    delete = Column(Boolean)
    pesquisar = Column(Boolean)
    visualisar = Column(Boolean)
    id_usuario_criou = Column(Integer, ForeignKey('usuario.id_usuario', onupdate="CASCADE", ondelete="RESTRICT",
                                                  name='fk_id_usuario_criou_usuario'))
    registrado = Column(DateTime, default=datetime.utcnow)
    modificado = Column(DateTime)

    def __init__(self, id_usuario_permissao: int, id_usuario: int, acesso: bool, registra: bool, editar: bool,
                 deletar: bool, pesquisar: bool, visualisar: bool, id_usuario_criou: int, registrado: datetime,
                 modificado: datetime):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Parâmetro:
            - id_usuario_permissao: index da permissão de usuario, do tipo inteiro
            - id_usuario: index de usuario, do tipo inteiro, chave estrangeira
            - acesso: permissão para acessar, do tipo boolean
            - registra: permissão para registrar, do tipo boolean
            - editar: permissão para registrar, do tipo boolean
            - delete: permissão para delertar, do tipo boolean
            - pesquisar: permissão para pesquisar, do tipo boolean
            - visualisar: permissão para visualisar, do tipo boolean
            - id_usuario_criou: index do usuário, do tipo inteiro
            - registrado: data e hora do registro, do tipo data e hora
            - modificado: data e hora de modificação, do tipo data e hora
        """
        self.id_usuario_permissao = id_usuario_permissao
        self.id_usuario = id_usuario
        self.acesso = acesso
        self.registra = registra
        self.edita = editar
        self.deleta = deletar
        self.pesquisa = pesquisar
        self.visualisa = visualisar
        self.id_usuario_criou = id_usuario_criou
        self.registrado = registrado
        self.modificado = modificado

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retorna apenas a volor contido em genre
        """
        return self.id_usuario_permissao, self.id_usuario, self.acesso, self.registra, self.editar, self.deletar, \
               self.pesquisar, self.visualisar


class TituloPagamento(BASE):
    """
    Classe da estrutura da tabela "titulo_pagamento" do banco de dados
    Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
    Parâmetro:
        - __tablename__: nome da tabela no banco de dados do tipo texto
        - id_titulo_pagamento: index do titulo de pagemento de usuario, representando a coluna, do tipo inteiro, chave
                                primaria, autoincrementado, nunca nulo
        - id_cliente: index de cliente, representando a coluna, do tipo inteiro, chave estrangeira
        - id_balanca: index de balança, representando a coluna, do tipo inteiro, chave estrangeira
        - vencimento: data de vemcimento, representando a coluna, do tipo data
        - valor: valor da fatura, representando a coluna, do tipo decimal
        - observacao: descrição da observação, representando a coluna, do tipo texto
        - id_usuario_criou: index do usuário, representando a coluna, do tipo inteiro, chave estrangeira
        - registrado: data e hora do registro, representando a coluna, do tipo data e hora, nunca falso
        - modificado: data e hora de modificação, representando a coluna, do tipo data e hora
    """
    __tablename__ = 'titulo_pagamento'
    id_titulo_pagamento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    id_cliente = Column(Integer, ForeignKey('cliente.id_cliente', onupdate="CASCADE", ondelete="RESTRICT",
                                                  name='fk_id_cliente_titulo_pagamento'))
    id_balanca = Column(Integer, ForeignKey('balanca.id_balanca', onupdate="CASCADE", ondelete="RESTRICT",
                                                  name='fk_id_balanca_titulo_balanca'))
    vencimento = Column(Date)
    valor = Column(DECIMAL(10,2))
    observacao = Column(Text)
    id_usuario_criou = Column(Integer, ForeignKey('usuario.id_usuario', onupdate="CASCADE", ondelete="RESTRICT",
                                                  name='fk_id_usuario_criou_titulo_pagamento'))
    registrado = Column(DateTime, default=datetime.utcnow)
    modificado = Column(DateTime)

    def __init__(self, id_titulo_pagamento: int, id_cliente: int, id_balanca: int, vencimento: datetime, valor: float,
                 observacao: str, id_usuario_criou: int, registrado: datetime, modificado: datetime):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Parâmetro:
            - id_titulo_pagamento: index do titulo de pagemento de usuario, do tipo inteiro
            - id_cliente: index de cliente, do tipo inteiro
            - id_balanca: index de balança, do tipo inteiro
            - vencimento: data de vemcimento, do tipo data
            - valor: valor da fatura, do tipo decimal
            - observacao: descrição da observação, do tipo texto
            - id_usuario_criou: index do usuário, do tipo inteiro
            - registrado: data e hora do registro, do tipo data e hora
            - modificado: data e hora de modificação, do tipo data e hora
        """
        self.id_titulo_pagamento = id_titulo_pagamento
        self.id_cliente = id_cliente
        self.id_balanca = id_balanca
        self.vencimento = vencimento
        self.valor = valor
        self.observacao = observacao
        self.id_usuario_criou = id_usuario_criou
        self.registrado = registrado
        self.modificado = modificado

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retorna apenas a volor contido em genre
        """
        return self.id_titulo_pagamento, self.id_cliente, self.id_balanca, self.vencimento, self.valor, self.observacao


class MovimentoPagamento(BASE):
    """
    Classe da estrutura da tabela "movimento_titulo" do banco de dados
    Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
    Parâmetro:
        - __tablename__: nome da tabela no banco de dados do tipo texto
        - id_movimento_titulo: index do tipo de movimento do titulo, representando a coluna, do tipo inteiro, chave
                                primaria, autoincrementado, nunca nulo
        - movimento_titulo: descrição do tipo de movimento do titulo, representando a coluna, do tipo texto, de
                            tamanho 50
    """
    __tablename__ = 'movimento_titulo'
    id_movimento_titulo = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    movimento_titulo = Column(String(50))

    def __init__(self, id_movimento_titulo: int, movimento_titulo: str):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Parâmetro:
            - id_movimento_titulo: index do tipo de movimento do titulo, do tipo inteiro
            - movimento_titulo: descrição do tipo de movimento do titulo, do tipo texto
        """
        self.id_movimento_titulo = id_movimento_titulo
        self.movimento_titulo = movimento_titulo

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retorna apenas a volor contido em genre
        """
        return self.id_movimento_titulo, self.movimento_titulo


class Especie(BASE):
    """
    Classe da estrutura da tabela "especie" do banco de dados
    Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
    Parâmetro:
        - __tablename__: nome da tabela no banco de dados do tipo texto
        - id_especie: index do especie do recemimento, representando a coluna, do tipo inteiro, chave
                                primaria, autoincrementado, nunca nulo
        - especie: descrição do especie do recemimento, representando a coluna, do tipo texto, de tamanho 50
    """
    __tablename__ = 'especie'
    id_especie = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    especie = Column(String(50))

    def __init__(self, id_especie: int, especie: str):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Parâmetro:
            - id_especie: index do especie do recemimento, do tipo inteiro
            - especie: descrição do especie do recemimento, do tipo texto
        """
        self.id_especie = id_especie
        self.especie = especie

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retorna apenas a volor contido em id_especie, especie
        """
        return self.id_especie, self.especie


class Caixa(BASE):
    """
    Classe da estrutura da tabela "caixa" do banco de dados
    Herança:
        - BASE: atributo da chamada da funcção declarative_base() padrão da biblioteca SqlAlchemy, responsvel por
                utilizar a classe a herdou para produzir schema da tabela ao qual cria um mapeador.
    Parâmetro:
        - __tablename__: nome da tabela no banco de dados do tipo texto
        - id_caixa: index do caixa, representando a coluna, do tipo inteiro, chave primaria, autoincrementado,
                     nunca nulo
        - id_movimento_titulo: index de movimento titulo, representando a coluna, do tipo inteiro, chave estrangeira
        - id_especie: index de tipo da especie, representando a coluna, do tipo inteiro, chave estrangeira
        - id_titulo_pagamento: index de titulo de pagamento, representando a coluna, do tipo inteiro, chave estrangeira
        - valor: valor do movimento caixa, representando a coluna, do tipo decimal
        - data: data do movimento caixa, representando a coluna, do tipo data
        - observacao: descricao da observação, representando a coluna, do tipo texto
        - id_usuario_criou: index do usuário, representando a coluna, do tipo inteiro, chave estrangeira
        - registrado: data e hora do registro, representando a coluna, do tipo data e hora, nunca falso
        - modificado: data e hora de modificação, representando a coluna, do tipo data e hora
    """
    __tablename__ = 'caixa'
    id_caixa = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    id_movimento_titulo = Column(Integer, ForeignKey('movimento_titulo.id_movimento_titulo', onupdate="CASCADE",
                                                     ondelete="RESTRICT", name='fk_id_movimento_titulo_caixa'))
    id_especie = Column(Integer, ForeignKey('especie.id_especie', onupdate="CASCADE", ondelete="RESTRICT",
                                            name='fk_id_especie_caixa'))
    id_titulo_recebimento = Column(Integer, ForeignKey('titulo_recebimento.id_titulo_recebimento', onupdate="CASCADE",
                                                       ondelete="RESTRICT", name='fk_id_titulo_recebimento_caixa'))
    valor = Column(DECIMAL(10,2))
    data = Column(Date)
    observacao = Column(Text)
    id_usuario_criou = Column(Integer, ForeignKey('usuario.id_usuario', onupdate="CASCADE", ondelete="RESTRICT",
                                                  name='fk_id_usuario_criou_caixa'))
    registrado = Column(DateTime, default=datetime.utcnow)
    modificado = Column(DateTime)

    def __init__(self, id_caixa: int, id_movimento_titulo: int, id_especie: int, id_titulo_recebimento: int,
                 valor: float, data: datetime, observacao: str, id_usuario_criou: int, registrado: datetime,
                 modificado: datetime):
        """
        Inicializador da classe ao qual irá inserir as informações nos atributos
        Parâmetro:
            - id_caixa: index do caixa, do tipo inteiro, chave primaria
            - id_movimento_titulo: index de movimento titulo, do tipo inteiro
            - id_especie: index de tipo da especie, do tipo inteiro
            - id_titulo_pagamento: index de titulo de pagamento, do tipo inteiro
            - valor: valor do movimento caixa, do tipo decimal
            - data: data do movimento caixa, do tipo data
            - observacao: descricao da observação, do tipo texto
            - id_usuario_criou: index do usuário, do tipo inteiro
            - registrado: data e hora do registro, do tipo data e hora
            - modificado: data e hora de modificação, do tipo data e hora
        """
        self.id_caixa = id_caixa
        self.id_movimento_titulo = id_movimento_titulo
        self.id_especie = id_especie
        self.id_titulo_recebimento = id_titulo_recebimento
        self.valor = valor
        self.data = data
        self.observacao = observacao
        self.id_usuario_criou = id_usuario_criou
        self.registrado = registrado
        self.modificado = modificado

    def __repr__(self):
        """
        Função de representação
        Retorno:
            Retorna apenas a volor contido em id_caixa, id_movimento_titulo, id_especie, id_titulo_recebimento, valor,
            data, observacao
        """
        return self.id_caixa, self.id_movimento_titulo, self.id_especie, self.id_titulo_recebimento, self.valor, \
               self.data, self.observacao