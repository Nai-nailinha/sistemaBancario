class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.transacoes = []
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
        self.LIMITE_SACAR = 500

    def depositar(self):
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito: R$ {valor:.2f}")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self):
        if self.numero_saques >= self.LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
            return

        valor = float(input("Informe o valor do saque: "))
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif valor > self.saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > self.LIMITE_SACAR:
            print("Operação falhou! O valor do saque excede o limite.")
        else:
            self.saldo -= valor
            self.transacoes.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1

    def extrato(self):
        print("\n================ EXTRATO ================")
        if not self.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self.transacoes:
                print(transacao)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

    def mostrar_menu(self):
        menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        => """
        return input(menu)

def main():
    conta = ContaBancaria()
    while True:
        opcao = conta.mostrar_menu()

        if opcao == "d":
            conta.depositar()
        elif opcao == "s":
            conta.sacar()
        elif opcao == "e":
            conta.extrato()
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
