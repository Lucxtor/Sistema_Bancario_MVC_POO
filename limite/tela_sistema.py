from limite.lib_limite import valida_opcao

class TelaSistema:
    def tela_opcoes(self):
        self.exibe_menu()
<<<<<<< Updated upstream
        opcao = int(input("Escolha a opcao:"))
        while opcao not in [0,1,2,3]:
            self.exibe_menu()
            opcao = int(input("Escolha a opcao:"))
        return opcao
=======
        return valida_opcao([0,1,2,3])
>>>>>>> Stashed changes

    def exibe_menu(self):
        print("-------- Sistema Bancário  ---------")
        print("Escolha a área que deseja acessar: ")
        print("1 - Área de cadastros")
        print("2 - Área de Operações")
        print("3 - Área de Funcionários")
        print("0 - Finalizar sistema")