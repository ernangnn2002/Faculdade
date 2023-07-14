import os
import math

def leArquivoDados(caminhoArquivo):
    dados = []
    with open(caminhoArquivo, 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            idade, total, homens, mulheres = linha.strip().split(',')
            dados.append((int(idade), int(total), int(homens), int(mulheres)))
    return dados


def jump_search(dados, idade):
    tamanho = len(dados)
    salto = int(math.sqrt(tamanho))  # Define o tamanho do salto com base na raiz quadrada do tamanho do array de dados

    bloco_inicial = 0
    while dados[min(bloco_inicial, tamanho) - 1][0] < idade:
        bloco_inicial += salto
        if bloco_inicial >= tamanho:
            return None  # Dados não encontrados

    while dados[bloco_inicial][0] < idade:
        bloco_inicial += 1
        if bloco_inicial == min(bloco_inicial + salto, tamanho):
            return None  # Dados não encontrados

    if dados[bloco_inicial][0] == idade:
        return dados[bloco_inicial]

    return None  # Dados não encontrados


caminhoArquivo = os.path.join('C:\\', 'Users', 'windows10', 'Documents', 'Faculdade', 'Pesquisa e Ordenação', 'idades_sc.txt') #define o caminho do arquivo
dados = leArquivoDados(caminhoArquivo)

while True:
    idadeBusca = input('Digite a idade ou "sair": ')
    if idadeBusca.lower() == 'sair':
        break

    resultadoBusca = jump_search(dados, int(idadeBusca))
    if resultadoBusca:
        idade, total, homens, mulheres = resultadoBusca
        print('Idade:', idade, '| Total de População:', total, '| Homens:', homens, '| Mulheres:', mulheres)
    else:
        print("Dados não encontrados")
