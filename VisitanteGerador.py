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
        atributosInPath = []
        mapInicializacaoOut = {'str': "''", 'int': '0', 'float': '0.0'}
        prefixoOut = 'out_'

        nome = ctx.IDENT().getText()
        tipoHttp = 'get'
        if ctx.TIPO_HTTP() != None:
            tipoHttp = ctx.TIPO_HTTP().getText()

        #pathServico = '@app.%s("/%s/")\n' % (tipoHttp, nome)
        self.saida += '***TROCAR_DEPOIS***'
        self.saida += 'async def %s(' % nome
        for atributo in ctx.linhaatributo():
            tipoAtributo = atributo.TIPO_ATR().getText()
            tipoValor = atributo.TIPO_VAR().getText()
            nomeAtributo = atributo.IDENT().getText()
            tipoIn = atributo.TIPO_ATR_IN() 
            if tipoAtributo == 'in':
                self.saida += '%s: %s, ' % (nomeAtributo, tipoValor)
                if tipoIn != None and tipoIn.getText() == 'path':
                    atributosInPath.append(nomeAtributo)
            else:
                atributosOut.append([nomeAtributo, tipoValor])

        linhaAtrsPath = ''
        
        for atrPath in atributosInPath:
            linhaAtrsPath += '{%s}/' % atrPath

        pathServico = '@app.%s("/%s/%s")\n' % (tipoHttp, nome, linhaAtrsPath)
        self.saida = self.saida.replace('***TROCAR_DEPOIS***', pathServico)

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