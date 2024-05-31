def escaneamento_ambiente(matriz_comodo: list[list]):
    """Modo do robo em que ele olha o comodo e procura sujeira ao seu redor,
        se encontra alguma muda para o modo limpando, nesse caso é uma função
        no codigo, e muda para o modo finalizar limpeza quando termina de
        passar por todo o comodo, nesse caso é a função finalizar_limpeza"""
    i = 0
    for indice_mc in range(len(matriz_comodo)):
        linha = matriz_comodo[indice_mc]
        if i % 2 == 0:
            j = 0
        else:
            j = len(linha) - 1
            linha = linha.copy()
            linha = linha[::-1]
        for indice_l in range(len(linha)):
            posição_matriz = linha[indice_l]
            if posição_matriz == "r":
                if (j != len(linha) - 1) and (j != 0) and (i != 0) and (i != len(matriz_comodo) - 1):
                    # esses if conferem onde o r tá mais ou menos, para quando o codigo buscar a sujeira não ter um IndexErro
                    if "o" in (matriz_comodo[i][j - 1], matriz_comodo[i][j + 1],
                               matriz_comodo[i - 1][j], matriz_comodo[i + 1][j]):
                        posição_retorno = [i, j]
                        return limpando(matriz_comodo, posição_retorno)
                    else:
                        matriz_comodo[i][j] = "."
                        if i % 2 == 0:
                            matriz_comodo[i][j + 1] = "r"
                            j += 1
                        else:
                            matriz_comodo[i][j - 1] = "r"
                            linha = matriz_comodo[i].copy()
                            linha.reverse()
                            j -= 1
                        print_situação(matriz_comodo)
                elif j == 0 and i == 0:
                    if "o" in (matriz_comodo[i][j + 1], matriz_comodo[i + 1][j]):
                        posição_retorno = [i, j]
                        return limpando(matriz_comodo, posição_retorno)
                    else:
                        matriz_comodo[i][j] = "."
                        matriz_comodo[i][j + 1] = "r"
                        j += 1
                        print_situação(matriz_comodo)
                elif j == len(linha) - 1 and i == len(matriz_comodo) - 1:
                    if "o" in (matriz_comodo[i][j - 1], matriz_comodo[i - 1][j]):
                        posição_retorno = [i, j]
                        return limpando(matriz_comodo, posição_retorno)
                    else:
                        matriz_comodo[i][j] = "."
                        if i % 2 == 0:
                            matriz_comodo[i][j] = "r"
                            return finalizar_limpeza(matriz_comodo)
                        else:
                            matriz_comodo[i][j - 1] = "r"
                            linha = matriz_comodo[i].copy()
                            linha.reverse()
                            j -= 1
                            print_situação(matriz_comodo)
                elif j == 0 and i != 0 and i != len(matriz_comodo) - 1:
                    if "o" in (matriz_comodo[i][j + 1], matriz_comodo[i - 1][j]):
                        posição_retorno = [i, j]
                        return limpando(matriz_comodo, posição_retorno)
                    else:
                        matriz_comodo[i][j] = "."
                        if i % 2 == 0:
                            matriz_comodo[i][j + 1] = "r"
                            j += 1
                        else:
                            matriz_comodo[i + 1][j] = "r"
                            linha = matriz_comodo[i].copy()
                            linha.reverse()
                            j -= 1
                        print_situação(matriz_comodo)
                elif i == 0 and j != 0 and j != len(linha) - 1:
                    if "o" in (matriz_comodo[i][j - 1], matriz_comodo[i][j + 1], matriz_comodo[i + 1][j]):
                        posição_retorno = [i, j]
                        return limpando(matriz_comodo, posição_retorno)
                    else:
                        matriz_comodo[i][j] = "."
                        matriz_comodo[i][j + 1] = "r"
                        j += 1
                        print_situação(matriz_comodo)
                elif j == len(linha) - 1 and i != 0 and i != len(matriz_comodo) - 1:
                    if "o" in (matriz_comodo[i][j - 1], matriz_comodo[i - 1][j], matriz_comodo[i + 1][j]):
                        posição_retorno = [i, j]
                        return limpando(matriz_comodo, posição_retorno)
                    else:
                        matriz_comodo[i][j] = "."
                        if i % 2 == 0:
                            matriz_comodo[i + 1][j] = "r"
                        else:
                            matriz_comodo[i][j - 1] = "r"
                            linha = matriz_comodo[i].copy()
                            linha.reverse()
                            j -= 1
                        print_situação(matriz_comodo)
                elif i == len(matriz_comodo) - 1 and j != 0 and j != len(linha) - 1:
                    if "o" in (matriz_comodo[i][j - 1], matriz_comodo[i][j + 1], matriz_comodo[i - 1][j]):
                        posição_retorno = [i, j]
                        return limpando(matriz_comodo, posição_retorno)
                    else:
                        matriz_comodo[i][j] = "."
                        if i % 2 == 0:
                            matriz_comodo[i][j + 1] = "r"
                            j += 1
                        else:
                            matriz_comodo[i][j - 1] = "r"
                            linha = matriz_comodo[i].copy()
                            linha.reverse()
                            j -= 1
                        print_situação(matriz_comodo)
                elif i == 0 and j == len(linha) - 1:
                    if "o" in (matriz_comodo[i][j - 1], matriz_comodo[i + 1][j]):
                        posição_retorno = [i, j]
                        return limpando(matriz_comodo, posição_retorno)
                    else:
                        matriz_comodo[0][j] = "."
                        matriz_comodo[1][j] = "r"
                        print_situação(matriz_comodo)
                elif j == 0 and i == len(matriz_comodo) - 1:
                    if "o" in (matriz_comodo[i - 1][j], matriz_comodo[i][j + 1]):
                        posição_retorno = [i, j]
                        return limpando(matriz_comodo, posição_retorno)
                    else:
                        matriz_comodo[i][j] = "."
                        if i % 2 == 0:
                            matriz_comodo[i][j + 1] = "r"
                            j += 1
                            print_situação(matriz_comodo)
                        else:
                            matriz_comodo[i][0] = "r"
                            return finalizar_limpeza(matriz_comodo)
            if posição_matriz == "o" or posição_matriz == ".":
                if i % 2 == 0:
                    j += 1
                else:
                    j -= 1
        i += 1
    return


