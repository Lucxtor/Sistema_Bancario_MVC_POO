from limite.tela import Tela
import PySimpleGUI as sg

class TelaOperacao(Tela):

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

    def pega_dados_saida(self, saldo):
        super().mostra_mensagem(f'Saldo disponível R$ {saldo:.2f}')
        is_saldo_positivo, valor = super().valida_operacao_saida(saldo)
        if is_saldo_positivo:
            return valor
        else:
            return None

    def pega_dados_deposito(self):
        return super().valida_operacao_entrada()

    def pega_chave_PIX(self):
        return super().layout_input("Informe a chave PIX para transferência", "Chave PIX", "Chave PIX")

    def pega_codigo_conta_destino(self):
        while True:
            try:
                codigo_conta_destino = int(super().layout_input("Informe o código da conta destino", "Código", "Código Conta Destino"))
                break
            except:
                super().mostra_mensagem("O código digitado é inválido!")
        return codigo_conta_destino

    def exibe_saldo(self, saldo_final, saldo_depositos, saldo_saques, saldo_transferencia_enviadas, saldo_transferencia_recebidas, saldo_transferencia_entrada_vs_saida):
        layout = [
            [sg.Text(f'O saldo em conta atualmente é R$ {saldo_final:.2f}')]
            [sg.Text(f'O saldo de movimentações é:')]
            [sg.Text(f'   Saques: R$ {saldo_saques:.2f}   Depósitos: R$ {saldo_depositos:.2f}')]
            [sg.Text(f'O saldo entre transferências é:')]
            [sg.Text(f'   Transferências enviadas: R$ {saldo_transferencia_enviadas:.2f}')]
            [sg.Text(f'   Transferências recebidas: R$ {saldo_transferencia_recebidas:.2f}')]
            [sg.Text(f'O saldo de transferências entre entradas e saídas: R$ {saldo_transferencia_entrada_vs_saida:.2f}')]
            [sg.Submit('Ok')]
        ]
        self.__window = sg.Window('Exibe Saldo').Layout(layout)
        botao, valor = self.__window.Read()
        if botao == None:
            exit(0)
        else:
            return valor['valor']

    def exibe_extrato(self, dados_operacao):
        valor_str = str(dados_operacao["Valor"])
        layout = [
            [sg.Text(f'{dados_operacao["Codigo"]}  {dados_operacao["Tipo"].ljust(21)}  {dados_operacao["Data"]}  R${valor_str.ljust(10)}  {dados_operacao["Desc"].ljust(10)} {dados_operacao["Chave"]}')]
            [sg.Submit('Ok')]
        ]
        self.__window = sg.Window('Exibe Extrato').Layout(layout)
        botao, valor = self.__window.Read()
        if botao == None:
            exit(0)
        else:
            return valor['valor']
