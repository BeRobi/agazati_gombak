from Gomba import Gomba


def beker():
    lista = []
    while len(lista) < 5:
        kor = int(input(f"Adja meg a(z) {len(lista)+1} személy korát!"))
        if (kor >= 0) & (kor <= 120):
            lista.append(kor)
        else:
            print("Helytelen kor!")
    return lista


def osszefuz(lista, elvalaszto):
    i = 0
    szamsor = ""
    while i < len(lista):
        if i == len(lista)-1:
            szamsor += str(lista[i])
        else:
            szamsor += str(lista[i]) + elvalaszto
        i += 1
    print(f"\t{szamsor}")


def elso_idos(lista):
    i = 0
    hely = -1
    # -1-es indexszám nem létezik, ez érvénytelen adat, azt jelöli,
    # hogy nincs még olyanunk, ami megfelelne a feltételnek
    while i < len(lista) and hely == -1:
        if int(lista[i]) > 70:
            hely = i + 1
            # i = len(korok)  - ez nem is fog kelleni, mert a helyet is hozzáadtuk fent
        i += 1
    return hely


def konzolra_ir(lista):
    index = elso_idos(lista)
    print(f"\tElső idős ember korának helye a listában: {index}.")


def fajl_ir(lista):
    fajl = open("oreg.txt", "w", encoding="UTF-8")
    index = elso_idos(lista)
    fajl.write(f"Első idős ember korának helye a listában: {index}.")
    fajl.close()
    print("\tAz írás elkészült!")


def beolvas():
    gombak = []
    fajl = open("gombak_jav.txt", "r", encoding="UTF-8")
    fajl.readline()
    gomba = fajl.readlines()
    fajl.close()
    i = 0
    while i < len(gomba):
        sor = gomba[i].strip().split("@")
        gombak.append(Gomba(sor))
        i += 1
    return gombak


def gombak_szama(gombak):
    print(f"\nIII/A, B:\n\tA gombák száma: {len(gombak)}.")


def papsapka(gombak):
    i = 0
    while i < len(gombak) and gombak[i].nemz != "papsapkagombák ":
        i += 1
    if i < len(gombak):
        print(f"\nIII/C:\n\tAz első papsapkagomba neve: {gombak[i].nev}")


def tinoru(gombak):
    i = 0
    db = 0
    while i < len(gombak):
        if gombak[i].nemz == "tinóru":
            db += 1
        i += 1
    print(f"\nIII/D:\n\tA tinóru gombák száma: {db}.")
