# Sistema Bancário Desafio DIO

Este repositório contém a implementação do desafio de criar um sistema bancário simples, proposto pela DIO. 
O objetivo do desafio é criar funcionalidades básicas de um sistema bancário como depósito, saque e visualização de extrato.

## Estrutura do Projeto

O projeto é constituído principalmente pelo arquivo `main.py`, que inclui toda a lógica para as operações bancárias mencionadas.

### `main.py`

Este arquivo contém a implementação das seguintes funcionalidades:
## Primeiro Desafio: 
- **Depósito**: Permite ao usuário adicionar fundos à sua conta bancária.
- **Saque**: Permite ao usuário retirar fundos de sua conta bancária, respeitando um limite de saque diário.
- **Extrato**: Mostra todas as transações realizadas na conta, incluindo depósitos e saques, e o saldo atual.

## Segundo Desafio: 
- **Implementação do Sistema de Conta Bancária**: Reformulada nossa estrutura de dados para usar funções para depósitos, saques e extratos, o que melhora a organização do código e facilita a manutenção.
  - Adicionamos classes para `Usuario`, `ContaBancaria` e `Transacoes`.
  - Implementamos limites de saque diários e controle sobre valores máximos de saque para aumentar a segurança das operações bancárias.

## Terceiro Desafio: 
- **Atualização baseada no modelo de classes UML**: Restruturado o código conforme modelo enviado
  - Transformamos o atributo `saldo` em um método `get_saldo()` para encapsular melhor o acesso ao saldo da conta.
  - Adicionamos verificações e validações aprimoradas para depósitos e saques, garantindo que apenas transações válidas sejam processadas.


## Como Executar

Para executar este projeto, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/Nai-nailinha/sistemaBancario
2. Navegue até a pasta do projeto:
   cd sistemaBancario
3. Execute o arquivo main.py utilizando Python:
  python main.py

## Como testar caso esteja no segundo desafio ou terceiro desafio: 
Remova as aspas triplas que tornam o trecho final um trecho comentado e realize os testes que achar necessário. 


