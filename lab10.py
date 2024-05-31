class Maquina:
    """Armazena as informações da maquina"""
    def __init__(self, nome_maquina: int, pontos_vida: int,
                 pontos_ataque: int, quantidade_partes: int,
                 info_parte_corpo: list, status: str) -> None:
        self.nome_maquina = nome_maquina
        self.pontos_vida = pontos_vida
        self.pontos_ataque = pontos_ataque
        self.quantidade_partes = quantidade_partes
        self.info_parte_corpo = info_parte_corpo
        self.status = status

    def organizar_informações(self) -> list[dict]:
        """Para organizar melhor as informações recebidas sobre as partes dos corpos"""
        fraqueza_corpo = {}
        info_totais = {}
        ponto_critico_acertado = {}

        for indice in range(len(self.info_parte_corpo)):
            fraqueza_corpo[self.info_parte_corpo[indice][0]] = self.info_parte_corpo[indice][1]
            info_totais[self.info_parte_corpo[indice][0]] = (int(self.info_parte_corpo[indice][2]), (int(self.info_parte_corpo[indice][3]), int(self.info_parte_corpo[indice][4])))
            ponto_critico_acertado[(int(self.info_parte_corpo[indice][3]), int(self.info_parte_corpo[indice][4]))] = 0

        return [fraqueza_corpo, info_totais, ponto_critico_acertado]


class Ataque:
    """Armazena as informações do ataque da aloy"""
    def __init__(self, numero_ataque: int, alvo: int, parte_alvo: str,
                 tipo_flecha: str, cordenada_tiro: tuple) -> None:
        self.numero_ataque = numero_ataque
        self.alvo = alvo
        self.parte_alvo = parte_alvo
        self.tipo_flecha = tipo_flecha
        self.cordenada_tiro = cordenada_tiro


def criar_maquinas_cambate(maquinas_por_combate):
    """Cria as maquinas e organiza suas informações"""
    list_maquina = []
    maquina_info_corpo = {}

    for numero_maquina in range(maquinas_por_combate):
        infotmações_todo_corpo = []
        informações_gerais = input().split()
        informações_parte_corpo = input().split(", ")
        infotmações_todo_corpo.append(informações_parte_corpo)
        nome_maquina = Maquina(numero_maquina, int(informações_gerais[0]),
                               int(informações_gerais[1]), int(informações_gerais[2]),
                               infotmações_todo_corpo, "vivo")
        list_maquina.append(nome_maquina)

        for info in range(1, nome_maquina.quantidade_partes):
            informações_parte_corpo = input().split(", ")
            nome_maquina.info_parte_corpo.append(informações_parte_corpo)
            maquina_info_corpo[nome_maquina.nome_maquina] = (nome_maquina.organizar_informações())

    return list_maquina, maquina_info_corpo


def luta(quantidade_flechas: int, flechas: list,
         list_maquina: list[Maquina], maquina_info_corpo: dict,
         flechas_tipo_quantidade: dict, numero_inimigos: int,
         vida_aloy: int, maquinas_por_combate: int,
         vida_total_aloy: int, combate: int) -> list:
    """Organiza o ataque, e faz o combate com as maquinas acontecer"""
    quantidade_flechas_sobraram = quantidade_flechas
    flecha_usada_quantidade = {flechas[f]: 0 for f in range(0, len(flechas) - 1, 2)}
    numero_inimigos -= maquinas_por_combate
    vida_inicial_aloy = vida_aloy
    quantidade_ataque = 0
    info_critico = {}
    maquinas_derrotadas = []
    maquina_critico = []

    while maquinas_por_combate > 0 and vida_aloy > 0 and quantidade_flechas_sobraram > 0:
        dados_ataque = input().split(", ")
        numero_ataque = Ataque(quantidade_ataque, int(dados_ataque[0]),
                               dados_ataque[1], dados_ataque[2],
                               (int(dados_ataque[3]), int(dados_ataque[4])))
        quantidade_flechas_sobraram -= 1
        flecha_usada_quantidade[numero_ataque.tipo_flecha] += 1
        info_critico, maquinas_derrotadas, maquinas_por_combate = conferir_requisito(numero_ataque, maquinas_por_combate,
                                                                                     list_maquina, info_critico,
                                                                                     maquinas_derrotadas, maquina_critico,
                                                                                     maquina_info_corpo)
        if quantidade_ataque == 2:
            vida_aloy, quantidade_ataque = dano_maquina(vida_aloy, list_maquina)
            if vida_aloy <= 0:
                break
        quantidade_ataque += 1

    if maquinas_por_combate == 0 or vida_aloy <= 0 or quantidade_flechas_sobraram <= 0:
        combate = print_indice(combate, vida_aloy, flecha_usada_quantidade,
                               vida_inicial_aloy, info_critico,
                               maquinas_derrotadas, flechas_tipo_quantidade,
                               list_maquina, quantidade_flechas_sobraram,
                               maquina_critico,  numero_inimigos)
        if vida_aloy > 0:
            vida_aloy = cura_aloy(vida_aloy, vida_total_aloy)
    return [numero_inimigos, combate, vida_aloy]


