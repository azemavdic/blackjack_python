import random

suits = ('Srce', 'Karo', 'Pik', 'Tref')
ranks = ('Dva', 'Tri', 'Četiri', 'Pet', 'Šest', 'Sedam',
         'Osam', 'Devet', 'Deset', 'Žandar', 'Kraljica', 'Kralj', 'As')
values = {'Dva': 2, 'Tri': 3, 'Četiri': 4, 'Pet': 5, 'Šest': 6, 'Sedam': 7, 'Osam': 8,
          'Devet': 9, 'Deset': 10, 'Žandar': 11, 'Kraljica': 12, 'Kralj': 13, 'As': 14}

# Klasa Karta


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' ' + self.suit

# Klasa Špil


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def promijesaj(self):
        random.shuffle(self.all_cards)

    def podijeli_zadnju_kartu(self):
        return self.all_cards.pop()

# Klasa Igrač


class Igrac():
    def __init__(self, ime):
        self.ime = ime
        self.all_cards = []

    def ukloni_jednu(self):
        return self.all_cards.pop(0)

    def dodaj_karte(self, nove_karte):
        if type(nove_karte) == type([]):
            self.all_cards.extend(nove_karte)
        else:
            self.all_cards.append(nove_karte)

    def __str__(self) -> str:
        return f'Igrač {self.ime} ima {len(self.all_cards)} karti.'


# GAME SETUP

igrac1 = Igrac(input('Igrač 1: '))
igrac2 = Igrac(input('Igrač 2: '))
novi_spil = Deck()
novi_spil.promijesaj()

for x in range(26):
    igrac1.dodaj_karte(novi_spil.podijeli_zadnju_kartu())
    igrac2.dodaj_karte(novi_spil.podijeli_zadnju_kartu())

game_on = True

broj_rundi = 0

while game_on:
    broj_rundi += 1
    print(f'{broj_rundi}. runda')

    if len(igrac1.all_cards) == 0:
        print(f'{igrac1.ime} nema više karti. {igrac2.ime} je pobijedio.')
        game_on = False
        break

    if len(igrac2.all_cards) == 0:
        print(f'{igrac2.ime} nema više karti. {igrac1.ime} je pobijedio.')
        game_on = False
        break

    igrac1_karte_na_stolu = []
    igrac1_karte_na_stolu.append(igrac1.ukloni_jednu())
    igrac2_karte_na_stolu = []
    igrac2_karte_na_stolu.append(igrac2.ukloni_jednu())

    at_war = True

    while at_war:
        if igrac1_karte_na_stolu[-1].value > igrac2_karte_na_stolu[-1].value:
            igrac1.dodaj_karte(igrac1_karte_na_stolu)
            igrac1.dodaj_karte(igrac2_karte_na_stolu)
            at_war = False
        elif igrac1_karte_na_stolu[-1].value < igrac2_karte_na_stolu[-1].value:
            igrac2.dodaj_karte(igrac1_karte_na_stolu)
            igrac2.dodaj_karte(igrac2_karte_na_stolu)
            at_war = False
        else:
            print('BORBA!')
            if len(igrac1.all_cards) < 5:
                print(f'{igrac1.ime} nema dovoljno karti za borbu.')
                print(f'{igrac2.ime} je POBJEDNIK!')
                game_on = False
                break
            elif len(igrac2.all_cards) < 5:
                print(f'{igrac2.ime} nema dovoljno karti za borbu.')
                print(f'{igrac1.ime} je POBJEDNIK!')
                game_on = False
                break
            else:
                for num in range(5):
                    igrac1_karte_na_stolu.append(igrac1.ukloni_jednu())
                    igrac2_karte_na_stolu.append(igrac2.ukloni_jednu())
