from limite.lib_limite import valida_opcao

class TelaSistema:
    def tela_opcoes(self):
        self.exibe_menu()
        return valida_opcao([0,1,2,3])

    def exibe_menu(self):
        print("\n-------- Sistema Bancário  ---------\n")
        print("Escolha a área que deseja acessar: ")
        print("1 - Área de Cadastros")
        print("2 - Área de Operações")
        print("3 - Área de Funcionários")
        print("0 - Finalizar sistema")
