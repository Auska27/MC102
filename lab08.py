def categoria_simples(categoria_avaliada: str, filme_avaliado: list,
                      categoria: list, nota: list) -> list:
    """Calcula quem é o ganhador da categoria selecionada"""
    filme_nota = {}
    quantidade_votos = {}
    for indice in range(len(categoria)):
        if categoria_avaliada == categoria[indice]:
            if filme_avaliado[indice] in filme_nota:
                filme_nota[filme_avaliado[indice]] = nota[indice] + filme_nota[filme_avaliado[indice]]
                quantidade_votos[filme_avaliado[indice]] += 1
            else:
                filme_nota[filme_avaliado[indice]] = nota[indice]
                quantidade_votos[filme_avaliado[indice]] = 1
    media_nota = {}
    for chave in filme_nota:
        media_nota[chave] = filme_nota[chave]/quantidade_votos[chave]
    nota_ganhadora = 0
    for filme in media_nota:
        if media_nota[filme] > nota_ganhadora:
            nota_ganhadora = media_nota[filme]
            filme_ganhador = filme
        elif media_nota[filme] == nota_ganhadora:
            if quantidade_votos[filme] > quantidade_votos[filme_ganhador]:
                filme_ganhador = filme
                nota_ganhadora = media_nota[filme]
    return [filme_ganhador, nota_ganhadora]


def categoria_especial(filmes_ganhadores: list, notas_ganhadores: list,
                       lista_filme: list, filme_avaliado: list) -> list:
    """Calcula quem são os ganhadores das categorias especiais"""
    dicionario_ganhadores = {}
    for gc in filmes_ganhadores:
        if gc in dicionario_ganhadores:
            dicionario_ganhadores[gc] += 1
        else:
            dicionario_ganhadores[gc] = 1
    vezes_ganhas = 0
    pontuacao1 = 0
    pontuacao2 = 0
    for filme in dicionario_ganhadores:
        if dicionario_ganhadores[filme] > vezes_ganhas:
            vezes_ganhas = dicionario_ganhadores[filme]
            ganhador_piorfilme = filme
        elif dicionario_ganhadores[filme] == vezes_ganhas:
            for f in range(len(filmes_ganhadores)):
                if filmes_ganhadores[f] == filme:
                    pontuacao1 += notas_ganhadores[f]
                elif filmes_ganhadores[f] == ganhador_piorfilme:
                    pontuacao2 += notas_ganhadores[f]
            if pontuacao1 > pontuacao2:
                ganhador_piorfilme = filme
    ganhador_nãomerecia = []
    for lf in lista_filme:
        if lf not in filme_avaliado:
            ganhador_nãomerecia.append(lf)
    if len(ganhador_nãomerecia) == 0:
        ganhador_nãomerecia.append("sem ganhadores")
    return [ganhador_piorfilme, ganhador_nãomerecia]


def main() -> None:
    F = int(input())
    lista_filme = []
    for f in range(F):
        nome_filme = input()
        lista_filme.append(nome_filme)

    Q = int(input())
    avaliador = []
    categoria = []
    filme_avaliado = []
    nota = []
    for q in range(Q):
        informações = input().split(", ")
        for i in range(0, len(informações), 4):
            avaliador.append(informações[0])
            categoria.append(informações[1])
            filme_avaliado.append(informações[2])
            nota.append(int(informações[3]))

    filmes_ganhadores = []
    notas_ganhadores = []
    print("#### abacaxi de ouro ####")
    print()
    print("categorias simples")
    print("categoria: filme que causou mais bocejos")
    ganhador_categoria1, nota_categoria1 = categoria_simples("filme que causou mais bocejos", filme_avaliado, categoria, nota)
    filmes_ganhadores.append(ganhador_categoria1)
    notas_ganhadores.append(nota_categoria1)
    print("-", ganhador_categoria1)
    ganhador_categoria2, nota_categoria2 = categoria_simples("filme que foi mais pausado", filme_avaliado, categoria, nota)
    filmes_ganhadores.append(ganhador_categoria2)
    notas_ganhadores.append(nota_categoria2)
    print("categoria: filme que foi mais pausado")
    print("-", ganhador_categoria2)
    ganhador_categoria3, nota_categoria3 = categoria_simples("filme que mais revirou olhos", filme_avaliado, categoria, nota)
    filmes_ganhadores.append(ganhador_categoria3)
    notas_ganhadores.append(nota_categoria3)
    print("categoria: filme que mais revirou olhos")
    print("-", ganhador_categoria3)
    ganhador_categoria4, nota_categoria4 = categoria_simples("filme que não gerou discussão nas redes sociais", filme_avaliado, categoria, nota)
    filmes_ganhadores.append(ganhador_categoria4)
    notas_ganhadores.append(nota_categoria4)
    print("categoria: filme que não gerou discussão nas redes sociais")
    print("-", ganhador_categoria4)
    ganhador_categoria5, nota_categoria5 = categoria_simples("enredo mais sem noção", filme_avaliado, categoria, nota)
    filmes_ganhadores.append(ganhador_categoria5)
    notas_ganhadores.append(nota_categoria5)
    print("categoria: enredo mais sem noção")
    print("-", ganhador_categoria5)
    print()
    ganhador_piorfilme, ganhador_nãomerecia = categoria_especial(filmes_ganhadores, notas_ganhadores, lista_filme, filme_avaliado)
    print("categorias especiais")
    print("prêmio pior filme do ano")
    print("-", ganhador_piorfilme)
    print("prêmio não merecia estar aqui")
    print("-", ", ".join(ganhador_nãomerecia))


if __name__ == "__main__":
    main()
