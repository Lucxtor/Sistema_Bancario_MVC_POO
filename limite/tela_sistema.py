import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def exibe_menu_sistema(self):
        self.menu_sistema()
        botao, valores = self.__window.Read()
        return botao

    def menu_sistema(self):
        layout = [
            [sg.Text('Sistema Bancário')],

            [sg.Text('Escolha a área que deseja acessar')],
            [sg.Submit('Área de Cadastros', key=1)],
            [sg.Submit('Área de Operações', key=2)],
            [sg.Submit('Área de Funcionários', key=3)],
            [sg.Cancel('Finalizar Sistema', key=0)],
        ]
        self.__window = sg.Window('Sistema Bancário').Layout(layout)

    def exibe_menu_cadastros(self):
        self.menu_cadastros()
        botao, valor = self.__window.Read()
        return botao

    def menu_cadastros(self):
        layout = [
            [sg.Text('Área de Cadastros')],

            [sg.Text('Escolha o cadastro que deseja gerenciar')],
            [sg.Submit('Gerenciar Pessoas', key=1)],
            [sg.Submit('Gerenciar Contas', key=2)],
            [sg.Cancel('Retornar para o menu anterior', key=0)],
        ]
        self.__window = sg.Window('Área de Cadastros').Layout(layout)

    def exibe_menu_area_funcionarios(self, nome_funcionario):
        self.menu_area_funcionarios(nome_funcionario)
        botao, valor = self.__window.Read()
        if botao == None:
            exit(0)
        else:
            return botao

    def menu_area_funcionarios(self, nome_funcionario):
        layout = [
            [sg.Text('Área dos Funcionários')],

            [sg.Text(f'Bem-vindo(a) {nome_funcionario}!')],
            [sg.Text('Escolha o cadastro que deseja gerenciar')],
            [sg.Submit('Listar Contas', key=1)],
            [sg.Submit('Listar Clientes', key=2)],
            [sg.Cancel('Retornar para o menu anterior', key=0)],
        ]
        self.__window = sg.Window('Área dos Funcionários').Layout(layout)

    #EXEMPLO INPUT
    def pega_senha_funcionario(self):
        layout = [
            [sg.Text('Informe a senha do funcionário para liberar o acesso')],
            [sg.Text('Senha:'), sg.InputText('', key='senha')],
            [sg.Submit(), sg.Cancel()],
        ]
        self.__window = sg.Window('Área de Cadastros').Layout(layout)
        botao, valor = self.__window.Read()
        if botao == None:
            exit(0)
        else:
            return valor['senha']

    def mostra_mensagem(self, msg):
        layout = [
            [sg.Text(msg)],
            [sg.Submit('Ok')]
        ]
        self.__window = sg.Window('Mensagem').Layout(layout)
        botao = self.__window.Read()
        if botao == None:
            exit(0)
        else:
            return botao