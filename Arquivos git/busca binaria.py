import os

caminho_arquivo = os.path.join('C:\\', 'Users', 'windows10', 'Documents', 'Faculdade', 'Pesquisa e Ordenação', 'sc.txt')

cidades = []
with open(caminho_arquivo, 'r', encoding="utf-8") as arquivo:
    for linha in arquivo:
        cidade, populacao = linha.strip().split(',')
        cidades.append((cidade, int(populacao)))


# Implementação da função de busca binária.
def busca_binaria(lista, cidade):
    baixo = 0
    alto = len(lista) - 1 #tamanho da lista
    
    while baixo <= alto:
        meio = (baixo + alto) // 2
        pivo = lista[meio] #particiona a lista pelo meio 
        
        if pivo[0] == cidade:
            return lista[meio] 
        if pivo[0] > cidade:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


# neste trecho se eu digito sair o programa não para, ele simplesmente continua. como corrigir?
while True:
    cidadeBusca = input('Digite o nome da cidade ou "sair": ')
    if(cidadeBusca.lower() == 'sair'):
        break

    resultadoBusca = busca_binaria(cidades, cidadeBusca)
    if (resultadoBusca):            
        print('Cidade:', resultadoBusca[0], '| População:', resultadoBusca[1])
    else:
        print("Cidade nao encontrada na base de dados")
        