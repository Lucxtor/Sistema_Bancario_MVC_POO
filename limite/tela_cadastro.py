from limite.lib_limite import valida_opcao

class TelaCadastro:
    def tela_opcoes(self):
        self.exibe_menu()
        return valida_opcao([0,1,2])

    def exibe_menu(self):
        print("\n-------- Área de Cadastros ---------\n")
        print("Escolha o cadastro que deseja gerenciar: ")
        print("1 - Gerenciar Pessoas")
        print("2 - Gerenciar Contas")
        print("0 - Retornar para o menu anterior")