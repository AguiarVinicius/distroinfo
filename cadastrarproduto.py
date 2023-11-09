
def cadastrarproduto ():

        nome = input("Nome: ")
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

#adicionar o novo produto em um arquivo txt
with open ("produto_cad.txt","a") as arquivo:
        # Use "a" para adicionar ao arquivo existente
        produto_cad_str = f"{produto_cad['nome']},{produto_cad['valor']},{produto_cad['quantidade']},{produto_cad['tipo']},{produto_cad['data']}\n"

        arquivo.write(produto_cad_str)

print("Produto",produto_cad )

