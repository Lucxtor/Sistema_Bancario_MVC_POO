from limite.lib_limite import valida_opcao, valida_operacao_saida, valida_operacao_entrada

class TelaOperacao:
    def tela_opcoes(self):
        self.exibe_menu()
        return valida_opcao([0,1,2,3,4,5,6])

    def exibe_menu(self):
        print("\n-------- Área de Operações ---------\n")
        print("Escolha a operação que deseja efetuar: ")
        print("1 - Saque")
        print("2 - Depósito")
        print("3 - Transferência Bancaria")
        print("4 - Transferência PIX")
        print("5 - Consultar Extrato")
        print("6 - Consultar Saldo")
        print("0 - Retornar para o menu anterior")

    def pega_dados_saque(self, saldo):
        print("Saldo disponível R$", saldo)
        valor_saque = float(input("Digite qual valor deseja sacar: "))
        return valida_operacao_saida(valor_saque, saldo)

    def pega_dados_deposito(self):
        print("Realizar depósito:")
        return valida_operacao_entrada()

    def exibe_mensagem(self, retorno):
        if retorno:
            print("Operação realizada com sucesso")
        else:
            print("Falha na operação, tente novamente mais tarde")


