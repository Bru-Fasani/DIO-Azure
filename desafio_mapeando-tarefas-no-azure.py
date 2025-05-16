# Lê a entrada do usuário
entrada = input()

# Função que retorna o recurso correspondente à tarefa
def identificar_recurso(tarefa):
    if tarefa == "Criar um servidor com sistema operacional":
        return "Máquina Virtual"
    elif tarefa == "Guardar dados em um banco relacional":
        return "Instância de Banco de Dados"
    elif tarefa == "Explorar os serviços disponíveis":
        return "Portal Azure"
    elif tarefa == "Criar conta para acessar o Azure":
        return "Conta Microsoft e Assinatura"
    else:
        return "Tarefa desconhecida"

# Imprime o recurso correspondente
print(identificar_recurso(entrada))
