def comparar_vetores(vetor1: list[int], vetor2: list[int], parametro1: int,
                     parametro2: int) -> list[list[int]]:
    """Compara o tamnaho dos vetores, e no menor vetor adiciona termo para
    ficar do mesmo tamanho que o outro vetor, e a operação poder ser feita"""
    if len(vetor1) < len(vetor2):
        for v1 in range(len(vetor1), len(vetor2)):
            vetor1.append(parametro1)
    elif len(vetor1) > len(vetor2):
        for v2 in range(len(vetor2), len(vetor1)):
            vetor2.append(parametro2)
    return [vetor1, vetor2]


def soma_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """Soma dois vetores entre si"""
    vetor1, vetor2 = comparar_vetores(vetor1, vetor2, 0, 0)
    vetor_soma = []
    for v in range(len(vetor2)):
        vs = vetor1[v] + vetor2[v]
        vetor_soma.append(vs)
    return vetor_soma


def subtrai_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """Subitrai dois vetores entre si"""
    vetor1, vetor2 = comparar_vetores(vetor1, vetor2, 0, 0)
    vetor_subtrai = []
    for v in range(len(vetor1)):
        vs = vetor1[v] - vetor2[v]
        vetor_subtrai.append(vs)
    return vetor_subtrai


def multiplica_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """Multiplica dois vetores entre si"""
    vetor1, vetor2 = comparar_vetores(vetor1, vetor2, 1, 1)
    vetor_multiplica = []
    for v in range(len(vetor1)):
        vm = vetor1[v] * vetor2[v]
        vetor_multiplica.append(vm)
    return vetor_multiplica


def divide_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """Divide dois vetores entre si"""
    vetor1, vetor2 = comparar_vetores(vetor1, vetor2, 0, 1)
    vetor_divide = []
    for v in range(len(vetor1)):
        vd = vetor1[v] // vetor2[v]
        vetor_divide.append(vd)
    return vetor_divide


def multiplicacao_escalar(vetor1: list[int], escalar: int) -> list[int]:
    """Multiplica cada termo do vetor por um escalar"""
    vetor_me = []
    for v in range(len(vetor1)):
        vme = vetor1[v] * escalar
        vetor_me.append(vme)
    return vetor_me


def n_duplicacao(vetor: list[int], n: int) -> list[int]:
    """Aumenta o vetor recebe ele mesmo n vezes"""
    vetor_copia = vetor[0: len(vetor)]
    if n > 1:
        while n > 1:
            vetor.extend(vetor_copia)
            n -= 1
    elif n == 0:
        vetor = []
    return vetor


def soma_elementos(vetor: list[int]) -> int:
    """Soma os elementos de um vetor"""
    soma = 0
    for v in vetor:
        soma += v
    return soma


def produto_interno(vetor1: list[int], vetor2: list[int]) -> int:
    """Multiplica elemento a elemento e depois soma o resultado"""
    vetor1, vetor2 = comparar_vetores(vetor1, vetor2, 1, 1)
    soma = 0
    for v in range(len(vetor1)):
        vpi = vetor1[v] * vetor2[v]
        soma += vpi
    return soma


def multiplica_todos(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """Multiplica cada elemento do primeiro vetor por todos os elementos do
        segundo vetor e soma o resultado."""
    lista_mt = []
    for v1 in vetor1:
        m_t = 0
        for v2 in vetor2:
            multiplica = v1 * v2
            m_t += multiplica
        lista_mt.append(m_t)
    return lista_mt


def correlacao_cruzada(vetor1: list[int], mascara: list[int]) -> list[int]:
    """Consiste em utilizar uma máscara (um vetor menor), que caminha pelo
        vetor calculando um produto interno."""
    vetor_cc = []
    for i in range(len(vetor1) - len(mascara) + 1):
        soma_cc = 0
        for j in range(len(mascara)):
            cc = vetor1[i + j] * mascara[j]
            soma_cc += cc
        vetor_cc.append(soma_cc)
        j = 0
    return vetor_cc


def lista_str_int(lista1: list[str]) -> list[int]:
    """Transforma a lista de stirngs recebida em uma lista de inteiros"""
    lista2 = []
    for l1 in range(len(lista1)):
        lista2.append(int(lista1[l1]))
    return lista2


if __name__ == "__main__":
    vetor_str = input().split(",")
    vetor = lista_str_int(vetor_str)

    while True:
        função = input()
        if função == "soma_vetores":
            vetor2_str = input().split(",")
            vetor2 = lista_str_int(vetor2_str)
            vetor = soma_vetores(vetor, vetor2)
            print(vetor)

        elif função == "subtrai_vetores":
            vetor2_str = input().split(",")
            vetor2 = lista_str_int(vetor2_str)
            vetor = subtrai_vetores(vetor, vetor2)
            print(vetor)

        elif função == "multiplica_vetores":
            vetor2_str = input().split(",")
            vetor2 = lista_str_int(vetor2_str)
            vetor = multiplica_vetores(vetor, vetor2)
            print(vetor)

        elif função == "divide_vetores":
            vetor2_str = input().split(",")
            vetor2 = lista_str_int(vetor2_str)
            vetor = divide_vetores(vetor, vetor2)
            print(vetor)

        elif função == "multiplicacao_escalar":
            escalar = int(input())
            vetor = multiplicacao_escalar(vetor, escalar)
            print(vetor)

        elif função == "n_duplicacao":
            n = int(input())
            vetor = n_duplicacao(vetor, n)
            print(vetor)

        elif função == "soma_elementos":
            vetor = [soma_elementos(vetor)]
            print(vetor)

        elif função == "produto_interno":
            vetor2_str = input().split(",")
            vetor2 = lista_str_int(vetor2_str)
            vetor = [produto_interno(vetor, vetor2)]
            print(vetor)

        elif função == "multiplica_todos":
            vetor2_str = input().split(",")
            vetor2 = lista_str_int(vetor2_str)
            vetor = multiplica_todos(vetor, vetor2)
            print(vetor)

        elif função == "correlacao_cruzada":
            mascara_str = input().split(",")
            mascara = lista_str_int(mascara_str)
            vetor = correlacao_cruzada(vetor, mascara)
            print(vetor)

        elif função == "fim":
            break
