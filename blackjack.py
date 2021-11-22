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
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Koliko ćete novca uloziti? '))
        except:
            print('Molimo upišite broj.')
        else:
            if chips.bet > chips.total:
                print('Nemate dovoljno novca!. Imate {} KM'.format(chips.total))
            else:
                break


def hit(deck, hand):
    karta = deck.podijeli_kartu()
    hand.dodaj_kartu(karta)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Uzmi dodatnu kartu ili ne ? (da,ne)')

        if x == 'da':
            hit(deck, hand)
        elif x == 'ne':
            print('Igrač čeka djelitelja.')
            playing = False
        else:
            print('Ukucajte da ili ne.')
            continue
        break


def prikazi_neke_karte(igrac, djelitelj):

    print('\n Karte djelitelja:')
    print('Prva karta skrivena')
    print(djelitelj.karte[1])

    print('\n Karte igrača:')
    for karta in igrac.karte:
        print(karta)


def prikazi_sve_karte(igrac, djelitelj):

    print('\n Karte djelitelja:')
    for karta in djelitelj.karte:
        print(karta)

    print(f'Vrijednost karti djelitelja: {djelitelj.value}')

    print('\n Karte igrača:')
    for karta in igrac.karte:
        print(karta)

    print(f'Vrijednost karti igrača: {igrac.value}')


def igrac_izgubio(igrac, djelitelj, novac):
    print('Igrač izgubio.')
    novac.lose_bet()


def igrac_pobijedio(igrac, djelitelj, novac):
    print('Igrač pobijedio.')
    novac.win_bet()


def djelitelj_izgubio(igrac, djelitelj, novac):
    print('Djelitelj Izgubio.')
    novac.win_bet()


def djelitelj_pobijedio(igrac, djelitelj, novac):
    print('Djelitelj pobijedio.')
    novac.lose_bet()


def nerijeseno(igrac, djelitelj):
    print('NERIJEŠENO!')
