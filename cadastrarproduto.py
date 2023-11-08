

def cadastrarproduto ():

        nome = input("Nome : ")
        valor = input("Valor: ")
        quantidade = input("Quantidade: ")
        tipo = input("Tipo: ")
        data = input("Data: ")

        sub_produto = {
                "nome": nome,
                "valor": valor,
                "quantidade": quantidade,
                "tipo": tipo,
                "data": data,
        }
        return sub_produto

produto_cad = cadastrarproduto ()
print("Produto",produto_cad )
