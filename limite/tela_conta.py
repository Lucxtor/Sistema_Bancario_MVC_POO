from limite.lib_limite import valida_opcao, cpf_valido

class TelaConta:
    def tela_opcoes(self):
        self.exibe_menu()
        return valida_opcao([0,1,2,3,4])

    def exibe_menu(self):
        print("\n-------- Gerenciamento de conta ---------\n")
        print("Escolha como deseja gerenciar a conta: ")
        print("1 - Cadastrar nova conta")
        print("2 - Excluir conta")
        print("3 - Listar informações")
        print("4 - Cadastrar chave PIX")
        print("0 - Retornar para o menu anterior")



    def pega_dados_conta(self):
        print("\n-------- Dados da Conta ----------\n")
        cpf_titular = cpf_valido()
        print("\nEscolha qual tipo de conta deseja criar: ")
        print("1 - Conta Corrente")
        print("2 - Conta Poupança")
        print("3 - Conta Salário")
        tipo_conta = valida_opcao([1,2,3])
        senha = input("Digite sua senha da conta: ")
        return {"tipo_conta": tipo_conta, "cpf_titular": cpf_titular, "senha_operacoes":senha}

    def seleciona_codigo(self):
        while True:
            try:
                codigo_conta = int(input("Digite o código da conta que deseja acessar: "))
                break
            except:
                print("O código digitado é inválido!")
        return codigo_conta

    def pega_senha_operacoes(self):
        return input("Digite a sua senha para prosseguir com a operação: ")

    def mostra_mensagem(self, msg):
        print(msg)

    def lista_conta(self, dados_conta):
        tipo_escolhido = dados_conta["tipo"]
        if tipo_escolhido == 1:
            tipo_conta = "Corrente"
        elif tipo_escolhido == 2:
            tipo_conta = "Poupança"
        else:
            tipo_conta = "Salário"
        print("\nConta:", dados_conta["codigo"], "-", tipo_conta, "- Agência:", dados_conta["agencia"])
        chaves = dados_conta["chaves"]
        if len(chaves) != 0:
            print("Chaves PIX:", end=" ")
            for chave in chaves:
                print(chave, end=" ")
            print("")
        print(f"CPF do titular: {str(dados_conta['cpf'])[0:3]}.{str(dados_conta['cpf'])[3:6]}.{str(dados_conta['cpf'])[6:9]}-{str(dados_conta['cpf'])[9:11]}")

    def pega_chave_PIX(self):
        return input("Digite a chave PIX que deseja cadastrar: ")
