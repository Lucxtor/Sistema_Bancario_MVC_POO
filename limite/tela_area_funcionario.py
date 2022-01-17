class TelaAreaFuncionarios:
    def tela_opcoes(self):
        self.exibe_menu()
        return valida_opcao([0,1,2])

    def exibe_menu(self):
        print("\n-------- Área dos Funcionários  ---------\n")
        print("Escolha a ação que deseja executar: ")
        print("1 - Listar Contas")
        print("2 - Listar Clientes")
        print("0 - Finalizar sistema")