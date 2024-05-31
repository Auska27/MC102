class Jogador:
    """Guaradar as informações do jogador"""
    def __init__(self, nome: int, mão: list[str], jogada: list) -> None:
        self.nome = nome
        self.mão = mão
        self.jogada = jogada

    def ordenar_mão_jogada(self, mão_jogada: list[str]) -> None:
        """Utilizando o metodo de selectionsort para ordenar a mão do jogador"""
        baralho = {'KP': 1, 'KC': 2, 'KE': 3, 'KO': 4,
                   'QP': 5, 'QC': 6, 'QE': 7, 'QO': 8,
                   'JP': 9, 'JC': 10, 'JE': 11, 'JO': 12,
                   '10P': 13, '10C': 14, '10E': 15, '10O': 16,
                   '9P': 17, '9C': 18, '9E': 19, '9O': 20,
                   '8P': 21, '8C': 22, '8E': 23, '8O': 24,
                   '7P': 25, '7C': 26, '7E': 27, '7O': 28,
                   '6P': 29, '6C': 30, '6E': 31, '6O': 32,
                   '5P': 33, '5C': 34, '5E': 35, '5O': 36,
                   '4P': 37, '4C': 38, '4E': 39, '4O': 40,
                   '3P': 41, '3C': 42, '3E': 43, '3O': 44,
                   '2P': 45, '2C': 46, '2E': 47, '2O': 48,
                   'AP': 49, 'AC': 50, 'AE': 51, 'AO': 52}

        for indice in range(len(mão_jogada) - 1):
            minimo = indice
            for j in range(indice + 1, len(mão_jogada)):
                minimo_agora = baralho[mão_jogada[minimo]]
                possivel_minimo = baralho[mão_jogada[j]]
                if possivel_minimo < minimo_agora:
                    minimo = j
            aux = mão_jogada[indice]
            mão_jogada[indice] = mão_jogada[minimo]
            mão_jogada[minimo] = aux

        return

    def buscar_jogada(self, ultima_jogada: str) -> list:
        """Calcula qual vai ser a carta que o jogador ira jogar na pilha,
           e qual carta ele vai dizer que jogou"""
        tipo_cartas = {"K": 1, "Q": 2, "J": 3, "10": 4, "9": 5, "8": 6, "7": 7,
                       "6": 8, "5": 9, "4": 10, "3": 11, "2": 12, "A": 13}
        e = 0
        d = len(self.mão) - 1
        carta_mão = False
        # Utiliza busca binaria para ver se o jogador possui a ultima carta jogada

        while e <= d:
            m = (e + d) // 2
            if tipo_cartas[self.mão[m][:-1]] == tipo_cartas[ultima_jogada]:
                carta_mão = True
                return [ultima_jogada, self.mão[m], m]
            if tipo_cartas[self.mão[m][:-1]] < tipo_cartas[ultima_jogada]:
                e = m + 1
            else:
                d = m - 1

        if not carta_mão:
            for indice in range(len(self.mão) - 1, -1, -1):
                if tipo_cartas[self.mão[indice][:-1]] < tipo_cartas[ultima_jogada]:
                    ultima_jogada = self.mão[indice][:-1]
                    carta_mão = True
                    return [ultima_jogada, self.mão[indice], indice]
            if not carta_mão:
                # Nessa situação o jogador mente, uma vez que não tenha carta igual a ultima jogada ou maior que ela
                jogada = self.mão[len(self.mão) - 1]
                return [ultima_jogada, jogada, len(self.mão) - 1]


def criar_jogadores(numero_jogadores: int) -> list[Jogador]:
    """Cria o jogador de acordo com as inforamaões recebidas e ordena a mão dele"""
    list_jogadores = []

    for n in range(1, numero_jogadores + 1):
        mão_jogador = input().split(", ")
        jogador = Jogador(n, mão_jogador, [])
        jogador.ordenar_mão_jogada(jogador.mão)
        list_jogadores.append(jogador)

    return list_jogadores


def chama_jogadas(ganhador: str, list_jogadores: list,
                  jogadas_antes_duvido: int, pilha: list,
                  ultima_jogada: str, ultimo_jogador: int,
                  numero_jogadores: int) -> None:
    """Faz as jogadas acontecerem"""
    while True:
        if ganhador != "ninguém":
            break
        ganhador, ultimo_jogador, pilha, ultima_jogada = jogar(list_jogadores, jogadas_antes_duvido,
                                                               pilha, ultima_jogada, ultimo_jogador)
        if ganhador == "ninguém":
            ganhador, pilha, ultima_jogada = duvidou(ultimo_jogador, pilha, numero_jogadores,
                                                     ultima_jogada, list_jogadores)


