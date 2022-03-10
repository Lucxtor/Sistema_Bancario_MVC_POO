import PySimpleGUI as sg

TIPOS_OPERACOES = {1: "Saque", 2: "Depósito", 3: "Transferência Ted/Doc", 4: "Transferência PIX"}
TIPOS_CONTAS = {1:"Corrente", 2:"Popupança", 3:"Salário" }

def valida_opcao(opcoesValidas):
    while True:
        try:
            opcao = int(input("\nEscolha a opção: "))
            while opcao not in opcoesValidas:
                mostra_mensagem("A opção escolhida é inválida, por favor, tente novamente!")
                opcao = int(input("\nEscolha uma nova opção: "))
        except:
            print("A opção digitada é invalida, por favor, tente novamente!")
        else:
            return opcao

#Regra de negócio: O cadastro da Pessoa deve utilizar um CPF válido
def cpf_valido():
    while True:
        cpf = layout_input('Digite o CPF (contendo apenas números)', 'CPF', 'Pega CPF')
        if len(cpf) != 11:
            mostra_mensagem("Número de dígitos incorreto, verifique!")
        else:
            try:
                for i in range(11):
                    teste = int(cpf[i])
            except:
                mostra_mensagem("O CPF possui dígitos incorretos, verifique!")
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
                        mostra_mensagem("O CPF digitado é inválido!")
                else:
                    mostra_mensagem("O CPF digitado é inválido!")

def valida_operacao_saida(saldo):
    if saldo > 0:
        while True:
            try:
                valor_operacao = float(layout_input('Digite qual o valor da operação', 'Valor', 'Pega Valor'))
                #Regra de Negócio: Não é permitida a transferência de valores negativos + Qualquer operação de saída apenas pode ocorrer enquanto houver saldo disponível
                while(valor_operacao > saldo or valor_operacao <= 0):
                    mostra_mensagem("Valor inválido, tente novamente!")
                    valor_operacao = float(layout_input('Digite qual o valor da operação', 'Valor', 'Pega Valor'))

            except:
                mostra_mensagem("A opção digitada é invalida, por favor, tente novamente!")
            else:
                return True, valor_operacao
    else:
        mostra_mensagem("Saldo insuficiente!")
        return False, None

def valida_operacao_entrada():
    while True:
        try:
            valor_operacao = float(layout_input('Digite qual o valor da operação', 'Valor', 'Pega Valor'))
            while(valor_operacao <= 0):
                mostra_mensagem("Valor inválido, tente novamente!")
                valor_operacao = float(layout_input('Digite qual o valor da operação', 'Valor', 'Pega Valor'))
        except:
            mostra_mensagem("A opção digitada é inválida, por favor, tente novamente!")
        else:
            return valor_operacao

def valida_data(dia, mes, ano):
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

def mostra_mensagem(msg):
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

def layout_input(instrucao, valor, titulo):
    layout = [
        [sg.Text(instrucao)],
        [sg.Text(f'{valor}:'), sg.InputText('', key='valor')],
        [sg.Submit(), sg.Cancel()],
    ]
    self.__window = sg.Window(titulo).Layout(layout)
    botao, valor = self.__window.Read()
    if botao == None:
        exit(0)
    else:
        return valor['valor']