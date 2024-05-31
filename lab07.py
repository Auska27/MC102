def verdadeiro_caractere(caractere: str, mensagem_completa: list[str],) -> str:
    """Descobri qual é o caractectere utilizado para descobri a chave"""
    lista_vogal = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    lista_numero = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    lista_consoante = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                       'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    if caractere == "consoante":
        for mc in mensagem_completa:
            if mc.lower() in lista_consoante:
                caractere_verdadeiro = mc
                return caractere_verdadeiro
    elif caractere == "vogal":
        for mc in mensagem_completa:
            if mc in lista_vogal:
                caractere_verdadeiro = mc
                return caractere_verdadeiro
    elif caractere == "numero":
        for mc in mensagem_completa:
            if mc in lista_numero:
                caractere_verdadeiro = mc
                return caractere_verdadeiro
    else:
        return caractere


def calcular_chave(caractere1: str, caractere2: str, operador: str, mensagem_completa: list[str]) -> int:
    """Calcula o valor da chave para poder descriptografa a mensagem"""
    caractere1_verdadeiro = verdadeiro_caractere(caractere1, mensagem_completa)
    indice1 = mensagem_completa.index(caractere1_verdadeiro)
    caractere2_verdadeiro = verdadeiro_caractere(caractere2, mensagem_completa[indice1:])
    indice2 = indice1 + mensagem_completa[indice1:].index(caractere2_verdadeiro)
    if operador == "+":
        chave = indice1 + indice2
    elif operador == "-":
        chave = indice1 - indice2
    elif operador == "*":
        chave = indice1 * indice2
    return chave


def criptografia(mensagem_dividida: list[list[str]], chave: int) -> list[list[str]]:
    """Descriptografa a mensagem recebida"""
    mensagem_codificada = []
    for md in mensagem_dividida:
        linha_codificada = []
        for caractere in md:
            valor = ord(caractere)
            valor_codificado = valor + chave
            if valor_codificado > 126 or valor_codificado < 32:
                valor_codificado = (((valor_codificado - 32) % 95) + 32)
            caractere_codificado = chr(valor_codificado)
            linha_codificada.append(caractere_codificado)
        mensagem_codificada.append(linha_codificada)
    return mensagem_codificada

def main():
    """Utilizado para caso seja necessario importar o codigo, e não acabar indo algo que não é necessário"""
    operador_math = input()
    caractere_busca1 = input()
    caractere_busca2 = input()
    tamanho_mensagem = int(input())
    mensagem_dividida = []
    mensagem_completa = []
    for x in range(tamanho_mensagem):
        lista_mensagem = []
        mensagem = input()
        for m in mensagem:
            lista_mensagem.append(m)
        mensagem_dividida.append(lista_mensagem)
        mensagem_completa.extend(lista_mensagem)
    chave = calcular_chave(caractere_busca1, caractere_busca2, operador_math, mensagem_completa)
    print(chave)
    mensagem_codificada = criptografia(mensagem_dividida, chave)
    for md in mensagem_codificada:
        print("".join(md))


if __name__ == "__main__":
    main()
