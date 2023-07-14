import os


class Registro:
    def __init__(self, cidade, populacao):
        self.cidade = cidade
        self.populacao = populacao


class No:
    def __init__(self, registro):
        self.registro = registro
        self.esquerda = None
        self.direita = None
        self.altura = 1


class AVLTree:
    def __init__(self):
        self.raiz = None

    def insert(self, registro):
        self.raiz = self._insert(self.raiz, registro)

    def _insert(self, no, registro):
        if not no:
            return No(registro)

        if registro.cidade < no.registro.cidade:
            no.esquerda = self._insert(no.esquerda, registro)
        else:
            no.direita = self._insert(no.direita, registro)

        no.altura = 1 + max(self.getAltura(no.esquerda), self.getAltura(no.direita))

        fatorBalanca = self.getFatorBalanceamento(no)

        if fatorBalanca > 1:
            if registro.cidade < no.esquerda.registro.cidade:
                return self.rotacionaDireita(no)
            else:
                no.esquerda = self.rotacionaEsquerda(no.esquerda)
                return self.rotacionaDireita(no)

        if fatorBalanca < -1:
            if registro.cidade > no.direita.registro.cidade:
                return self.rotacionaEsquerda(no)
            else:
                no.direita = self.rotacionaDireita(no.direita)
                return self.rotacionaEsquerda(no)

        return no

    def busca_cidade(self, cidade):
        return self._busca_cidade(self.raiz, cidade)

    def _busca_cidade(self, no, cidade):
        if not no or no.registro.cidade == cidade:
            return no

        if cidade < no.registro.cidade:
            return self._busca_cidade(no.esquerda, cidade)
        else:
            return self._busca_cidade(no.direita, cidade)

    def getAltura(self, no):
        if not no:
            return 0
        return no.altura

    def getFatorBalanceamento(self, no):
        if not no:
            return 0
        return self.getAltura(no.esquerda) - self.getAltura(no.direita)

    def rotacionaEsquerda(self, z):
        y = z.direita
        T2 = y.esquerda

        y.esquerda = z
        z.direita = T2

        z.altura = 1 + max(self.getAltura(z.esquerda), self.getAltura(z.direita))
        y.altura = 1 + max(self.getAltura(y.esquerda), self.getAltura(y.direita))

        return y

    def rotacionaDireita(self, z):
        y = z.esquerda
        T3 = y.direita

        y.direita = z
        z.esquerda = T3

        z.altura = 1 + max(self.getAltura(z.esquerda), self.getAltura(z.direita))
        y.altura = 1 + max(self.getAltura(y.esquerda), self.getAltura(y.direita))

        return y


def le_arquivo(caminho_arquivo):
    registros = []
    with open(caminho_arquivo, 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            campos = linha.strip().split(',')
            cidade = campos[0]
            populacao = int(campos[1])
            registros.append(Registro(cidade, populacao))
    return registros


caminho_arquivo = os.path.join('C:\\', 'Users', 'windows10', 'Documents', 'Faculdade', 'Pesquisa e Ordenação', 'sc.txt')
registros = le_arquivo(caminho_arquivo)

arvore = AVLTree()
for registro in registros:
    arvore.insert(registro)

while True:
    cidade_busca = input('Digite o nome da cidade ou "sair": ')
    if cidade_busca.lower() == 'sair':
        break

    resultado_busca = arvore.busca_cidade(cidade_busca)
    if resultado_busca:
        print('Cidade:', resultado_busca.registro.cidade, '| População:', resultado_busca.registro.populacao)
    else:
        print("Cidade não encontrada na base de dados")
