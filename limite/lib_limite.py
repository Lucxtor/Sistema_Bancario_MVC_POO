TIPOS_OPERACOES = {1: "Saque", 2: "Depósito", 3: "Transferência Ted/Doc", 4: "Transferência PIX"}

def valida_opcao(opcoesValidas):
    while True:
        try:
            opcao = int(input("\nEscolha a opção: "))
            while opcao not in opcoesValidas:
                print("A opção escolhida é inválida, por favor, tente novamente!")
                opcao = int(input("\nEscolha uma nova opção: "))
        except:
            print("A opção digitada é invalida, por favor, tente novamente!")
        else:
            return opcao

def cpf_valido():
    while True:
        cpf = input("CPF ( Digite o CPF contendo apenas números ): ")
        if len(cpf) != 11:
            print("Número de dígitos incorreto, verifique!")
        else:
            try:
                for i in range(11):
                    teste = int(cpf[i])
            except:
                print("O CPF possui dígitos incorretos, verifique!")
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
                        print("O CPF digitado é inválido!")
                else:
                    print("O CPF digitado é inválido!")

def valida_operacao_saida(saldo):
    if saldo > 0:
        while True:
            try:
                valor_operacao = float(input("Digite qual o valor da operação: "))
                while(valor_operacao > saldo or valor_operacao <= 0):
                    print("Valor inválido, tente novamente!")
                    valor_operacao = float(input("Digite qual o valor da operação: "))
            except:
                print("A opção digitada é invalida, por favor, tente novamente!")
            else:
                return valor_operacao
    else:
        print("Saldo insuficiente!")
        return 0

def valida_operacao_entrada():
    while True:
        try:
            valor_operacao = float(input("Digite qual o valor da operação: "))
            while(valor_operacao <= 0):
                print("Valor inválido, tente novamente!")
                valor_operacao = float(input("Digite qual o valor da operação: "))
        except:
            print("A opção digitada é invalida, por favor, tente novamente!")
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