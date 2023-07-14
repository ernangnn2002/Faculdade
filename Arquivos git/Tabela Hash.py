#basicamente a ideia dessa implementação é verificar do total que compoe a idade, quantos são homens e quantos são mulheres

import os

def cria_hash(caminho_arquivo):
    tabela_hash = {}  
    with open(caminho_arquivo) as f:
        for linha in f:            
            idade, total, total_homens, total_mulheres = linha.strip().split(',')                       
            idade = int(idade)
            total = int(total)
            total_homens = int(total_homens)
            total_mulheres = int(total_mulheres)
            tabela_hash[idade] = (total, total_homens, total_mulheres)

    return tabela_hash

def menu_busca(tabela_hash):
    while True:
        opcao = input('Digite a idade(entre 0 e 79 anos) que deseja pesquisar ou "sair" para finalizar: ')
        if opcao.lower() == 'sair':
            break
        else:
            idade = int(opcao)
            if idade in tabela_hash:
                total, homens, mulheres = tabela_hash[idade]
                print(f'Idade: {idade}, Total: {total}, Total Homens: {homens}, Total Mulheres: {mulheres}')
            else:
                print(f'Nenhum registro encontrado para a idade {idade}')


caminho_arquivo = os.path.join('C:\\', 'Users', 'windows10', 'Documents', 'Faculdade', 'Pesquisa e Ordenação', 'idades_sc.txt') #define o caminho do arquivo

tabela_hash = cria_hash(caminho_arquivo)
menu_busca(tabela_hash)