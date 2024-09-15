import re

# Lista para armazenar os usuários e as contas
usuarios = []
contas = []

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        if not re.match(r"^\d{11}$", cpf):
            raise ValueError("CPF deve conter apenas 11 dígitos numéricos.")
        if any(u.cpf == cpf for u in usuarios):
            raise ValueError("Já existe um usuário com este CPF.")
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(novo_usuario)
    return novo_usuario

class ContaBancaria:
    agencia = '0001'

    def __init__(self, cliente_cpf):
        self.numero = len(contas) + 1
        self.saldo = 0.0
        self.extrato = []
        self.cliente_cpf = cliente_cpf
        self.limite_saques = 3
        self.numero_saques = 0

    def depositar(self, valor, /):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f}")
            return self.saldo, self.extrato
        else:
            raise ValueError("O valor do depósito deve ser positivo.")

    def sacar(self, *, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if self.numero_saques >= self.limite_saques:
            raise ValueError("Limite de saques diários excedido.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= valor
        self.extrato.append(f"Saque: R${valor:.2f}")
        self.numero_saques += 1
        return self.saldo, self.extrato

    def imprimir_extrato(self, /, *args, **kwargs):
        return self.saldo, self.extrato

def cadastrar_conta(cpf):
    if not any(u.cpf == cpf for u in usuarios):
        raise ValueError("Não existe usuário com este CPF.")
    nova_conta = ContaBancaria(cpf)
    contas.append(nova_conta)
    return nova_conta

# Exemplo de uso:
try:
    user = cadastrar_usuario("João Silva", "01-01-1990", "12345678901", "Rua Exemplo, 100, Centro, Cidade, ST")
    conta = cadastrar_conta("12345678901")
    saldo, extrato = conta.depositar(500)
    saldo, extrato = conta.sacar(valor=250)
    print(saldo, extrato)
except ValueError as e:
    print(e)

# Teste:
"""
try:
    user = cadastrar_usuario("João Silva", "01-01-1990", "12345678901", "Rua Exemplo, 100, Centro, Cidade, ST")
    conta = cadastrar_conta("12345678901")
    saldo, extrato = conta.depositar(500)
    saldo, extrato = conta.sacar(valor=250)
    print(saldo, extrato)
except ValueError as e:
    print(e)
"""