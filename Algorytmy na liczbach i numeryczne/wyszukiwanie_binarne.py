tab = []
for x in range(11):
    tab.append(x)

lewy = 1
prawy = len(tab)
szukana = 6

while prawy > lewy:
    srodek = int((lewy + prawy) / 2)
    if szukana > tab[srodek]:
        lewy = srodek+1
    else:
        prawy = srodek

if tab[lewy] == szukana:
    indeks = lewy
else:
    indeks = None

print(tab[indeks]) #wynik
