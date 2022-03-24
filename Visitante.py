from antlr4 import *
from dist.WebserviceGenVisitor import WebserviceGenVisitor
from dist.WebserviceGenParser import WebserviceGenParser


class TabelaServico:

    listaServicos = []

    def adicionarServico(self, nome):
        self.listaServicos.append(TabelaAtributo(nome))

    def obterServico(self, nome):
        for serv in self.listaServicos:
            if serv.nomeServico == nome:
                return serv
        
        return None          

    def existeServico(self, nome):
        servico = self.obterServico(nome)
        return (servico != None)


class EntradaAtributo:

    def __init__(self, nome, tipoAtr, tipoVar):
        self.nome = nome
        self.tipoAtr = tipoAtr
        self.tipoVar = tipoVar


class TabelaAtributo: #serviço

    listaAtributos = []

    def __init__(self, nomeServico):
        self.nomeServico = nomeServico

    def adicionarEntrada(self, nome, tipoAtr, tipoVar):
        self.listaAtributos.append(EntradaAtributo(nome, tipoAtr, tipoVar))

    def existeAtributo(self, nome, tipoAtr):
        for entrada in self.listaAtributos:
            if entrada.nome == nome and entrada.tipoAtr == tipoAtr:
                return True

        return False


class Visitante(WebserviceGenVisitor):

    servicos = TabelaServico()
    
    # Visit a parse tree produced by WebserviceGenParser#programa.
    def visitPrograma(self, ctx:WebserviceGenParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebserviceGenParser#servico.
    def visitServico(self, ctx:WebserviceGenParser.ServicoContext):
        nome = ctx.IDENT().getText()
        if self.servicos.existeServico(nome):
            raise Exception('Erro semantico: nome de serviço duplicado: ' + nome)
        else:
            self.servicos.adicionarServico(nome)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebserviceGenParser#linhaatributo.
    def visitLinhaatributo(self, ctx:WebserviceGenParser.LinhaatributoContext):

        servico = self.servicos.obterServico(ctx.parentCtx.IDENT().getText())
        nomeAtributo = ctx.IDENT().getText()
        tipoAtributo = ctx.TIPO_ATR().getText()
        tipoValor = ctx.TIPO_VAR().getText()

        if (servico.existeAtributo(nomeAtributo, tipoAtributo)):
            raise Exception('Erro semantico: atributo %s:%s duplicado para o serviço %s' % (nomeAtributo, tipoAtributo, servico.nomeServico))
        else:
            servico.adicionarEntrada(nomeAtributo, tipoAtributo, tipoValor)

        return self.visitChildren(ctx)