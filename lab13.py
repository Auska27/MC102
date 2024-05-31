import sys
sys.setrecursionlimit(999999999)


class Imagem:
    """Quarda as informações da imagem, e muda a imagem de acordo com cada função"""
    def __init__(self, tipo: str, info_imagem: str, formato_matriz: tuple,
                 maximo_pixels: int, matriz_imagem: list) -> None:
        self.tipo = tipo
        self.info_imagem = info_imagem
        self.formato_matriz = formato_matriz
        self.maximo_pixels = maximo_pixels
        self.matriz_imagem = matriz_imagem

    def info_arquivo_imagem(self, arquivo) -> None:
        """Organiza as informações obtidas pelo arquivo"""
        numero_linha = 1
        for linha in arquivo:
            if numero_linha == 2:
                self.info_imagem = linha
            if numero_linha == 3:
                colunas, linhas = linha.split()
                self.formato_matriz = (int(linhas), int(colunas))
            if numero_linha == 4:
                self.maximo_pixels = int(linha)
            if numero_linha > 4:
                self.matriz_imagem.append(linha.split())
            numero_linha += 1

    def buket_recursivo(self, nova_cor: str, liminar_tolerancia: int, pixel_semente: int,
                        linha: int, coluna: int, matriz_mudou: list[list[str]]) -> None:
        """Por meio da região semente vai mudando a str para uma nova,
           e chama novamente a função para olhar ao aredor
           e ver se é pra pintar também ou não"""
        if 0 <= linha < len(self.matriz_imagem) and 0 <= coluna < len(self.matriz_imagem[0]):
            if self.matriz_imagem[linha][coluna] == nova_cor or matriz_mudou[linha][coluna] == "mudou":
                return
            matriz_mudou[linha][coluna] = "mudou"
            if abs(int(self.matriz_imagem[linha][coluna]) - pixel_semente) <= liminar_tolerancia:
                self.matriz_imagem[linha][coluna] = nova_cor
                for linha_arredor in range(linha - 1, linha + 2):
                    for coluna_arredor in range(coluna - 1, coluna + 2):
                        self.buket_recursivo(nova_cor, liminar_tolerancia,
                                             pixel_semente, linha_arredor, coluna_arredor, matriz_mudou)
        return

    def buket(self, comando: list, matriz_mudou: list[list]) -> None:
        """Organiza as informações para conseguir chamar recursivamente a função"""
        self.buket_recursivo(comando[0], int(comando[1]),
                             int(self.matriz_imagem[int(comando[3])][int(comando[2])]),
                             int(comando[3]), int(comando[2]), matriz_mudou)

    def negative_recursivo(self, liminar_tolerancia: int,
                           pixel_semente: int, linha: int, coluna: int,
                           matriz_mudou: list[list[str]]) -> list[list[str]]:
        """Inverter as cores das regiões conexas a uma região semente,
           ao primeiro mudar da posição que deu e olhar se aoredor dessa
           posição tambem vai precisar mudar ao chamar recursivamente
           a função para olhar na nova posição"""
        if 0 <= linha < len(self.matriz_imagem) and 0 <= coluna < len(self.matriz_imagem[0]):
            if matriz_mudou[linha][coluna] == "mudou":
                return self.matriz_imagem
            matriz_mudou[linha][coluna] = "mudou"
            if abs(int(self.matriz_imagem[linha][coluna]) - pixel_semente) <= liminar_tolerancia:
                self.matriz_imagem[linha][coluna] = str(self.maximo_pixels - int(self.matriz_imagem[linha][coluna]))
                for linha_arredor in range(linha - 1, linha + 2):
                    for coluna_arredor in range(coluna - 1, coluna + 2):
                        self.matriz_imagem = self.negative_recursivo(liminar_tolerancia, pixel_semente,
                                                                     linha_arredor, coluna_arredor, matriz_mudou)

        return self.matriz_imagem

    def negative(self, comando: list, matriz_mudou: list[list]) -> None:
        """"Organiza as informações recebidas para conseguir chamar
            a função negative_recursivo de maneira recursiva"""
        self.matriz_imagem = self.negative_recursivo(int(comando[0]), int(self.matriz_imagem[int(comando[2])][int(comando[1])]),
                                                     int(comando[2]), int(comando[1]), matriz_mudou)

    def cmask_recursivo_inicio(self, liminar_tolerancia: int, pixel_semente: int,
                               linha: int, coluna: int, matriz_mudou: list[list]):
        """Retornar uma matriz contendo 0 nos píxeis pertencentes a região
           conexa contendo o píxel semente."""
        if 0 <= linha < len(self.matriz_imagem) and 0 <= coluna < len(self.matriz_imagem[linha]):
            if matriz_mudou[linha][coluna] == "mudou":
                return self.matriz_imagem, matriz_mudou

            if abs(int(self.matriz_imagem[linha][coluna]) - pixel_semente) <= liminar_tolerancia:
                self.matriz_imagem[linha][coluna] = "0"
                matriz_mudou[linha][coluna] = "mudou"
                for linha_arredor in range(linha - 1, linha + 2):
                    for coluna_arredor in range(coluna - 1, coluna + 2):
                        self.matriz_imagem, matriz_mudou = self.cmask_recursivo_inicio(liminar_tolerancia, pixel_semente,
                                                                                       linha_arredor, coluna_arredor,
                                                                                       matriz_mudou)
        return self.matriz_imagem, matriz_mudou

    def cmask_final(self, matriz_mudou: list[list]):
        """Muda o resto na imagem que não faz parte da região conexa para ficar com o valor 255"""
        for linha in range(0, len(self.matriz_imagem)):
            for coluna in range(0, len(self.matriz_imagem[linha])):
                if matriz_mudou[linha][coluna] == "não mudou":
                    self.matriz_imagem[linha][coluna] = "255"

        return self.matriz_imagem

    def cmask(self, comando: list, matriz_mudou: list) -> None:
        """Organiza as informações recebidas para conseguir
           chama recursivamente a função cmask_recursivo"""
        # Dividi o meu cmask em duas partes primeiro para poder mudar a região semente, depois mudo o resto
        self.matriz_imagem, matriz_mudou = self.cmask_recursivo_inicio(int(comando[0]), int(self.matriz_imagem[int(comando[2])][int(comando[1])]),
                                                                       int(comando[2]), int(comando[1]), matriz_mudou)
        self.matriz_imagem = self.cmask_final(matriz_mudou)

    def save(self) -> None:
        "Printa as informações da imagem"
        print(self.tipo)
        print("# Imagem criada pelo lab13")
        print("{} {}".format(self.formato_matriz[1], self.formato_matriz[0]))
        print(self.maximo_pixels)
        for i in range(self.formato_matriz[0]):
            print(" ".join(self.matriz_imagem[i]))
        return

    def criar_matriz_mudou(self) -> list[list]:
        """Crio uma matriz que evita o codigo ser chamando numa
           posição que já foi chamada"""
        matriz_mudou = []
        for i in range(len(self.matriz_imagem)):
            linha = []
            for x in range(len(self.matriz_imagem[0])):
                linha.append("não mudou")
            matriz_mudou.append(linha)
        return matriz_mudou


def chamar_função(imagem: Imagem, n: int):
    """Chama as funções para mudar a imagem"""
    for i in range(n):
        comando = input().split()
        if comando[0] == "bucket":
            matriz_mudou = imagem.criar_matriz_mudou()
            imagem.buket(comando[1:], matriz_mudou)
        elif comando[0] == "cmask":
            matriz_mudou = imagem.criar_matriz_mudou()
            imagem.cmask(comando[1:], matriz_mudou)
        elif comando[0] == "negative":
            matriz_mudou = imagem.criar_matriz_mudou()
            imagem.negative(comando[1:], matriz_mudou)
        elif comando[0] == "save":
            imagem.save()


def main():
    """Recebe arquivo, abre ele e organiza as informações,
       e chama as funções"""
    nome_arquivo = input()
    arquivo = open(nome_arquivo)
    imagem = Imagem("P2", 0, (0, 0), 0, [])
    imagem.info_arquivo_imagem(arquivo)
    arquivo.close()
    n = int(input())
    chamar_função(imagem, n)


if __name__ == "__main__":
    main()
