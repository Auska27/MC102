class Personagem:
    """Armazenar as ingformações do personegem"""
    def __init__(self, nome: str, vida: int, dano: int,
                 posição: tuple, saida: tuple) -> None:
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.posição = posição
        self.saida = saida


class Monstro:
    """Armazena as informações da monstro"""
    def __init__(self, nome_monstro: int, pontos_vida: int,
                 pontos_ataque: int, tipo: str, posição: tuple) -> None:
        self.nome_monstro = nome_monstro
        self.pontos_vida = pontos_vida
        self.pontos_ataque = pontos_ataque
        self.tipo = tipo
        self.posição = posição

    def movimentação_monstro(self, matriz_dungeon):
        """Movimenta o monstro dependendo do tipo dele"""
        if self.pontos_vida > 0:
            if self.tipo == "U":
                x, y = self.posição
                if x > 0:
                    matriz_dungeon[x][y] = "."
                    matriz_dungeon[x - 1][y] = "U"
                    self.posição = (x - 1, y)
            elif self.tipo == "D":
                x, y = self.posição
                if x < len(matriz_dungeon) - 1:
                    matriz_dungeon[x][y] = "."
                    matriz_dungeon[x + 1][y] = "D"
                    self.posição = (x + 1, y)
            elif self.tipo == "L":
                x, y = self.posição
                if y > 0:
                    matriz_dungeon[x][y] = "."
                    matriz_dungeon[x][y - 1] = "L"
                    self.posição = (x, y - 1)
            elif self.tipo == "R":
                x, y = self.posição
                if y < len(matriz_dungeon[0]) - 1:
                    matriz_dungeon[x][y] = "."
                    matriz_dungeon[x][y + 1] = "R"
                    self.posição = (x, y + 1)
        return matriz_dungeon


class Objeto:
    """Armazenar as informações do objeto"""
    def __init__(self, nome: str, tipo: str, posição: tuple,
                 status: int, situação: str) -> None:
        self.nome = nome
        self.tipo = tipo
        self.posição = posição
        self.status = status
        self.situação = situação


def criar_mostro(quantidade_monstros: int) -> list[Monstro]:
    """Recebe os inputs sobre os monstros e organiza"""
    list_monstros = []
    for numero_monstro in range(quantidade_monstros):
        info_monstro = input().split(" ")
        monstro = Monstro(numero_monstro, int(info_monstro[0]), int(info_monstro[1]),
                          info_monstro[2], tuple([int(info_monstro[3][0]), int(info_monstro[3][2])]))
        list_monstros.append(monstro)
    return list_monstros


def criar_objetos(quantidade_objetos: int) -> list[Objeto]:
    """Recebe os inputs sobre os objetos e organiza"""
    list_objetos = []
    for numero_objeto in range(quantidade_objetos):
        info_objetos = input().split(" ")
        x_objeto = int(info_objetos[2][0])
        y_objeto = int(info_objetos[2][2])
        objeto = Objeto(info_objetos[0], info_objetos[1],
                        tuple([x_objeto, y_objeto]), int(info_objetos[3]),
                        "não pego")
        list_objetos.append(objeto)
    return list_objetos


def organizar_matriz(matriz_dungeon: list, list_monstros: list[Monstro],
                     list_objetos: list[Objeto], link: Personagem,
                     numero_linhas=0, numero_colunas=0) -> list[list]:
    """Depois de receber os parametros da matriz,
       organiza as informações em um lista de listas"""
    if matriz_dungeon == []:
        for linha in range(int(numero_linhas)):
            lista_linha = []
            for c in range(int(numero_colunas)):
                lista_linha.append(".")
            matriz_dungeon.append(lista_linha)
    x_personagem, y_perosnagem = link.posição
    x_saida, y_saida = link.saida
    for objeto in list_objetos:
        if objeto.situação == "não pego":
            x_objeto, y_objeto = objeto.posição
            matriz_dungeon[x_objeto][y_objeto] = objeto.tipo
    for monstro in list_monstros:
        if monstro.pontos_vida > 0:
            x_monstro, y_monstro = monstro.posição
            matriz_dungeon[x_monstro][y_monstro] = monstro.tipo
    matriz_dungeon[x_saida][y_saida] = "*"
    matriz_dungeon[x_personagem][y_perosnagem] = "P"
    return matriz_dungeon


