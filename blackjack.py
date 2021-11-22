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
        return self.sve_karte.pop()


class Hand():
    def __init__(self):
        self.karte = []
        self.value = 0
        self.aces = 0

    def dodaj_kartu(self, karta):
        self.karte.append(karta)
        self.value += values[karta.rank]
        if karta.rank == 'As':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
