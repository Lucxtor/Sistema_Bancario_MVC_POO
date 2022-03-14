from limite.tela import Tela
import PySimpleGUI as sg

class TelaConta(Tela):

    def __init__(self):
        super().__init__()

    def close(self):
        self.__window.Close()

    def exibe_menu_conta(self):
        self.menu_conta()
        botao, valores = self.__window.Read()
        return botao

    def menu_conta(self):
        layout = [
            [sg.Text('Gerenciamento de Conta')],

            [sg.Text('Escolha como deseja gerenciar a conta')],
            [sg.Submit('Cadastrar nova conta', key=1)],
            [sg.Submit('Excluir conta', key=2)],
            [sg.Submit('Listar informações', key=3)],
            [sg.Submit('Cadastrar chave PIX', key=4)],
            [sg.Cancel('Retornar para o menu anterior', key=0)],

        ]
        self.__window = sg.Window('Gerenciamento de Conta').Layout(layout)

    def pega_dados_conta(self):
        cpf_titular = super().cpf_valido()
        layout = [
                [sg.Text('Dados da Conta')],
                [sg.Text("Escolha qual tipo de conta deseja criar: ")],
                [sg.Combo(['Corrente', 'Poupança', 'Salário'],
                          key='Tipo_Conta',
                          default_value='Escolha uma opção',
                          size=(20, 1))],
                [sg.Text('Senha:'), sg.InputText('', key='senha')],
                [sg.Submit(), sg.Cancel()],
                ]
        self.__window = sg.Window('Pega Dados Conta').Layout(layout)
        botao, valor = self.__window.Read()
        if botao != None:
            if valor['Tipo_Conta'] == 'Corrente':
                tipo_conta = 1
            elif valor['Tipo_Conta'] == 'Poupança':
                tipo_conta = 2
            elif valor['Tipo_Conta'] == 'Salário':
                tipo_conta = 3
            return {"tipo_conta": tipo_conta, "cpf_titular": cpf_titular, "senha_operacoes": valor['senha']}
        else:
            exit(0)

    def seleciona_codigo(self):
        layout = [
            [sg.Text('Digite o código da conta que deseja acessar: ')],
            [sg.Text('Código:'), sg.InputText('', key='codigo')],
            [sg.Submit(), sg.Cancel()],
        ]
        self.__window = sg.Window('Pega Código Conta').Layout(layout)
        botao, valor = self.__window.Read()
        if botao == None:
            exit(0)
        elif botao == 'Cancel':
            return botao
        else:
            return valor['codigo']

    def pega_senha_operacoes(self):
        layout = [
            [sg.Text('Digite a sua senha para prosseguir com a operação')],
            [sg.Text('Senha:'), sg.InputText('', key='senha')],
            [sg.Submit(), sg.Cancel()],
        ]
        self.__window = sg.Window('Área de Operações').Layout(layout)
        botao, valor = self.__window.Read()
        if botao == None:
            exit(0)
        elif botao == 'Cancel':
            return botao
        else:
            return valor['senha']

    def lista_conta(self, dados_conta):
        tipo_escolhido = dados_conta["tipo"]
        if tipo_escolhido == 1:
            tipo_conta = super().TIPOS_CONTAS[1]
        elif tipo_escolhido == 2:
            tipo_conta = super().TIPOS_CONTAS[2]
        else:
            tipo_conta = super().TIPOS_CONTAS[3]
        chaves = dados_conta["chaves"]
        layout = [
            [sg.Text('Lista Conta')],

            [sg.Text((str(dados_conta["codigo"]) + " - Conta " + tipo_conta + "Agência " + dados_conta["agencia"]))],
            [sg.Text("chaves PIX: " + str(chaves))],
            [sg.Text((f"CPF do titular: {str(dados_conta['cpf'])[0:3]}.{str(dados_conta['cpf'])[3:6]}.{str(dados_conta['cpf'])[6:9]}-{str(dados_conta['cpf'])[9:11]}"))],
            [sg.Submit("Ok")],
        ]
        self.__window = sg.Window('Lista Conta').Layout(layout)
        botao, valores = self.__window.Read()

    def lista_contas(self, contas):
        cabecalho = [[sg.Text('Código', size=(8, 1))] + [sg.Text('Tipo Conta', size=(15, 1))] +
                     [sg.Text('Agência', size=(8, 1))] + [sg.Text('CPF titular', size=(15, 1))] +
                     [sg.Text('Chaves PIX', size=(15, 1))]]
        linhas = []
        for conta in contas:
            linhas += [[sg.Text(conta.codigo, size=(8, 1))] + [sg.Text(conta.tipo, size=(15, 1))] +
                       [sg.Text(conta.agencia, size=(8, 1))] + [sg.Text(conta.titular.cpf, size=(15, 1))] +
                       [sg.Text(str(conta.chaves_PIX))]]
        layout = cabecalho + linhas

        self.__window = sg.Window('Lista de Contas').Layout(layout)
        botao, valor = self.__window.Read()

    def pega_chave_PIX(self):
        layout = [
            [sg.Text('Digite a chave PIX que deseja cadastrar: ')],
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
