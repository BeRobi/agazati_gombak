import random


def vel_szam():
    v_szam = int(random.random()*50 + 1)
    print(f"\nI/A:\n\tA generált szám: {v_szam}")
    print("\nI/B:")
    oszthato(v_szam)


def oszthato(v_szam):
    if v_szam % 5 == 0:
        print("\tA szám 5-tel osztható!")
    elif v_szam % 3 == 0:
        print("\tA szám 3-mal osztható!")
    elif v_szam % 5 == 0 and v_szam % 3 == 0:
        print("\tA szám 5-tel és 3-mal is osztható!")
