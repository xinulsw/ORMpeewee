# -*- coding: utf-8 -*-
import csv
import os
from peewee import *

# sprawdzimy czy baza istnieje
if os.path.exists('calkowite.db'):
    os.remove('calkowite.db')

# stworzymy instancje bazy uzywanej przez modele
baza = SqliteDatabase('calkowite.db')

# teraz klasa bazowa z której będziemy czerpac


class BazaModel(Model):
    class Meta:
        database = baza

# teraz tabela z promieniowaniem bezposrednim


class Calkowite(BazaModel):
    data = CharField(null=False)
    pomiary = CharField(null=False)


# nawiązanie połączneia z bazą
baza.connect()
# tworzymy tabele
baza.create_table(Calkowite, True)

#############################################################################


def pobieraj_dane(plikcsv):
    """odczytamy sobie dane z pliku i dodamy do tupli"""
    dane = []
    with open(plikcsv, newline='') as zawartosc:
        reader = csv.DictReader(zawartosc, delimiter=',')
        for linia in reader:
            dane.append(linia)
    return (dane)  # przeksztalcamy liste na tuple i zwracamy ja


dane = pobieraj_dane('outputCalkowite.csv')
# print(dane)
#############################################################################

# dodamy wiele danych - rozne terminy, rozne pomiary
Calkowite.insert_many(dane).execute()

# odczytamy dane z bazy


def czytaj_baze():
    for miary in Calkowite.select():
        print(miary.data, miary.pomiary)
        print()

############################################


czytaj_baze()