def print_mãojogador(list_jogador: list[Jogador], pilha: list) -> None:
    """Mostra na tela a mão de cada jogador e a pilha de cartas"""
    for jogador in list_jogador:
        print("Jogador", jogador.nome)
        if jogador.mão == []:
            print("Mão:")
        else:
            print("Mão:", " ".join(jogador.mão))
    print("Pilha:")
    return


def jogar(list_jogadores: list[Jogador], jogadas_antes_duvido: int,
          pilha: list, ultima_jogada: str, ultimo_jogador: int) -> list:
    """Faz a jogada dos jogadores, conferi se alguem venceu,
    e mostra pra pessoa qual foi a jogada, como a pilha tá ficando
    e se obtiver um ganhador quem é, isso ocorre até chegar o momento do duvido"""
    while True:
        if ultimo_jogador == len(list_jogadores):
            ultimo_jogador = 0
        for jogador in list_jogadores[ultimo_jogador:]:
            ultimo_jogador += 1
            cartas_jogadas = []
            ultima_jogada, jogada, indice = jogador.buscar_jogada(ultima_jogada)
            cartas_jogadas.append(jogada)
            numero_cartas_jogadas = 1

            for carta in jogador.mão:
                if carta in cartas_jogadas:
                    pass
                    # Só pra ter certeza que não vai pegar carta repetida
                elif carta[:-1] == jogada[:-1]:
                    cartas_jogadas.append(carta)
                    numero_cartas_jogadas += 1
            jogador.jogada = cartas_jogadas
            jogador.ordenar_mão_jogada(jogador.jogada)

            for carta_mão in cartas_jogadas:
                jogador.mão.remove(carta_mão)
            pilha.extend(jogador.jogada[::-1])
            print("[Jogador {}] {} carta(s) {}".format(jogador.nome, numero_cartas_jogadas, ultima_jogada))
            print("Pilha:", " ".join(pilha))
            jogadas_antes_duvido -= 1

            if jogadas_antes_duvido == 0:
                return ["ninguém", jogador.nome, pilha, ultima_jogada]
            if jogador.mão == []:
                print("Jogador {} é o vencedor!".format(jogador.nome))
                return [jogador.nome, jogador.nome, pilha, ultima_jogada]


def duvidou(ultimo_jogador: int, pilha: list[str], numero_jogadores: int,
            ultima_jogada: str, list_jogadores: list[Jogador]) -> list:
    """Chegou o momneto de um jogador seguinte duvidar da jogada do ultimo jogador,
       então conferi se o ultimo jogador mintiu mesmo ou não """
    jogador_duvido = ultimo_jogador + 1
    if jogador_duvido > numero_jogadores:
        jogador_duvido = 1
    print("Jogador", jogador_duvido, "duvidou.")

    if ultima_jogada == pilha[len(pilha) - 1][:-1]:
        jogador = list_jogadores[jogador_duvido - 1]
        jogador.mão.extend(pilha)
        jogada_certa = True
    else:
        jogador = list_jogadores[ultimo_jogador - 1]
        jogador.mão.extend(pilha)
        jogada_certa = False
    jogador.ordenar_mão_jogada(jogador.mão)

    pilha = []
    ultima_jogada = "A"
    print_mãojogador(list_jogadores, pilha)
    if jogada_certa:
        jogador_certo = list_jogadores[ultimo_jogador - 1]
        if jogador_certo.mão == []:
            print("Jogador {} é o vencedor!".format(jogador_certo.nome))
            return [jogador_certo.nome, pilha, ultima_jogada]
    return ["ninguém", pilha, ultima_jogada]


def main() -> None:
    """Recebe os inputs  e chama as funções"""
    numero_jogadores = int(input())
    list_jogadores = criar_jogadores(numero_jogadores)
    jogadas_antes_duvido = int(input())
    print_mãojogador(list_jogadores, [])
    chama_jogadas("ninguém", list_jogadores, jogadas_antes_duvido,
                  [], "A", 0, numero_jogadores)


if __name__ == "__main__":
    main()
