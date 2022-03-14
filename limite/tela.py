from abc import ABC, abstractmethod
import PySimpleGUI as sg

class Tela(ABC):
    TIPOS_OPERACOES = {1: "Saque", 2: "Depósito", 3: "Transferência Ted/Doc", 4: "Transferência PIX"}
    TIPOS_CONTAS = {1:"Corrente", 2:"Popupança", 3:"Salário"}

    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def valida_opcao(self, opcoesValidas):
        while True:
            try:
                opcao = int(input("\nEscolha a opção: "))
                while opcao not in opcoesValidas:
                    self.mostra_mensagem("A opção escolhida é inválida, por favor, tente novamente!")
                    opcao = int(input("\nEscolha uma nova opção: "))
            except:
                print("A opção digitada é invalida, por favor, tente novamente!")
            else:
                return opcao

    #Regra de negócio: O cadastro da Pessoa deve utilizar um CPF válido
    def cpf_valido(self):
        while True:
            layout = [
                [sg.Text('Digite o CPF (contendo apenas números)')],
                [sg.Text('CPF:'), sg.InputText('', key='cpf')],
                [sg.Submit(), sg.Cancel()],
            ]
            self.__window = sg.Window('Pega CPF').Layout(layout)
            botao, valor = self.__window.Read()
            cpf = valor['cpf']
            self.__window.Close()
            if len(cpf) != 11:
                self.mostra_mensagem("Número de dígitos incorreto, verifique!")
            else:
                try:
                    for i in range(11):
                        teste = int(cpf[i])
                except:
                    self.mostra_mensagem("O CPF possui dígitos incorretos, verifique!")
                else:
                    soma = 0
                    aux = 0
                    for i in range(10, 1, -1):
                        soma += int(cpf[aux:aux+1]) * i
                        aux += 1
                    digito_verificador_01 = int(cpf[9])
                    digito_verificador_02 = int(cpf[10])
                    if (soma * 10) % 11 == digito_verificador_01 or (soma * 10) % 11 == 10 and digito_verificador_01 == 0:
                        soma = 0
                        aux = 0
                        for i in range(11, 1, -1):
                            soma += int(cpf[aux:aux + 1]) * i
                            aux += 1
                        if (soma * 10) % 11 == digito_verificador_02 or (
                                soma * 10) % 11 == 10 and digito_verificador_02 == 0:
                            return cpf
                        else:
                            self.mostra_mensagem("O CPF digitado é inválido!")
                    else:
                        self.mostra_mensagem("O CPF digitado é inválido!")

    def valida_data(self, dia, mes, ano):
        meses_31 = [1, 3, 5, 7, 8, 10, 12]
        if ano >= 1 and mes <= 12 and mes >= 1 and dia <= 31 and dia >= 1:
            if mes == 2:
                if ano % 4 == 0 and dia <= 29:
                    return True
                elif dia <= 28:
                    return True
                else:
                    return False
            if mes in meses_31:
                return True
            elif dia <= 30:
                return True
        else:
            return False

    def mostra_mensagem(self, msg):
        sg.Popup(msg)
