import random

suits = ('Srce', 'Karo', 'Pik', 'Tref')
ranks = ('Dva', 'Tri', 'Četiri', 'Pet', 'Šest', 'Sedam',
         'Osam', 'Devet', 'Deset', 'Žandar', 'Kraljica', 'Kralj', 'As')
values = {'Dva': 2, 'Tri': 3, 'Četiri': 4, 'Pet': 5, 'Šest': 6, 'Sedam': 7, 'Osam': 8,
          'Devet': 9, 'Deset': 10, 'Žandar': 10, 'Kraljica': 10, 'Kralj': 10, 'As': 11}

playing = True


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self) -> str:
        return '-'*5 + f' {self.rank} {self.suit} ' + '-'*5


class Deck():
    def __init__(self):
        self.sve_karte = []
        for suit in suits:
            for rank in ranks:
                karta = Card(suit, rank)
                self.sve_karte.append(karta)

    def __str__(self):
        return f'{len(self.sve_karte)} karte.'

    def promijesaj(self):
        random.shuffle(self.sve_karte)

    def podijeli_kartu(self):
        self.sve_karte.pop()


spil = Deck()
spil.promijesaj()
print(spil.sve_karte[45])