def calcular_dano(dano_máximo: int, cordenada_maquina: tuple, cordenada_tiro) -> int:
    """Calcula quanto dano a Aloy deu na maquina"""
    cx, cy = cordenada_tiro
    fx, fy = cordenada_maquina
    subtrai_cordenada_x = abs(cx - fx)
    subtrai_cordenada_y = abs(cy - fy)
    dano_dado = (dano_máximo - (subtrai_cordenada_x + subtrai_cordenada_y))

    if dano_dado <= 0:
        return 0
    return dano_dado


def conferir_requisito(numero_ataque: Ataque,  maquinas_por_combate: int,
                       list_maquina: list[Maquina], info_critico: dict,
                       maquinas_derrotadas: list, maquina_critico: list,
                       maquina_info_corpo: dict) -> list:
    """Olhar se a flecha é ponto fraco da maquina, e dpois quanto de dano a maquina recebeu (se é um critico ou não)"""
    flecha_correta = False
    nome_maquina = list_maquina[numero_ataque.alvo]

    for maquina in maquina_info_corpo.keys():
        if maquina == nome_maquina.nome_maquina:
            fraqueza_corpo, info_totais, ponto_critico_acertado = maquina_info_corpo[maquina]

    for parte_corpo, flecha_fraqueza in fraqueza_corpo.items():
        if parte_corpo == numero_ataque.parte_alvo:
            if flecha_fraqueza == "todas" or flecha_fraqueza == numero_ataque.tipo_flecha:
                flecha_correta = True
                break

    for parte_corpo, tuple_info in info_totais.items():
        if parte_corpo == numero_ataque.parte_alvo:
            if tuple_info[1] == numero_ataque.cordenada_tiro:
                if nome_maquina.nome_maquina not in maquina_critico:
                    maquina_critico.append(nome_maquina.nome_maquina)
                ponto_critico_acertado[tuple_info[1]] += 1
                info_critico[nome_maquina.nome_maquina] = ponto_critico_acertado

            if tuple_info[1] == numero_ataque.cordenada_tiro and flecha_correta:
                dano_dado = tuple_info[0]
                break

            elif flecha_correta:
                dano_dado = calcular_dano(tuple_info[0], tuple_info[1], numero_ataque.cordenada_tiro)
                break

            else:
                dano_dado = (calcular_dano(tuple_info[0], tuple_info[1], numero_ataque.cordenada_tiro)) // 2
                break

    nome_maquina.pontos_vida -= dano_dado

    if nome_maquina.pontos_vida <= 0 and nome_maquina.status == "vivo":
        nome_maquina.status = "morto"
        maquinas_por_combate -= 1
        maquinas_derrotadas.append(nome_maquina.nome_maquina)

    return [info_critico, maquinas_derrotadas, maquinas_por_combate]


