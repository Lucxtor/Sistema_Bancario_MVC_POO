from limite.lib_limite import valida_opcao, cpf_valido

class TelaConta:
    def tela_opcoes(self):
        self.exibe_menu()
        return valida_opcao([0,1,2,3])

    def exibe_menu(self):
        print("\n-------- Gerenciamento de conta ---------\n")
        print("Escolha como deseja gerenciar a conta: ")
        print("1 - Cadastrar nova conta")
        print("2 - Excluir conta")
        print("3 - Listar informações")
        print("0 - Retornar para o menu anterior")



    def pega_dados_conta(self):
        print("-------- Dados da Conta ----------")
        cpf_titular = cpf_valido()
        print("Escolha qual tipo de conta deseja criar: ")
        print("1 - Conta Corrente")
        print("2 - Conta Poupança")
        print("3 - Conta Salário")
        tipo_conta = valida_opcao([1,2,3])
        senha = input("Digite sua senha da conta: ")
        return {"tipo_conta": tipo_conta, "cpf_titular": cpf_titular, "senha_conta":senha}

    def seleciona_codigo(self):
        #fazer tratamento de excessões(Verificar se só tem números e se tem 4 números)
        codigo_conta = int(input("Digite o código da conta que deseja excluir: "))
        return codigo_conta

    def pega_senha_conta(self):
        return input("Digite a sua senha para prosseguir com a operação: ")

    def mostra_mensagem(self, msg):
        print(msg)