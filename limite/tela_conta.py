from limite.lib_limite import valida_opcao

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