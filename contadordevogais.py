digite = str(input("digite algo: ")).upper()
vogais = "AEIOU"
contador = 0

for i in digite:
    if i in vogais:
        print(i, "e vogal")
        contador += 1
        print(contador)
    else:
        print(i,"nao e vogal")