def movimentação_inicial(matriz_dungeon: list[list], list_monstros: list[Monstro],
                         link: Personagem, list_objetos: list[Objeto], vezes_movimentação) -> list[list]:
    """Inincialmente o personagem só pode se mover em direção a ultima linha"""
    while vezes_movimentação > 0 and link.vida > 0:
        for monstro in list_monstros:
            matriz_dungeon = monstro.movimentação_monstro(matriz_dungeon)
        x_personagem, y_perosnagem = link.posição
        link.posição = (x_personagem + 1, y_perosnagem)
        matriz_dungeon[x_personagem][y_perosnagem] = "."
        matriz_dungeon[x_personagem + 1][y_perosnagem] = "P"
        matriz_dungeon = organizar_matriz(matriz_dungeon, list_monstros,
                                          list_objetos, link)
        vezes_movimentação -= 1
        batalha(matriz_dungeon, list_monstros, link, list_objetos)
    return matriz_dungeon


def movimentação(matriz_dungeon: list[list], list_monstros: list[Monstro],
                 link: Personagem, list_objetos: list[Objeto]) -> list[list]:
    """Depois do personagem se mover para a ultima linha da dungeon,
        ele começa a se movimentar para os lados"""
    while True:
        if link.posição == link.saida:
            print("Chegou ao fim!")
            break
        elif link.vida == 0:
            break
        else:
            x_personagem, y = link.posição
            if x_personagem % 2 == 0:
                if y == 0:
                    link.posição = (x_personagem - 1, y)
                    matriz_dungeon[x_personagem - 1][y] = "P"
                    matriz_dungeon[x_personagem][y] = "."
                else:
                    link.posição = (x_personagem, y - 1)
                    matriz_dungeon[x_personagem][y - 1] = "P"
                    matriz_dungeon[x_personagem][y] = "."
            else:
                if y + 1 == len(matriz_dungeon[0]):
                    link.posição = (x_personagem - 1, y)
                    matriz_dungeon[x_personagem - 1][y] = "P"
                    matriz_dungeon[x_personagem][y] = "."
                else:
                    link.posição = (x_personagem, y + 1)
                    matriz_dungeon[x_personagem][y + 1] = "P"
                    matriz_dungeon[x_personagem][y] = "."
            for monstro in list_monstros:
                matriz_dungeon = monstro.movimentação_monstro(matriz_dungeon)
            matriz_dungeon = organizar_matriz(matriz_dungeon, list_monstros,
                                              list_objetos, link)
            batalha(matriz_dungeon, list_monstros, link, list_objetos)
    return matriz_dungeon


