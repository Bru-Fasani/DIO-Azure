# Lê a entrada do usuário
entrada = input()

# Função que retorna a descrição do benefício
def descrever_beneficio(beneficio):
    if beneficio == "Escalabilidade":
        return "Cresce ou reduz conforme necessidade"
    elif beneficio == "Alta Disponibilidade":
        return "Disponível quase sempre"
    elif beneficio == "Custo sob demanda":
        return "Paga apenas pelo que usar"
    elif beneficio == "Acesso global":
        return "Acesso de qualquer lugar"
    else:
        return "Benefício desconhecido"

# Imprime a descrição correspondente
print(descrever_beneficio(entrada))
