from limite.lib_limite import valida_opcao, valida_operacao_saida, valida_operacao_entrada, TIPOS_OPERACOES
import PySimpleGUI as sg

class TelaOperacao:
    def close(self):
        self.__window.Close()

    def exibe_menu_operacoes(self, agencia_conta, codigo_conta):
        self.menu_operacoes(agencia_conta, codigo_conta)
        botao, valores = self.__window.Read()
        return botao


    def menu_operacoes(self, agencia_conta, codigo_conta):
        layout = [
            [sg.Text('Área de Operações')],
            [sg.Text(f'   Agência: {agencia_conta}     Conta: {codigo_conta}')],
            [sg.Text('Escolha a operação que deseja efetuar')],
            [sg.Submit('Saque', key=1)],
            [sg.Submit('Depósito', key=2)],
            [sg.Submit('Transferência Ted/Doc', key=3)],
            [sg.Submit('Transferência PIX', key=4)],
            [sg.Submit('Consultar Extrato', key=5)],
            [sg.Submit('Consultar Saldo', key=6)],
            [sg.Cancel('Finalizar Sistema', key=0)],
        ]
        self.__window = sg.Window('Área de Operações').Layout(layout)
        #print("\n-------- Área de Operações ---------\n")
        #print(f'   Agência: {agencia_conta}     Conta: {codigo_conta}\n')
        #print("Escolha a operação que deseja efetuar: ")
        #for opcao, descricao in TIPOS_OPERACOES.items():
        #    print(opcao, "-", descricao)
        #print("5 - Consultar Extrato")
        #print("6 - Consultar Saldo")
        #print("0 - Retornar para o menu anterior")

    def pega_dados_saida(self, saldo):
        print(f'Saldo disponível R$ {saldo:.2f}')
        is_saldo_positivo, valor = valida_operacao_saida(saldo)
        if is_saldo_positivo:
            return valor
        else:
            return None

    def pega_dados_deposito(self):
        print("Realizar depósito:")
        return valida_operacao_entrada()

    def pega_chave_PIX(self):
        return input("Informe a chave PIX para transferência: ")

    def pega_codigo_conta_destino(self):
        while True:
            try:
                codigo_conta_destino = int(input("Informe o código da conta destino: "))
                break
            except:
                print("O código digitado é inválido!")
        return codigo_conta_destino

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
        valor_str = str(dados_operacao["Valor"])
        print(f'{dados_operacao["Codigo"]}  {dados_operacao["Tipo"].ljust(21)}  {dados_operacao["Data"]}  R${valor_str.ljust(10)}  {dados_operacao["Desc"].ljust(10)} {dados_operacao["Chave"]}')


    def mostra_mensagem(self, msg):
        print(msg)

