from antlr4 import *
from dist.WebserviceGenLexer import WebserviceGenLexer
from dist.WebserviceGenParser import WebserviceGenParser
from Visitante import Visitante
from VisitanteGerador import VisitanteGerador

if __name__ == "__main__":
    f = open('programa.txt')
    data =  InputStream(f.read())
    f.close()
    # lexer
    lexer = WebserviceGenLexer(data)
    stream = CommonTokenStream(lexer)
    # parser
    parser = WebserviceGenParser(stream)
    tree = parser.programa()
    # visitante erro semantico
    visitante = Visitante()
    visitante.visitPrograma(tree)
    # visitante gerador de código
    gerador = VisitanteGerador()
    gerador.visitPrograma(tree)
    
    f2 = open('programagerado.py', 'w')
    f2.write(gerador.saida)
    f2.close()

