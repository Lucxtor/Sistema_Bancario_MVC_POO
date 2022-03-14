from limite.tela import Tela
import PySimpleGUI as sg
from excecao.valorNegativoException import ValorNegativoException
from excecao.saldoIndisponivelException import SaldoIndisponivelException

class TelaOperacao(Tela):

    def __init__(self):
        super().__init__()

    def close(self):
        self.__window.Close()

    def exibe_menu_operacoes(self, agencia_conta, codigo_conta):
        self.menu_operacoes(agencia_conta, codigo_conta)
        botao, valores = self.__window.Read()
        return botao


    def menu_operacoes(self, agencia_conta, codigo_conta):
        layout = [
            [sg.Text('Área de Operações')],
            [sg.Text(f'Agência: {agencia_conta}     Conta: {codigo_conta}')],
            [sg.Text('Escolha a operação que deseja efetuar')],
            [sg.Submit('Saque', key=1)],
            [sg.Submit('Depósito', key=2)],
            [sg.Submit('Transferência Ted/Doc', key=3)],
            [sg.Submit('Transferência PIX', key=4)],
            [sg.Submit('Consultar Extrato', key=5)],
            [sg.Submit('Consultar Saldo', key=6)],
            [sg.Cancel('Retornar para o menu anterior', key=0)],
        ]
        self.__window = sg.Window('Área de Operações').Layout(layout)

    def pega_dados_saida(self, saldo):
        super().mostra_mensagem(f'Saldo disponível R$ {saldo:.2f}')
        is_saldo_positivo, valor = self.valida_operacao_saida(saldo)
        if is_saldo_positivo:
            return valor
        else:
            return None

    def pega_dados_deposito(self):
        layout = [
            [sg.Text('Digite qual o valor da operação: ')],
            [sg.Text('Valor:'), sg.InputText('', key='valor')],
            [sg.Submit(), sg.Cancel()],
        ]
        self.__window = sg.Window('Pega Valor').Layout(layout)
        botao, valor = self.__window.Read()
        if botao == None:
            exit(0)
        elif botao == 'Cancel':
            return botao
        else:
            return valor['valor']

    def pega_chave_PIX(self):
        layout = [
            [sg.Text('Informe a chave PIX para transferência')],
            [sg.Text('Chave PIX:'), sg.InputText('', key='chave')],
            [sg.Submit(), sg.Cancel()],
        ]
        self.__window = sg.Window('Cadastro Chave PIX').Layout(layout)
        botao, valor = self.__window.Read()
        if botao == None:
            exit(0)
        elif botao == 'Cancel':
            return botao
        else:
            return valor['chave']

    def pega_codigo_conta_destino(self):
        while True:
            try:
                layout = [
                    [sg.Text('Informe o código da conta destino: ')],
                    [sg.Text('Código:'), sg.InputText('', key='codigo')],
                    [sg.Submit(), sg.Cancel()],
                ]
                self.__window = sg.Window('Pega Código Conta Destino').Layout(layout)
                botao, valor = self.__window.Read()
                self.__window.Close()
                if botao == None:
                    exit(0)
                elif botao == 'Cancel':
                    return botao
                else:
                    return int(valor['codigo'])
                break
            except:
                self.__window.Close()
                super().mostra_mensagem("O código digitado é inválido!")

    def exibe_saldo(self, saldo_final, saldo_depositos, saldo_saques, saldo_transferencia_enviadas, saldo_transferencia_recebidas, saldo_transferencia_entrada_vs_saida):
        layout = [
            [sg.Text(f'O saldo em conta atualmente é R$ {saldo_final:.2f}')],
            [sg.Text(f'O saldo de movimentações é:')],
            [sg.Text(f'   Saques: R$ {saldo_saques:.2f}   Depósitos: R$ {saldo_depositos:.2f}')],
            [sg.Text(f'O saldo entre transferências é:')],
            [sg.Text(f'   Transferências enviadas: R$ {saldo_transferencia_enviadas:.2f}')],
            [sg.Text(f'   Transferências recebidas: R$ {saldo_transferencia_recebidas:.2f}')],
            [sg.Text(f'O saldo de transferências entre entradas e saídas: R$ {saldo_transferencia_entrada_vs_saida:.2f}')],
            [sg.Submit('Ok')],
        ]
        self.__window = sg.Window('Exibe Saldo').Layout(layout)
        botao, valor = self.__window.Read()
        self.__window.Close()
        return botao

    def exibe_extrato(self, saldo, operacoes):
        linhaSaldo = [[sg.Text("O saldo em conta é R$ " + str(saldo), size=(50, 2))]]
        cabecalho = [[sg.Text('Código', size=(8, 1))] + [sg.Text('Tipo da Operação', size=(21, 1))] + [
            sg.Text('Data da Operação', size=(20, 1))] + [sg.Text('Valor ( R$ )', size=(10, 1))] + [sg.Text('Descrição', size=(10, 1))] + [sg.Text('Chave', size=(10, 1))]]
        linhas = []
        for operacao in operacoes:
            linhas += [[sg.Text(operacao['Codigo'], size=(8, 1))] + [sg.Text(operacao['Tipo'], size=(21, 1))] + [
                sg.Text(operacao['Data'], size=(20, 1))] + [sg.Text("R$ " + str(operacao['Valor']), size=(10, 1))] + [
                sg.Text(operacao['Desc'], size=(10, 1))] + [sg.Text(operacao['Chave'], size=(10, 1))]]

        layout = linhaSaldo + cabecalho + linhas

        self.__window = sg.Window('Exibe Extrato').Layout(layout)
        botao, valor = self.__window.Read()

    def valida_operacao_saida(self, saldo):
        if saldo > 0:
            while True:
                try:
                    layout = [
                        [sg.Text('Digite qual o valor da operação: ')],
                        [sg.Text('Valor:'), sg.InputText('', key='valor')],
                        [sg.Submit(), sg.Cancel()],
                    ]
                    self.__window = sg.Window('Pega Valor').Layout(layout)
                    botao, valor = self.__window.Read()
                    valor_operacao = float(valor['valor'])

                    #Regra de Negócio: Não é permitida a transferência de valores negativos + Qualquer operação de saída apenas pode ocorrer enquanto houver saldo disponível
                    if valor_operacao > saldo:
                        raise SaldoIndisponivelException
                    if valor_operacao <= 0:
                        raise ValorNegativoException

                except SaldoIndisponivelException:
                    self.mostra_mensagem("O valor digitado é superior ao saldo para transferencias, por favor, tente novamente!")
                    self.__window.Close()

                except ValorNegativoException:
                    self.mostra_mensagem("O valor digitado é negativo, por favor, tente novamente!")
                    self.__window.Close()

                except:
                    self.mostra_mensagem("O valor digitado é invalido, por favor, tente novamente!")
                    self.__window.Close()

                else:
                    self.__window.Close()
                    return True, valor_operacao
        else:
            self.mostra_mensagem("Saldo insuficiente!")
            return False, None
