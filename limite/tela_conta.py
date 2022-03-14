from limite.tela import Tela
import PySimpleGUI as sg

class TelaConta(Tela):

    def close(self):
        #self.__window.Close()
        pass

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
            [sg.Cancel('Voltar ao menu anterior', key=0)],
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
            return {"tipo_conta": tipo_conta, "cpf_titular": cpf_titular, "senha_operacoes": 'senha'}
        else:
            exit(0)

    def seleciona_codigo(self):
        while True:
            try:
                codigo_conta = super().layout_input('Digite o código da conta que deseja acessar: ', 'Código', 'Pega Código Conta')
                codigo_conta = int(codigo_conta)
                break
            except:
                self.mostra_mensagem("O código digitado é inválido!")
        return codigo_conta

    def pega_senha_operacoes(self):
        layout = [
            [sg.Text('Digite a sua senha para prosseguir com a operação')],
            [sg.Text('Senha:'), sg.InputText('', key='senha')],
            [sg.Submit(), sg.Cancel()],
        ]
        self.__window = sg.Window('Área de Cadastros').Layout(layout)
        botao, valor = self.__window.Read()
        if botao == None:
            exit(0)
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
        print("\nConta:", dados_conta["codigo"], "-", tipo_conta, "- Agência:", dados_conta["agencia"])
        chaves = dados_conta["chaves"]
        if len(chaves) != 0:
            print("Chaves PIX:", end=" ")
            for chave in chaves:
                print(chave, end=" ")
            print("")
        print(f"CPF do titular: {str(dados_conta['cpf'])[0:3]}.{str(dados_conta['cpf'])[3:6]}.{str(dados_conta['cpf'])[6:9]}-{str(dados_conta['cpf'])[9:11]}")

    def pega_chave_PIX(self):
        super().layout_input('Digite a chave PIX que deseja cadastrar:', 'Chave PIX', 'Cadastro Chave PIX')
