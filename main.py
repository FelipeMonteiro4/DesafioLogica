name = "Gerson"
xp = 7070

def calculo():
    rank = "Ferro"

    if xp >= 10001:
        rank = "Radiante"

    if xp >= 9001 and xp <= 10000:
        rank = "Imortal"

    if xp >= 8001 and xp <= 9000:
        rank = "Ascendente"

    if xp >= 7001 and xp <= 8000:
        rank = "Platina"

    if xp >= 5001 and xp <= 7000:
        rank = "Ouro"

    if xp >= 2001 and xp <= 5000:
        rank = "Prata"

    if xp >= 1001 and xp <= 2000:
        rank = "Bronze"

    print("O herói de nome " + name + " está no nível de " + rank)


calculo()