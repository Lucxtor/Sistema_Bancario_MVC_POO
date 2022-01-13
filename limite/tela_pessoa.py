from limite.lib_limite import valida_opcao

class TelaPessoa:
    def tela_opcoes(self):
        self.exibe_menu()
        return valida_opcao([0,1,2])

    def exibe_menu(self):
        print("\n-------- Gerenciamento de Pessoas ---------\n")
        print("Escolha uma das opções abaixo: ")
        print("1 - Gerenciar clientes")
        print("2 - Gerenciar funcionarios")
        print("0 - Retornar para o menu anterior")