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

    #def tela_opcoes(self):
    #    self.exibe_menu()
    #    return valida_opcao([0,1,2,3])

    #def exibe_menu(self):
    #    print("\n-------- Sistema Bancário  ---------\n")
    #    print("Escolha a área que deseja acessar: ")
    #    print("1 - Área de Cadastros")
    #    print("2 - Área de Operações")
    #    print("3 - Área de Funcionários")
    #    print("0 - Finalizar sistema")

    def exibe_menu_cadastros(self):
        self.menu_cadastros()
        botao, valores = self.__window.Read()
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

        # print("\n-------- Área de Cadastros ---------\n")
        # print("Escolha o cadastro que deseja gerenciar: ")
        # print("1 - Gerenciar Pessoas")
        # print("2 - Gerenciar Contas")
        # print("0 - Retornar para o menu anterior")

    def exibe_menu_area_funcionarios(self, nome_funcionario):
        self.menu_area_funcionarios(nome_funcionario)
        return valida_opcao([0,1,2])

    def menu_area_funcionarios(self, nome_funcionario):
        print("\n-------- Área dos Funcionários  ---------\n")
        print(f'Bem-vindo(a) {nome_funcionario}')
        print("\nEscolha a opção que deseja acessar: ")
        print("1 - Listar Contas")
        print("2 - Listar Clientes")
        print("0 - Retornar para o menu anterior")

    def pega_senha_funcionario(self):
        return input("Informe a senha do funcionário para liberar o acesso: ")

    def mostra_mensagem(self, msg):
        print(msg)
