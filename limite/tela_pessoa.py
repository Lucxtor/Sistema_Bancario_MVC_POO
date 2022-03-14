from limite.tela import Tela
from datetime import datetime
import PySimpleGUI as sg

class TelaPessoa(Tela):

    def __init__(self):
        super().__init__()

    def close(self):
        self.__window.Close()

    def exibe_menu(self):
        self.menu()
        botao, valores = self.__window.Read()
        return botao

    def menu(self):
        layout = [
            [sg.Text('Gerenciamento de Pessoas')],

            [sg.Text('Escolha uma das opções abaixo: ')],
            [sg.Submit('Gerenciar clientes', key=1)],
            [sg.Submit('Gerenciar funcionarios', key=2)],
            [sg.Cancel('Retornar para o menu anterior', key=0)],
        ]
        self.__window = sg.Window('Gerenciamento de Pessoas').Layout(layout)

    def exibe_menu_gerencia(self, tipo):
        self.menu_gerencia(tipo)
        botao, valores = self.__window.Read()
        return botao

    def menu_gerencia(self, tipo):
        layout = [
            [sg.Text(('Gerenciamento de ' + tipo))],

            [sg.Text(("Escolha como deseja gerenciar o " + tipo + ": "))],
            [sg.Submit(('Cadastrar novo ' + tipo), key=1)],
            [sg.Submit(('Editar ' + tipo), key=2)],
            [sg.Submit(('Excluir ' + tipo), key=3)],
            [sg.Submit(('Listar ' + tipo), key=4)],
            [sg.Cancel('Retornar para o menu anterior', key=0)],
        ]
        self.__window = sg.Window('Gerenciamento de Pessoas').Layout(layout)

    def pega_dados_cliente(self):
        cpf = super().cpf_valido()
        while True:
            try:
                layout = [
                    [sg.Text('Cadastro de Clientes')],

                    [sg.Text('Nome: '), sg.InputText('', key='nome')],
                    [sg.Text('Data de nascimento: '), sg.Text('Dia:'),sg.InputText(key='dia', size=(4,1)),sg.Text('Mês:'), sg.InputText(key='mes', size=(4,1)),sg.Text('Ano:'), sg.InputText(key='ano', size=(4,1))],
                    [sg.Text('Senha para Edição: '), sg.InputText('', key='senha_cadastro')],
                    [sg.Submit(), sg.Cancel()],
                ]
                self.__window = sg.Window('Cadastro de Clientes').Layout(layout)

                botao, valor = self.__window.Read()
                data_nascimento_dia = int(valor['dia'])
                data_nascimento_mes = int(valor['mes'])
                data_nascimento_ano = int(valor['ano'])
                if super().valida_data(data_nascimento_dia, data_nascimento_mes, data_nascimento_ano):
                    data_nascimento_str = f'{data_nascimento_dia}/{data_nascimento_mes}/{data_nascimento_ano}'
                    data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y')
                    break
                else:
                    sg.Popup("Parece que a data informada é invalida, tente novamente!")
            except:
                sg.Popup("Parece que algo deu errado, tente novamente!")

        return {"nome": valor['nome'], "data_nascimento": data_nascimento, "cpf": cpf, "senha_cadastro": valor['senha_cadastro']}

    def pega_dados_cliente_alteracao(self):
        layout = [
            [sg.Text('Atualizar Cadastro do Cliente')],

            [sg.Text('Nome: '), sg.InputText('', key='nome')],
            [sg.Text('Nova senha para Edição: '), sg.InputText('', key='senha_cadastro')],
            [sg.Submit(), sg.Cancel()],
        ]
        self.__window = sg.Window('Cadastro de Clientes').Layout(layout)

        botao, valor = self.__window.Read()
        if botao == "Cancel":
            self.menu_gerencia('cliente')
        else:
            return {"nome": valor['nome'], "senha_cadastro": valor['senha_cadastro']}

    def pega_dados_funcionario(self):
        cpf = super().cpf_valido()
        while True:
            try:
                layout = [
                    [sg.Text('Cadastro de Funcionários')],

                    [sg.Text('Nome: '), sg.InputText('', key='nome')],
                    [sg.Text('Data de nascimento: '), sg.Text('Dia:'), sg.InputText(key='dia', size=(4, 1)),
                     sg.Text('Mês:'), sg.InputText(key='mes', size=(4, 1)), sg.Text('Ano:'),
                     sg.InputText(key='ano', size=(4, 1))],
                    [sg.Text('Senha: '), sg.InputText('', key='senha_funcionario')],
                    [sg.Text('Número CTPS: '), sg.InputText('', key='numero_CTPS')],
                    [sg.Submit(), sg.Cancel()],
                ]
                self.__window = sg.Window('Cadastro de Clientes').Layout(layout)

                botao, valor = self.__window.Read()

                # Regra de Negócio: O número CTPS deve ter 8 dígitos
                if len(valor['numero_CTPS']) != 8:
                    sg.Popup("Número de documento inválido, deve conter 8 dígitos!")
                    raise ValueError

                data_nascimento_dia = int(valor['dia'])
                data_nascimento_mes = int(valor['mes'])
                data_nascimento_ano = int(valor['ano'])
                if super().valida_data(data_nascimento_dia, data_nascimento_mes, data_nascimento_ano):
                    data_nascimento_str = f'{data_nascimento_dia}/{data_nascimento_mes}/{data_nascimento_ano}'
                    data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y')
                    break
                else:
                    sg.Popup("Parece que a data informada é invalida, tente novamente!")
            except:
                sg.Popup("Parece que algo deu errado, tente novamente!")

        return {"nome": valor['nome'], "data_nascimento": data_nascimento, "cpf": cpf,
                "senha_funcionario": valor['senha_funcionario'], "numero_CTPS": valor['numero_CTPS']}

    def pega_dados_funcionario_alteracao(self):
        layout = [
            [sg.Text('Atualizar Cadastro do Funcionário')],

            [sg.Text('Nome: '), sg.InputText('', key='nome')],
            [sg.Text('Nova senha : '), sg.InputText('', key='senha_funcionario')],
            [sg.Submit(), sg.Cancel()],
        ]
        self.__window = sg.Window('Cadastro de Funcionário').Layout(layout)

        botao, valor = self.__window.Read()

        return {"nome": valor['nome'], "senha_funcionario": valor['senha_funcionario']}

    def seleciona_cpf(self):
        return super().cpf_valido()

    def pega_senha_pessoa(self):
        layout = [
            [sg.Text('Digite a senha para prosseguir com a operação:')],
            [sg.Text('Senha:'), sg.InputText('', key='senha')],
            [sg.Submit(), sg.Cancel()],
        ]
        self.__window = sg.Window('Pega Senha').Layout(layout)
        botao, valor = self.__window.Read()
        if botao == None:
            exit(0)
        elif botao == 'Cancel':
            return botao
        else:
            return valor['senha']

    def lista_cliente(self, dados_cliente):
        layout = [
            [sg.Text('Lista Clientes')],

            [sg.Text(("Cliente: "+ str(dados_cliente["codigo"])+ " - " + dados_cliente["nome"]))],
            [sg.Text(("Data de nascimento do cliente: " + dados_cliente["data_nascimento"].strftime('%d/%m/%Y')))],
            [sg.Text((f"CPF do cliente: {str(dados_cliente['cpf'])[0:3]}.{str(dados_cliente['cpf'])[3:6]}.{str(dados_cliente['cpf'])[6:9]}-{str(dados_cliente['cpf'])[9:11]}"))],
            [sg.Submit("Ok")],
        ]
        self.__window = sg.Window('Lista Clientes').Layout(layout)
        botao, valores = self.__window.Read()

    def lista_clientes(self, clientes):
        cabecalho = [[sg.Text('Código', size=(8, 1))] + [sg.Text('Nome', size=(20,1))] + [sg.Text('Data de Nascimento', size=(20,1))] + [sg.Text('CPF', size=(15,1))]]
        linhas = []
        for cliente in clientes:
            linhas += [[sg.Text(cliente.codigo, size=(8, 1))] + [sg.Text(cliente.nome, size=(20, 1))] + [sg.Text(cliente.data_nascimento, size=(20, 1))] + [sg.Text(cliente.cpf, size=(15, 1))]]

        layout = cabecalho + linhas

        self.__window = sg.Window('Lista de Clientes').Layout(layout)
        botao, valor = self.__window.Read()

    def lista_funcionario(self, dados_funcionario):
        layout = [
            [sg.Text('Lista Funcionários')],

            [sg.Text(("Funcionário: " + str(dados_funcionario["codigo"]) + " - " + dados_funcionario["nome"]))],
            [sg.Text(("Data de nascimento do funcinário: " + dados_funcionario["data_nascimento"].strftime('%d/%m/%Y')))],
            [sg.Text((f"CPF do cliente: {str(dados_funcionario['cpf'])[0:3]}.{str(dados_funcionario['cpf'])[3:6]}.{str(dados_funcionario['cpf'])[6:9]}-{str(dados_funcionario['cpf'])[9:11]}"))],
            [sg.Text(("Número CTPS do funcinário: " + dados_funcionario["numero_CTPS"]))],
            [sg.Submit("Ok")],
        ]
        self.__window = sg.Window('Lista Clientes').Layout(layout)
        botao, valores = self.__window.Read()
