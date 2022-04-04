from antlr4 import *
from dist.WebserviceGenVisitor import WebserviceGenVisitor
from dist.WebserviceGenParser import WebserviceGenParser

class VisitanteGerador(WebserviceGenVisitor):

    saida = ''
    
    # Visit a parse tree produced by WebserviceGenParser#programa.
    def visitPrograma(self, ctx:WebserviceGenParser.ProgramaContext):
        self.saida += 'from fastapi import FastAPI\n'
        self.saida += 'app = FastAPI()\n\n'
        self.visitChildren(ctx)


    # Visit a parse tree produced by WebserviceGenParser#servico.
    def visitServico(self, ctx:WebserviceGenParser.ServicoContext):
        atributosOut = []
        mapInicializacaoOut = {'str': "''", 'int': '0', 'float': '0.0'}
        prefixoOut = 'out_'

        nome = ctx.IDENT().getText()
        self.saida += '@app.get("/%s/")\n' % nome
        self.saida += 'async def %s(' % nome
        for atributo in ctx.linhaatributo():
            tipoAtributo = atributo.TIPO_ATR().getText()
            tipoValor = atributo.TIPO_VAR().getText()
            nomeAtributo = atributo.IDENT().getText()            
            if tipoAtributo == 'in':
                self.saida += '%s: %s, ' % (nomeAtributo, tipoValor)
            else:
                atributosOut.append([nomeAtributo, tipoValor])

        self.saida = self.saida.strip(', ')
        self.saida += '):\n'

        for atributo in atributosOut:
            self.saida += '    '+ prefixoOut + atributo[0] + ' = ' + mapInicializacaoOut[atributo[1]] + '\n'

        self.saida += '\n'
        self.saida += '    return {'

        for atributo in atributosOut:
            self.saida += '"%s": %s, ' % (atributo[0], prefixoOut + atributo[0])

        self.saida = self.saida.strip(', ')
        self.saida += '}\n\n'