CREATE TABLE IF NOT EXISTS cliente (
    id_cliente SERIAL PRIMARY KEY,
    nome_cliente VARCHAR(120) NOT NULL,
    cpf_cnpj VARCHAR(14) NOT NULL UNIQUE,
    telefone VARCHAR(20) NOT NULL,
    status_cliente VARCHAR(20) NOT NULL,
    CONSTRAINT ck_cliente_cpf_cnpj
        CHECK (cpf_cnpj ~ '^([0-9]{11}|[0-9]{14})$'),
    CONSTRAINT ck_cliente_status_cliente
        CHECK (status_cliente IN ('ATIVO', 'INATIVO', 'INADIMPLENTE'))
);

CREATE TABLE IF NOT EXISTS planos (
    id_planos SERIAL PRIMARY KEY,
    descricao_planos VARCHAR(120) NOT NULL,
    velocidade_franquia VARCHAR(60) NOT NULL,
    valor_mensal NUMERIC(10, 2) NOT NULL,
    CONSTRAINT ck_planos_valor_mensal
        CHECK (valor_mensal > 0)
);

CREATE TABLE IF NOT EXISTS contrato (
    id_contrato SERIAL PRIMARY KEY,
    idcliente INTEGER NOT NULL,
    idplanos INTEGER NOT NULL,
    data_base DATE NOT NULL,
    end_instalacao VARCHAR(180) NOT NULL,
    tempo_contrato INTEGER NOT NULL,
    CONSTRAINT ck_contrato_tempo_contrato
        CHECK (tempo_contrato > 0),
    CONSTRAINT fk_contrato_cliente
        FOREIGN KEY (idcliente) REFERENCES cliente(id_cliente),
    CONSTRAINT fk_contrato_planos
        FOREIGN KEY (idplanos) REFERENCES planos(id_planos)
);

CREATE TABLE IF NOT EXISTS fatura (
    id_fatura SERIAL PRIMARY KEY,
    idcontrato INTEGER NOT NULL,
    valor_fatura NUMERIC(10, 2) NOT NULL,
    data_emissao DATE NOT NULL,
    data_vencimento DATE NOT NULL,
    CONSTRAINT ck_fatura_valor_fatura
        CHECK (valor_fatura > 0),
    CONSTRAINT fk_fatura_contrato
        FOREIGN KEY (idcontrato) REFERENCES contrato(id_contrato)
);

CREATE TABLE IF NOT EXISTS os (
    id_os SERIAL PRIMARY KEY,
    idcontrato INTEGER NOT NULL,
    data_abertura DATE NOT NULL,
    data_resolucao DATE,
    status VARCHAR(20) NOT NULL,
    desc_os TEXT NOT NULL,
    tipo_os VARCHAR(60) NOT NULL,
    CONSTRAINT fk_os_contrato
        FOREIGN KEY (idcontrato) REFERENCES contrato(id_contrato)
);

CREATE TABLE IF NOT EXISTS funcionario (
    id_func SERIAL PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    cargo VARCHAR(80) NOT NULL
);

CREATE TABLE IF NOT EXISTS atende (
    id_func INTEGER NOT NULL,
    id_os INTEGER NOT NULL,
    PRIMARY KEY (id_func, id_os),
    CONSTRAINT fk_atende_funcionario
        FOREIGN KEY (id_func) REFERENCES funcionario(id_func),
    CONSTRAINT fk_atende_os
        FOREIGN KEY (id_os) REFERENCES os(id_os)
);