def batalha(matriz_dugeon, list_monstros: list[Monstro],
            link: Personagem, list_objetos: list[Objeto]) -> list[list]:
    """Depois do persongem e dos monstros se mecherem, verifica
       se o persongem pega algum objeto e se ele entra em um combate"""
    x_personagem, y_personagem = link.posição
    objetos_pegos = {}
    dano_dado = {}
    dano_recebidao = {}
    if link.posição == link.saida:
        print_info(matriz_dugeon,  objetos_pegos, dano_dado, dano_recebidao)
        return matriz_dugeon
    for objeto in list_objetos:
        if objeto.posição == link.posição and objeto.situação == "não pego":
            if objeto.tipo == "v":
                link.vida += objeto.status
                matriz_dugeon[x_personagem][y_personagem] = "P"
                objetos_pegos[objeto.nome] = (objeto.tipo, objeto.status)
                objeto.situação = "pego"
                if link.vida <= 0:
                    link.vida = 0
                    matriz_dugeon[x_personagem][y_personagem] = "X"
                    print_info(matriz_dugeon, objetos_pegos, dano_dado, dano_recebidao)
                    return matriz_dugeon
            elif objeto.tipo == "d" and objeto.situação == "não pego":
                link.dano += objeto.status
                if link.dano <= 0:
                    link.dano = 1
                matriz_dugeon[x_personagem][y_personagem] = "P"
                objetos_pegos[objeto.nome] = (objeto.tipo, objeto.status)
                objeto.situação = "pego"
    for monstro in list_monstros:
        if monstro.posição == link.posição and monstro.pontos_vida > 0:
            dano_link = link.dano
            if link.dano > monstro.pontos_vida:
                dano_link = monstro.pontos_vida
            monstro.pontos_vida -= dano_link
            matriz_dugeon[x_personagem][y_personagem] = "P"
            dano_dado[monstro] = (link.posição, dano_link)
            if monstro.pontos_vida > 0:
                dano_monstro = monstro.pontos_ataque
                if monstro.pontos_ataque > link.vida:
                    dano_monstro = link.vida
                link.vida -= dano_monstro
                dano_recebidao[monstro] = (dano_monstro, link.vida)
                if link.vida <= 0:
                    matriz_dugeon[x_personagem][y_personagem] = "X"
                    print_info(matriz_dugeon, objetos_pegos, dano_dado, dano_recebidao)
                    return matriz_dugeon
    print_info(matriz_dugeon, objetos_pegos, dano_dado, dano_recebidao)
    return matriz_dugeon


def print_info(matriz_dugeon: list[list], objetos_pegos: dict,
               dano_dado: dict, dano_recebidao: dict) -> None:
    """Mostra na tela se o personagem deu dano e se ele sofreu dano,
       alem de sempre mostra qual a situação da dungeon"""
    if len(objetos_pegos) > 0:
        for objeto, info_objeto in objetos_pegos.items():
            print("[{}]Personagem adquiriu o objeto {} com status de {}".format(info_objeto[0], objeto, info_objeto[1]))
    if len(dano_dado) > 0:
        for monstro, info_dano in dano_dado.items():
            print("O Personagem deu {} de dano ao monstro na posicao {}".format(info_dano[1], info_dano[0]))
            if monstro in dano_recebidao.keys():
                dano, vida = dano_recebidao[monstro]
                print("O Monstro deu {} de dano ao Personagem. Vida restante = {}".format(dano, vida))

    for linha in matriz_dugeon:
        print(" ".join(linha))
    print()


def main() -> None:
    """Recebe os inputs e cria variaveis necessarias para chamar as funções"""
    vida, dano = input().split(" ")
    numero_linhas, numero_colunas = input().split(" ")
    posição_per_linha, posição_per_coluna = input().split(",")
    saida_linha, saida_coluna = input().split(",")
    link = Personagem("Link", int(vida), int(dano), (int(posição_per_linha), int(posição_per_coluna)),
                      (int(saida_linha), int(saida_coluna)))
    vezes_movimento_inicial = int(numero_linhas) - (int(posição_per_linha) + 1)
    # A variavel vezes_movimento_inicial é pra saber quantas vezes vou precisar
    # executar o laço da função movimentação_inicial até quebrar a maldição inicial.
    quantidade_monstros = int(input())
    list_monstros = criar_mostro(quantidade_monstros)
    quantidade_objetos = int(input())
    list_objetos = criar_objetos(quantidade_objetos)
    matriz_dungeon = []
    matriz_dungeon = organizar_matriz(matriz_dungeon, list_monstros,
                                      list_objetos, link, numero_linhas, numero_colunas)
    print_info(matriz_dungeon, {}, {}, {})
    matriz_dungeon = movimentação_inicial(matriz_dungeon, list_monstros, link,
                                          list_objetos, vezes_movimento_inicial)
    matriz_dungeon = movimentação(matriz_dungeon, list_monstros, link, list_objetos)


if __name__ == "__main__":
    main()
