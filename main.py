from antlr4 import *
from dist.WebserviceGenLexer import WebserviceGenLexer
from dist.WebserviceGenParser import WebserviceGenParser
from Visitante import Visitante

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
    visitante = Visitante()
    visitante.visitPrograma(tree)