def limpando(matriz_comodo: list[list], posição_retorno: list[int]):
    """Procura a posição do robo e olha se ao seu arredor possui sujeira,
        quando não encontra mais sujeira muda de modo para retorna a posição."""
    pr1, pr2 = posição_retorno
    vezes_limpas = 0
    while True:
        i = 0
        posição_seguinte = 1
        for linha in matriz_comodo:
            i_inicial = i
            j = 0
            for posição_matriz in linha:
                if posição_matriz == "r":
                    if j != 0 and matriz_comodo[i][j - 1] == "o":
                        matriz_comodo[i][j] = "."
                        matriz_comodo[i][j - 1] = "r"
                        j -= 1
                        vezes_limpas += 1
                        print_situação(matriz_comodo)
                        if i % 2 != 0 and vezes_limpas == posição_seguinte:
                            # para saber se a posição que o robo esta indo é a posição seguinte no cômodo
                            pr1 = i
                            pr2 = j
                            posição_seguinte += 1
                    elif j != len(linha) - 1 and matriz_comodo[i][j + 1] == "o":
                        matriz_comodo[i][j + 1] = "r"
                        matriz_comodo[i][j] = "."
                        j += 1
                        vezes_limpas += 1
                        print_situação(matriz_comodo)
                        if i % 2 == 0 and vezes_limpas == posição_seguinte:
                            pr1 = i
                            pr2 = j
                            posição_seguinte += 1
                    elif i != 0 and matriz_comodo[i - 1][j] == "o":
                        matriz_comodo[i][j] = "."
                        matriz_comodo[i - 1][j] = "r"
                        i -= 1
                        vezes_limpas += 1
                        print_situação(matriz_comodo)
                    elif i != len(matriz_comodo) - 1 and matriz_comodo[i + 1][j] == "o":
                        matriz_comodo[i][j] = "."
                        matriz_comodo[i + 1][j] = "r"
                        i += 1
                        vezes_limpas += 1
                        print_situação(matriz_comodo)
                        if i % 2 == 0 and j == 0 and vezes_limpas == posição_seguinte:
                            pr1 = i
                            pr2 = j
                            posição_seguinte += 1
                        elif i % 2 != 0 and j == len(linha) - 1 and vezes_limpas == posição_seguinte:
                            pr1 = i
                            pr2 = j
                            posição_seguinte += 1
                    else:
                        return retomar_escaneamento(matriz_comodo, pr1, pr2)
                elif posição_matriz == "." or posição_matriz == "o":
                    j += 1
            if i_inicial == i:
                i += 1


