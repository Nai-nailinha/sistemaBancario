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
        self.contas = []  # Lista para armazenar as contas do usuário

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class ContaBancaria:
    agencia = '0001'

    def __init__(self, cliente):
        self.numero = len(contas) + 1
        self._saldo = 0.0
        self.cliente = cliente
        self.extrato = []
        self.limite_saques = 3  # Limite de número de saques por dia
        self.limite_valor_saque = 500.0  # Limite do valor do saque
        self.numero_saques = 0
        cliente.adicionar_conta(self)  # Associar conta ao cliente

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f}")
            return self._saldo
        else:
            raise ValueError("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.limite_valor_saque:
            raise ValueError(f"Valor de saque excede o limite de R${self.limite_valor_saque:.2f}.")
        if self.numero_saques >= self.limite_saques:
            raise ValueError("Limite de saques diários excedido.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= valor
        self.extrato.append(f"Saque: R${valor:.2f}")
        self.numero_saques += 1
        return self._saldo

def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(novo_usuario)
    return novo_usuario

def cadastrar_conta(usuario):
    nova_conta = ContaBancaria(usuario)
    contas.append(nova_conta)
    return nova_conta

# Exemplo de uso:
"""
try:
    user = cadastrar_usuario("João Silva", "01-01-1990", "12345678901", "Rua Exemplo, 100, Centro, Cidade, ST")
    conta = cadastrar_conta(user)
    conta.depositar(1000)
    conta.sacar(400)
    print(f"Saldo atual: {conta.saldo}")
    print("Extrato:", conta.extrato)
    conta.sacar(50)
    print(f"Saldo atual: {conta.saldo}")
    print("Extrato:", conta.extrato)
    conta.sacar(30)
    print(f"Saldo atual: {conta.saldo}")
    print("Extrato:", conta.extrato)
    conta.sacar(60)
    print(f"Saldo atual: {conta.saldo}")
    print("Extrato:", conta.extrato)
except ValueError as e:
    print(e)
"""
