from limite.tela_pessoa import TelaPessoa
from entidade.cliente import Cliente
from entidade.funcionario import Funcionario
from datetime import datetime

class ControladorPessoa:

    def __init__(self, controlador_sistema):
        self.__clientes = []
        self.__qtde_clientes = 0
        self.__funcionarios = []
        self.__qtde_funcionarios = 0
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_sistema = controlador_sistema

    def pega_cliente_por_cpf(self, cpf:int):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def pega_funcionario_por_cpf(self, cpf:int):
        for funcionario in self.__funcionarios:
            if funcionario.cpf == cpf:
                return funcionario
        return None

    def incluir_cliente(self):
        cpf_unico = True
        self.__qtde_clientes += 1
        codigo = self.__qtde_clientes
        dados_cliente = self.__tela_pessoa.pega_dados_cliente()
        for cliente in self.__clientes:
            if cliente.cpf == dados_cliente["cpf"]:
                cpf_unico = False
        if cpf_unico:
            data_atual = datetime.now()
            quantidade_segundos = (data_atual - dados_cliente["data_nascimento"]).total_seconds()
            anos = ((((quantidade_segundos / 60) / 60) / 24) / 365)
            if anos > 18:
                cliente = Cliente(codigo, dados_cliente["nome"], dados_cliente["data_nascimento"], dados_cliente["cpf"], dados_cliente["senha_operacoes"])
                self.__clientes.append(cliente)
                self.__tela_pessoa.mostra_mensagem("Cliente cadastrado com sucesso!")
            else:
                self.__tela_pessoa.mostra_mensagem("Cliente é menor de idade, verifique!")
        else:
            self.__tela_pessoa.mostra_mensagem("O CPF já está cadastrado como cliente, por favor verifique!")

    def alterar_cliente(self):
        cpf_cliente = self.__tela_pessoa.seleciona_cpf()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)
        if (cliente is not None):
            senha_cliente = self.__tela_pessoa.pega_senha_pesoa()
            if cliente.senha_operacoes == senha_cliente:
                novos_dados_cliente = self.__tela_pessoa.pega_dados_cliente_alteracao()
                cliente.nome = novos_dados_cliente["nome"]
                cliente.senha_operacoes = novos_dados_cliente["senha_operacoes"]
                self.__tela_pessoa.mostra_mensagem("Cliente atualizado com sucesso!")
            else:
                self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Senha incorreta!")
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Cliente não existente!")

    def excluir_cliente(self):
        cpf_cliente = self.__tela_pessoa.seleciona_cpf()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)
        if (cliente is not None):
            senha_cliente = self.__tela_pessoa.pega_senha_pesoa()
            if cliente.senha_operacoes == senha_cliente:
                self.__clientes.remove(cliente)
                self.__tela_pessoa.mostra_mensagem("Cliente excluido com sucesso!")
            else:
                self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Senha incorreta!")
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Cliente não existente!")

    def lista_cliente(self):
        cpf_cliente = self.__tela_pessoa.seleciona_cpf()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)
        if (cliente is not None):
            senha_cliente = self.__tela_pessoa.pega_senha_pesoa()
            if cliente.senha_operacoes == senha_cliente:
                dados_cliente = {"codigo": cliente.codigo, "nome": cliente.nome,
                                 "data_nascimento": cliente.data_nascimento, "cpf": cliente.cpf}
                self.__tela_pessoa.lista_cliente(dados_cliente)
            else:
                self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Senha incorreta!")
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Cliente não existente!")

    def incluir_funcionario(self):
        cpf_unico = True
        self.__qtde_funcionarios += 1
        codigo = self.__qtde_funcionarios
        dados_funcionario = self.__tela_pessoa.pega_dados_funcionario()
        for funcionario in self.__funcionarios:
            if funcionario.cpf == dados_funcionario["cpf"]:
                cpf_unico = False
        if cpf_unico:
            data_atual = datetime.now()
            quantidade_segundos = (data_atual - dados_funcionario["data_nascimento"]).total_seconds()
            anos = ((((quantidade_segundos / 60) / 60) / 24) / 365)
            if anos > 18:
                funcionario = Funcionario(codigo, dados_funcionario["nome"], dados_funcionario["data_nascimento"], dados_funcionario["cpf"], dados_funcionario["numero_CTPS"], dados_funcionario["senha_funcionario"])
                self.__funcionarios.append(funcionario)
                self.__tela_pessoa.mostra_mensagem("Funcionário cadastrado com sucesso!")
        else:
            self.__tela_pessoa.mostra_mensagem("O CPF já está cadastrado como funcionário, por favor verifique!")

    def alterar_funcionario(self):
        cpf_funcionario = self.__tela_pessoa.seleciona_cpf()
        funcionario = self.pega_funcionario_por_cpf(cpf_funcionario)
        if (funcionario is not None):
            senha_funcionario = self.__tela_pessoa.pega_senha_pessoa()
            if funcionario.senha_operacoes == senha_funcionario:
                novos_dados_funcionario = self.__tela_pessoa.pega_dados_funcionario_alteracao()
                funcionario.nome = novos_dados_funcionario["nome"]
                funcionario.senha_funcionario = novos_dados_funcionario["senha_funcionario"]
                self.__tela_pessoa.mostra_mensagem("Funcionario atualizado com sucesso!")
            else:
                self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Senha incorreta!")
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Funcionário não existente!")

    def excluir_funcionario(self):
        cpf_funcionario = self.__tela_pessoa.seleciona_cpf()
        funcionario = self.pega_funcionario_por_cpf(cpf_funcionario)
        if (funcionario is not None):
            senha_funcionario = self.__tela_pessoa.pega_senha_pessoa()
            if funcionario.senha_funcionario == senha_funcionario:
                self.__funcionario.remove(funcionario)
                self.__tela_pessoa.mostra_mensagem("Funcionário excluido com sucesso!")
            else:
                self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Senha incorreta!")
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Funcionário não existente!")

    def lista_funcionario(self):
        cpf_funcionario = self.__tela_pessoa.seleciona_cpf()
        funcionario = self.pega_funcionario_por_cpf(cpf_funcionario)
        if (funcionario is not None):
            senha_funcionario = self.__tela_pessoa.pega_senha_pessoa()
            if funcionario.senha_funcionario == senha_funcionario:
                dados_funcionario = {"codigo": funcionario.codigo, "nome": funcionario.nome,
                                 "data_nascimento": funcionario.data_nascimento, "cpf": funcionario.cpf,
                                 "numero_CTPS": funcionario.numero_CTPS}
                self.__tela_pessoa.lista_funcionario(dados_funcionario)
            else:
                self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Senha incorreta!")
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Funcionário não existente!")

    def listar_clientes(self):
        print("lista clientes")
        for cliente in self.__clientes:
            dados_cliente = {"codigo":cliente.codigo, "nome": cliente.nome, "data_nascimento": cliente.data_nascimento,
                             "cpf": cliente.cpf}
            self.__tela_pessoa.lista_cliente(dados_cliente)

    def retorno_menu(self):
        self.__controlador_sistema.abre_tela_cadastros()

    def abre_tela(self):
        lista_opcoes = {1: self.abre_tela_cliente, 2: self.abre_tela_funcionario,
                        0: self.retorno_menu}

        while True:
            opcao_escolhida = self.__tela_pessoa.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def abre_tela_cliente(self):
        lista_opcoes_cliente = {1: self.incluir_cliente, 2: self.alterar_cliente,
                                3: self.excluir_cliente, 4: self.lista_cliente,
                                0: self.abre_tela}

        while True:
            opcao_escolhida = self.__tela_pessoa.tela_opcoes_gerencia('cliente')
            funcao_escolhida = lista_opcoes_cliente[opcao_escolhida]
            funcao_escolhida()

    def abre_tela_funcionario(self):
        lista_opcoes_funcionario = {1: self.incluir_funcionario, 2: self.alterar_funcionario,
                                    3: self.excluir_funcionario, 4: self.lista_funcionario,
                                    0: self.abre_tela}

        while True:
            opcao_escolhida = self.__tela_pessoa.tela_opcoes_gerencia('funcionário')
            funcao_escolhida = lista_opcoes_funcionario[opcao_escolhida]
            funcao_escolhida()