def retomar_escaneamento(matriz_comodo: list[list], pr1: int, pr2: int):
    """Ao finalizar o modo de limpeza, o robo inicia a sua volta para a
        posição em que saiu ao iniciar a limpeza, depois de retornar a posição,
        o robo volta para o modo de escaneamento"""
    while True:
        i = 0
        for linha in matriz_comodo:
            i_inicial = i
            j = 0
            if matriz_comodo[pr1][pr2] == "r":
                return escaneamento_ambiente(matriz_comodo)
            for posição_matriz in linha:
                if posição_matriz == "r":
                    if j < pr2 and i != pr1:
                        matriz_comodo[i][j + 1] = "r"
                        matriz_comodo[i][j] = "."
                        j += 1
                        print_situação(matriz_comodo)
                        return limpando(matriz_comodo, [pr1, pr2])
                    elif j > pr2 and i != pr1:
                        matriz_comodo[i][j - 1] = "r"
                        matriz_comodo[i][j] = "."
                        j -= 1
                        print_situação(matriz_comodo)
                        return limpando(matriz_comodo, [pr1, pr2])
                    elif j == pr2 and i > pr1:
                        matriz_comodo[i - 1][j] = "r"
                        matriz_comodo[i][j] = "."
                        i -= 1
                        print_situação(matriz_comodo)
                        return limpando(matriz_comodo, [pr1, pr2])
                    elif j == pr2 and i < pr1:
                        matriz_comodo[i + 1][j] = "r"
                        matriz_comodo[i][j] = "."
                        i += 1
                        print_situação(matriz_comodo)
                        return limpando(matriz_comodo, [pr1, pr2])
                elif posição_matriz == "." or posição_matriz == "o":
                    j += 1
            if i_inicial == i:
                i += 1


def finalizar_limpeza(matriz_comodo: list[list]):
    """Confere se tudo foi limpo, depois coloca o robo na posição final, e
        desliga o robo, terminando o codigo, se não encontra tudo limpo, o
        robo volta para o modo de escaneamento em busca da sujeira"""
    limpo = True
    for linha in matriz_comodo:
        # confire se realmente o robo limpo todo o comodo
        if "o" in linha:
            limpo = False
    if limpo:
        if "r" in matriz_comodo[-1][-1]:
            return
        elif "r" in matriz_comodo[-1][0]:
            j = 0
            while j < len(matriz_comodo[-1]) - 1:
                matriz_comodo[len(matriz_comodo) - 1][j] = "."
                matriz_comodo[len(matriz_comodo) - 1][j + 1] = "r"
                j += 1
                print_situação(matriz_comodo)
                if "r" in matriz_comodo[-1][-1]:
                    matriz_comodo[-1][-1] = "."
                    return
    else:
        return escaneamento_ambiente(matriz_comodo)


def print_situação(matriz_comodo: list[list]):
    """A cada movimento do robo esta função é chamada para imprimir na tela
        qual é a situação do ambiente, mas na primeira vez é chamada para
        mostrar qual a situação inicial do ambiente"""
    for posição_matriz in matriz_comodo:
        print(" ".join(posição_matriz))
    print()
    return


def main():
    numero_linhas = int(input())
    matriz_comodo = []
    for n in range(numero_linhas):
        linha_matriz = input().split()
        matriz_comodo.append(linha_matriz)
    print_situação(matriz_comodo)
    escaneamento_ambiente(matriz_comodo)


if __name__ == "__main__":
    main()
