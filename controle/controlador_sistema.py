from limite.tela_sistema import TelaSistema
from controle.controlador_pessoa import ControladorPessoa
from controle.controlador_conta import ControladorConta
from controle.controlador_operacao import ControladorOperacao

class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_conta = ControladorConta(self)
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_operacao = ControladorOperacao(self)

    @property
    def controlador_conta(self):
        return self.__controlador_conta

    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa

    @property
    def controlador_operacao(self):
        return self.__controlador_operacao

    def inicializa_sistema(self):
        self.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def gerenciar_cadastros(self):
        self.abre_tela_cadastros()

    def realizar_operacoes(self):
        self.__controlador_conta.realizar_operacoes()

    def listar_clientes(self):
        self.__controlador_pessoa.listar_clientes()

    def listar_contas(self):
        self.__controlador_conta.listar_contas()

    def valida_e_executa_funcao(self, opcao_escolhida, lista_opcoes):
        if opcao_escolhida != None:
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            self.__tela_sistema.close()
            funcao_escolhida()
        else:
            exit(0)

    def exibe_area_funcionarios(self):
        senha_funcionario = self.__tela_sistema.pega_senha_funcionario()
        valida_senha, funcionario = self.__controlador_pessoa.valida_senha_funcionario(senha_funcionario)
        if valida_senha:
            lista_opcoes = {1: self.listar_contas, 2: self.listar_clientes,
                            0: self.abre_tela}

            while True:
                opcao_escolhida = self.__tela_sistema.area_funcionarios(funcionario.nome)
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
        else:
            self.__tela_sistema.mostra_mensagem("\nATENÇÃO: Senha incorreta!")

    def abre_tela(self):
        lista_opcoes = {1: self.gerenciar_cadastros, 2: self.realizar_operacoes, 3: self.exibe_area_funcionarios,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.exibe_menu_sistema()
            self.valida_e_executa_funcao(opcao_escolhida, lista_opcoes)

    def gerenciar_pessoas(self):
        self.__controlador_pessoa.abre_tela()

    def gerenciar_contas(self):
        self.__controlador_conta.abre_tela()

    def retorno_menu(self):
        self.abre_tela()

    def abre_tela_cadastros(self):
        lista_opcoes = {1: self.gerenciar_pessoas, 2: self.gerenciar_contas,
                        0: self.retorno_menu}

        while True:
            opcao_escolhida = self.__tela_sistema.exibe_menu_cadastros()
            self.valida_e_executa_funcao(opcao_escolhida, lista_opcoes)
