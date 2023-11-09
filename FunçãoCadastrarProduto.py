#IMPORTANDO MODULO DE DATA
import datetime as data
#IMPORTANDO MODULO DE ALEATORIDADE
import random
#FUNÇÃO PRA GERAR CODIGO ALEATORIO
def codigo_aleatorio():
    codigo = ''.join(random.choice('ZXCWYKLMHP0123456789') for _ in range(4))
    return codigo

#CRIANDO A FUNÇÃO PARA CADASTRAR PRODUTO
def cadastrarproduto ():
        #RECEBENDO VARIAVEIS DO DICIONARIO QUE VAI SER ALOCADO NA LISTA DE PRODUTOS
        codigo = codigo_aleatorio()
        nome = input("\nNome: ")
        valor = float(input("Valor: "))
        quantidade = input("Quantidade: ")
        tipo = input("Tipo: ")
        data_atual = data.datetime.now()

        #FORMATANDO DATA PARA RECEBER APENAS DIAS/MESES/ANOS HORAS/MINUTOS
        data_formatada = data_atual.strftime( "%d/%m/%Y %H:%M" )

        #CRIANDO DICIONARIO sub_produto
        sub_produto = {
                "codigo": codigo,
                "nome": nome,
                "valor": valor,
                "quantidade": quantidade,
                "tipo": tipo,
                "data": data_formatada,

        }
        #retorno da função, o dicionario
        return sub_produto


#ALOCANDO O RETORNO DA FUNÇAO A UMA VARIAVEL QUE SERA USADA PARA IMPRIMIR EM UM ARQUIVO
produto_cad = cadastrarproduto ()

#adicionar o novo produto em um arquivo txt
with open ("produto_cad.txt","a") as arquivo:
        # A para adicionar em um arquivo existente
        produto_cad_str = f"{produto_cad['codigo']}     {produto_cad['nome']}       {produto_cad['valor']}      {produto_cad['quantidade']}     {produto_cad['tipo']}   {produto_cad['data']}\n"

        arquivo.write(produto_cad_str)
#RETORNO PARA VER COMO FOI ALOCADO NO ARQUIVO DE TEXTO
print("Produto",produto_cad )
print("\nProduto: ",produto_cad_str )

