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

    def tela_opcoes_cadastros(self):
        self.exibe_menu_cadastros()
        return valida_opcao([0, 1, 2])

    def exibe_menu_cadastros(self):
        print("\n-------- Área de Cadastros ---------\n")
        print("Escolha o cadastro que deseja gerenciar: ")
        print("1 - Gerenciar Pessoas")
        print("2 - Gerenciar Contas")
        print("0 - Retornar para o menu anterior")

    def area_funcionarios(self):
        self.menu_area_funcionarios()
        return valida_opcao([0,1,2])

    def menu_area_funcionarios(self):
        print("\n-------- Área dos Funcionários  ---------\n")
        print("Escolha a opção que deseja acessar: ")
        print("1 - Listar Contas")
        print("2 - Listar Clientes")
        print("0 - Retornar para o menu anterior")
