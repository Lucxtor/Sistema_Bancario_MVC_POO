def valida_opcao(opcoesValidas):
    while True:
        try:
            opcao = int(input("\nEscolha a opção: "))
        except:
            print("A opção digitada é invalida, por favor, tente novamente!")
        else:
            while opcao not in opcoesValidas:
                print("A opção escolhida é invalida, por favor, tente novamente!")
                opcao = int(input("\nEscolha uma nova opção: "))
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
                if (soma * 10) % 11 != digito_verificador_01 or (soma * 10) % 11 == 10 and digito_verificador_01 != 0:
                    print("O CPF digitado é invalido!")
                else:
                    soma = 0
                    aux = 0
                    for i in range(11, 1, -1):
                        soma += int(cpf[aux:aux + 1]) * i
                        aux += 1
                    if (soma * 10) % 11 != digito_verificador_02 or (soma * 10) % 11 == 10 and digito_verificador_02 != 0:
                        print("O CPF digitado é invalido!")
                    else:
                        return cpf

def valida_operacao_saida(valor_operacao, saldo):
   while(valor_operacao > saldo or valor_operacao <= 0):
       print("Valor inválido, tente novamente!")
       valor_operacao = int(input("Digite qual o valor da operação: "))
   return valor_operacao
