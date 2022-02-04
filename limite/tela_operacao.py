from limite.lib_limite import valida_opcao, valida_operacao_saida, valida_operacao_entrada, TIPOS_OPERACOES

class TelaOperacao:
    def tela_opcoes(self, agencia_conta, codigo_conta):
        self.exibe_menu(agencia_conta, codigo_conta)
        return valida_opcao([0,1,2,3,4,5,6])

    def exibe_menu(self, agencia_conta, codigo_conta):
        print("\n-------- Área de Operações ---------\n")
        print(f'   Agência: {agencia_conta}     Conta: {codigo_conta}\n')
        print("Escolha a operação que deseja efetuar: ")
        for opcao, descricao in TIPOS_OPERACOES.items():
            print(opcao, "-", descricao)
        print("5 - Consultar Extrato")
        print("6 - Consultar Saldo")
        print("0 - Retornar para o menu anterior")

    def pega_dados_saida(self, saldo):
        print(f'Saldo disponível R$ {saldo:.2f}')
        return valida_operacao_saida(saldo)

    def pega_dados_deposito(self):
        print("Realizar depósito:")
        return valida_operacao_entrada()

    def pega_chave_PIX(self):
        return input("Informe a chave PIX para transferência: ")

    def pega_codigo_conta_destino(self):
        return int(input("Informe o código da conta destino: "))

    def exibe_saldo(self, saldo_final, saldo_depositos, saldo_saques, saldo_transferencia_enviadas, saldo_transferencia_recebidas, saldo_transferencia_entrada_vs_saida):
        print(f'\nO saldo em conta atualmente é R$ {saldo_final:.2f}\n')
        print("O saldo de movimentações é:")
        print(f'   Saques: R$ {saldo_saques:.2f}   Depósitos: R$ {saldo_depositos:.2f}\n')
        print("O saldo entre transferências é:")
        print(f'   Transferências enviadas: R$ {saldo_transferencia_enviadas:.2f}')
        print(f'   Transferências recebidas: R$ {saldo_transferencia_recebidas:.2f}\n')
        print(f'O saldo de transferências entre entradas e saídas: R$ {saldo_transferencia_entrada_vs_saida:.2f}')
        input("\nAperte enter para continuar!")

    def exibe_extrato(self, dados_operacao):
        print(f'{dados_operacao["Codigo"]}  {dados_operacao["Tipo"].ljust(21)}  {dados_operacao["Data"]}  R${dados_operacao["Valor"]} {dados_operacao["Conta_destino"]} {dados_operacao["Chave"]} ')
        input("\nAperte enter para continuar!")

    def mostra_mensagem(self, msg):
        print(msg)