def dano_maquina(vida_aloy: int, list_maquina: list[Maquina]) -> list:
    """Calcular quanto que a vida da Aloy fica depois de atirar 3 flechas"""
    for indice in range(len(list_maquina)):
        numero_maquina = list_maquina[indice]
        if numero_maquina.status == "vivo":
            vida_aloy -= numero_maquina.pontos_ataque

    quantidade_ataque = -1

    if vida_aloy < 0:
        vida_aloy = 0
    return [vida_aloy, quantidade_ataque]


def cura_aloy(vida_aloy: int, vida_total_aloy: int) -> int:
    """Cura a Aloy apos o combate """
    vida_aloy += (vida_total_aloy // 2)

    if vida_aloy > vida_total_aloy:
        vida_aloy = vida_total_aloy
    return vida_aloy


def print_indice(combate: int, vida_aloy: int, flecha_usada_quantidade: dict,
                 vida_inicial_aloy: int, info_critico: dict,
                 maquinas_derrotadas: list[int], flechas_tipo_quantidade: dict,
                 list_maquina: list[Maquina], quantidade_flechas_sobraram: int,
                 maquina_critico: list[Maquina], numero_inimigos: int) -> int:
    """Mostra para o usuario as informções sobre o que occorreu no combate,
       e se ele finalizou a batalha"""
    print("Combate {}, vida = {}".format(combate, vida_inicial_aloy))

    for maquina in maquinas_derrotadas:
        Maquina_derrotada = list_maquina[int(maquina)]
        if Maquina_derrotada.status == "morto":
            print("Máquina", maquina, "derrotada")
    print("Vida após o combate =", vida_aloy)

    if vida_aloy > 0 and quantidade_flechas_sobraram > 0:
        print("Flechas utilizadas:")
        for tipo_flecha, quantidade_usada in flecha_usada_quantidade.items():
            for tipo, quantidade in flechas_tipo_quantidade.items():
                if tipo == tipo_flecha:
                    if quantidade_usada > 0:
                        print("- {}: {}/{}".format(tipo_flecha, quantidade_usada, quantidade))

    if len(maquina_critico) > 0:
        print("Críticos acertados:")
        for maquina_critada in list_maquina:
            if maquina_critada.nome_maquina in maquina_critico:
                print("Máquina {}:".format(maquina_critada.nome_maquina))
                for maquina, critico in info_critico.items():
                    if maquina == maquina_critada.nome_maquina:
                        for ponto_critico, vezes_acertadas in critico.items():
                            if vezes_acertadas > 0:
                                print("- {}: {}x".format(ponto_critico, vezes_acertadas))

    if quantidade_flechas_sobraram == 0:
        print("Aloy ficou sem flechas e recomeçará sua missão mais preparada.")
    elif vida_aloy == 0:
        print("Aloy foi derrotada em combate e não retornará a tribo.")
    elif numero_inimigos == 0:
        print("Aloy provou seu valor e voltou para sua tribo.")

    combate += 1
    return combate


def main() -> None:
    """Recebe os inputs, organiza as informações e chama as outras funções"""
    vida_aloy = int(input())
    vida_total_aloy = vida_aloy
    flechas = input().split()
    quantidade_flechas = 0
    flechas_tipo_quantidade = {}
    flecha_usada_quantidade = {}

    for f in range(0, len(flechas) - 1, 2):
        flechas_tipo_quantidade[flechas[f]] = int(flechas[f + 1])
        flecha_usada_quantidade[flechas[f]] = 0
        quantidade_flechas += int(flechas[f + 1])

    numero_inimigos = int(input())
    combate = 0

    while numero_inimigos > 0 and vida_aloy > 0:
        maquinas_por_combate = int(input())
        list_maquina, maquina_info_corpo = criar_maquinas_cambate(maquinas_por_combate)
        numero_inimigos, combate, vida_aloy = luta(quantidade_flechas, flechas, list_maquina,
                                                    maquina_info_corpo, flechas_tipo_quantidade,
                                                    numero_inimigos, vida_aloy, maquinas_por_combate,
                                                    vida_total_aloy, combate)


if __name__ == "__main__":
    main()
